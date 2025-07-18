answers = [
    'vanuatu',
    'vatican City',
    'venezuela',
    'vietnam'
]

guessed = []

tes = []
i = 0
while tes != 'q':
    guess = input(f'Enter answer for trial and q to end: ')
    guessed.append(guess)

 if tes==q:

for guess in guessed:

    i += 1
    print(f'ypu are left with {5 - i} trials')
    if i == 5:
        break

print(f'Test')
