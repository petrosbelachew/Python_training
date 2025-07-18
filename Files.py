sum=0

with open('data/input.txt') as file:
    for line in file.readlines():
     sum += float(line.strip())
print(sum)