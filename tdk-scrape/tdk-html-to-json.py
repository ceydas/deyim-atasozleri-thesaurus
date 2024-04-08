import pandas as pd
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import csv
import json

# Load the JSON file
with open('/Users/ceydog/Desktop/github_repos/deyim-atasozleri-thesaurus/tdk-scrape/atasozleri.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
 

set_of_i_tags = set()
contains_i_tag_pattern = r"</i>|\S+<\/i>\S*|</i>\S+"
quoted_i_pattern = r"-</i>\S*"
abbrev_i_tag_pattern = r""

# Remove 'i tags' from 'anlami' attribute in each object
for obj in data:
    if 'anlami' in obj and '</i>' in obj['anlami']:
        # Find all occurrences of the pattern
        matches = re.findall(pattern, obj['anlami'])
        for match in matches:
            set_of_i_tags.add(match)

print(set_of_i_tags)

'''
# Save the modified data back to a new JSON file
with open('/Users/ceydog/Desktop/github_repos/deyim-atasozleri-thesaurus/tdk-scrape/atasozleri_test_out.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=3)

print("Attributes removed and new file saved.")
'''

def remove_attributes():
    # Remove 'gosterim_tarihi' and 'atara' attributes from each object
    for obj in data:
        if 'gosterim_tarihi' in obj:
            del obj['gosterim_tarihi']
        if 'atara' in obj:
            del obj['atara']
        if 'anahtar' in obj:
            del obj['anahtar']
