with open('RDLsets.txt', 'r') as file:
    data = file.readlines()

for line in data:
    print(line.split("lbs")[0])