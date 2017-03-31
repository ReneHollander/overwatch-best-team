import shutil
import urllib.request

from input import readowcsv

heroes, players = readowcsv('Overwatch Cup - Hero Preferences.csv', 1 / 4)

for hero in heroes:
    fn = hero.simplename()
    with urllib.request.urlopen("https://blzgdapipro-a.akamaihd.net/hero/" + fn + "/hero-select-portrait.png") as response, open("res/portraits/" + fn + ".png", 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
