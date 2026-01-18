# Map, Reduce i Pipe funkcije

Vlastita implementacija map, reduce i pipe funkcija u imperativnom programskom jeziku

Ovaj projekt izrađen je u sklopu kolegija *Deklarativno programiranje. Cilj projekta je vlastita implementacija funkcija **map, **reduce* i *pipe* u Python te njihova primjena na stvarnom skupu podataka. Aplikacija dohvaća podatke o filmovima iz MongoDB baze podataka i omogućuje njihovu analizu putem jednostavnog web sučelja.

## Korištene tehnologije
•⁠  ⁠Python 3
•⁠  ⁠Flask
•⁠  ⁠MongoDB
•⁠  ⁠pymongo
•⁠  ⁠HTML
•⁠  ⁠CSS
•⁠  ⁠JavaScript

## Struktura projekta
⁠ text
.
├── app.py               
├── db.py
├── functional.py
├── analysis.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── app.js
    └── style.css
 ⁠

## Upute za pokretanje

### 1. Postavljanje virtualnog okruženja
Za početak je potrebno preuzeti repozitorij i kreirati virtualno okruženje:

python -m venv venv
source venv/bin/activate


### 2. Preuzimanje potrebnih paketa
Potrebno je preuzeti pakete pomoću kojih je napravljen projekt:

pip install -r requirements.txt


### 3. Pokretanje aplikacije
Aplikacija se pokreće naredbom ⁠ python app.py ⁠