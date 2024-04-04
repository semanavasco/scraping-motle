import json
import requests
from bs4 import BeautifulSoup

alphabet = "abcdefghijklmnopqrstuvwxyz"

mots = []

for lettre in alphabet:
    page = requests.get(f"https://www.liste-de-mots.com/mots-nombre-lettre/5/{lettre}/")
    soup = BeautifulSoup(page.content, "html.parser")

    resultat = str(soup.find("p", class_="liste-mots").contents[0]).replace("\n", "").strip().split(",")

    mots.extend(resultat)

for mot in mots:
    if "-" in mot:
        mots.pop(mots.index(mot))
    else:
        mots[mots.index(mot)] = mot.strip()

with open("mots.json", "w") as outfile:
    outfile.write(json.dumps(mots))
