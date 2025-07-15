
word=input("Type a word: ")

vowels=['A', 'E' ,'I', 'O', 'U']
counter=0
for vowels in word:
    counter +=1
print(f'There are {counter} vowels in "{word}" ')