# script to count times performing each exercise.
# Output is in exercise_counts.txt.

# file = open("data.txt", "r")
with open('full_data.txt', 'r') as file:
    data = file.readlines()

exercise_list = []
count_list = []
sets_list = [''] * 1000

onSets = False
index = -1

for line in data:
    # print(line, end='')
    if line[0].isalpha():
        #onSets = False
        if "(" in line:                             # remove paranthesis from lines
            line = line.split("(")[0]
        line = line.lower().capitalize()            # change all characters to lowercase
        if line in exercise_list:
            #onSets = True
            index = exercise_list.index(line)
            count_list[index] += 1
        else:
            exercise_list.append(line)
            index = len(exercise_list) - 1
            count_list.append(1)

    elif len(line.strip()) != 0:
        if "(" in line:                             # remove paranthesis from lines
            line = line.split("(")[0] + "\n"
        if "=======" in line:
            continue
        # sets_list[index] = sets_list[index] + line
        sets_list[index] += line.lower()


count = 0
for elem in exercise_list:
    elem = elem[0:len(elem)-1]
    # print(elem, end=' ()()()() ')
    # print(count_list[count])
    print("{:<60}{:>2.2f}".format(elem, int(count_list[count])))
    print(sets_list[count])
    count += 1

