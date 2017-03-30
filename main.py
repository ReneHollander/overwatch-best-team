from input import readowcsv

heroes, players = readowcsv('Overwatch Cup - Hero Preferences.csv')

for hero in heroes:
    print(hero)

print()

for player in players:
    print(player)