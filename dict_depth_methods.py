# Access keys, values and items
my_dict = {
    'id': 101,
    'name': 'Shreeharsh',
    'age': 20
}
print("Full dictionary:", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items as list of tuples:", my_dict.items())

print("\nChecking presence of key in dictionary")
test_dict = {'a': 10, 'b': 20, 'c': 30}
chk_key = input('Enter key name to check existence: ')
if chk_key in test_dict:
    print('Key {} exists with value {}'.format(chk_key, test_dict[chk_key]))
else:
    print('Key does not exist in dictionary.')

print("\nAccept number of players, create dict with names and runs")
n_players = int(input('Enter number of players: '))
players_dict = {}
for i in range(n_players):
    name = input('Enter player name: ')
    runs = int(input('Enter runs: '))
    players_dict[name] = runs

print("\nIterating dictionary to print player data")
print('{:<15} {:<10}'.format('PLAYER', 'RUNS'))
for key, val in players_dict.items():
    print('{:<15} {:<10}'.format(key, val))

target_p = input('\nEnter specific player name to find runs: ')
run_find = players_dict.get(target_p, -1)
if run_find != -1:
    print('{} runs: {}'.format(target_p, run_find))
else:
    print('Player not found.')

print("\nFind letter occurrences in a string using dict")
str_in = input('Enter a target string for analytics: ')
freq_dict = {}
for char in str_in:
    if char != ' ':
        freq_dict[char] = freq_dict.get(char, 0) + 1
print("Frequency list:")
for k, v in freq_dict.items():
    print('{}: {}'.format(k, v))

print("\nSum of all values in a numerical dictionary")
cost_dict = {'books': 500, 'pen': 20, 'bag': 1000}
val_sum = sum(cost_dict.values())
print('Total cost sum:', val_sum)

print("\nCombining parallel lists into dictionary items")
countries = ["India", "USA", "Germany", "France"]
cities = ["New Delhi", "Washington", "Berlin", "Paris"]
zip_dict = dict(zip(countries, cities))
print('Resulting dict from zip function:')
print(zip_dict)
