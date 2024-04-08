import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App">
      <Header title="Yapay Zeka Destekli Atasözleri ve Deyimler" />
      <SearchBox placeholder="karaktersiz olmak anlamına gelen deyimler..." buttonText="Deyimlerde Ara" />
      <SearchBox placeholder="yeni doğan çocuk ile ilgili atasözleri..." buttonText="Atasözlerinde Ara" />
      <FrequentSearches />
    </div>
  );
}

export default App;

function Header({title}){
  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
}

function SearchBox({ placeholder, buttonText }){
   return (
    <div className="search-box">
      <input type="text" placeholder={placeholder} />
      <button>{buttonText}</button>
    </div>
  );
}

function FrequentSearches(){
  return (
    <div className="frequent-searches">
      <p>Sık Arananlar</p>
      <span>...</span>
    </div>
  );
}