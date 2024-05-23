import json
import abbreviations as ab
import re
import os 


def extract_quote(text):
    author_regex = r"[A-Z][a-z]*(?:\. [A-Z][a-z]*| [A-Z][a-z]*| [a-z]+)"
    match = re.search(r": '([^']+)' -</i>(" + author_regex + r")", text)
    # A sequence ': ',
    # Followed by 1+ characters that are not single quotes,
    # Followed by a single quote and the string -</i>,
    # Followed by one or more characters that are not periods (capturing this as the author's name),
    # Followed by any single character.
    # text = "This is a sample text with a quote: 'This is the quoted text' -</i>Author Name."

    if match:
        return match.group(1), match.group(2), text # quote, author name, text
    else:
        return extract_example(text)

def extract_example(text):
    if ":" in text:
        parts = text.split(":", 1)
        return parts[1].strip(), "", parts[0].strip()
    else:
        return "", "", text

def extract_current_category(current_text):
    for abbreviation, category in ab.abbreviations.items():
        if abbreviation in current_text:
            current_text.replace(abbreviation, "")
            return category
        return ""

def parse_meanings(anlami):
    meanings = []
    parts = re.split(r"(\d\))", anlami) # split if there are multiple meanings (parts)
    current_text = "" 
    for part in parts:
        if re.match(r"\d\)", part): # if there's numbering e.g. 1) this is a meaning, 2) another meaning
            if current_text:
                quote_text, author, current_text = extract_quote(current_text)
                quote = {}
                if quote_text:
                    quote = {
                        "text": quote_text.replace("</i>", "").strip(),
                        "author": author,
                    }

                meanings.append(
                    {
                        "text": current_text.replace("</i>", "").strip(),
                        "category": current_category,
                        "quote": quote
                    }
                )
            current_text = ""
            current_category = ""
        else: # if there's only 1 meaning
            current_text += part
        current_category = extract_current_category(current_text)
    if current_text:
        quote_text, author, current_text = extract_quote(current_text)
        quote = {}
        if quote_text:
            quote = {"text": quote_text.replace("</i>", "").strip(), "author": author}

        meanings.append(
            {
                "text": current_text.replace("</i>", "").strip(),
                "category": current_category,
                "quote": quote,
            }
        )
    return meanings


def transform_data(data):
    new_data = []
    for item in data:
        meanings = parse_meanings(item["anlami"])
        new_item = {
            "soz_id": item["soz_id"],
            "soz_text": item["sozum"],
            "meanings": meanings,
            "category": item["turu2"],
        }
        new_data.append(new_item)
    return new_data


file_path = "tdk-scrape/atasozleri.json"
if os.path.exists(file_path):
    # Read the data from ata.json
    with open(file_path, "r", encoding="utf-8") as file:
        raw_json = json.load(file)
        # Transform the data
        transformed_json = transform_data(raw_json)
        # Output the result to a new file
        with open("transformed_atasozleri.json", "w", encoding="utf-8") as file:
            json.dump(transformed_json, file, ensure_ascii=False, indent=3)
else:
    print("File not found!")
