#Creating List using FOR LOOP:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_num = n + 1
    new_list.append(new_num)
print(new_list) #prints: [2, 3, 4]

#..............OR.......................................

#Creating List using LIST COMPREHENSION:
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list) #prints: [2, 3, 4]
#........................................................

#EXAMPLE 2:
name = "Kotha"
neww_list = [letter for letter in name]
print(neww_list) #prints: ['K', 'o', 't', 'h', 'a']
#.........................................................
#EXAMPLE 3:
new_list = [n * 2 for n in range(1, 5)]
print(new_list) #prints: [2, 4, 6, 8]

#......................................................................................................

#CONDITIONAL LIST COMPREHENSION
#EXAMPLE 4: Make a new list that adds 1 to each item if item is > 2
numberss = [1, 2, 3, 4, 5, 6]
newww_list = [n + 1 for n in numberss if n > 2]
print(newww_list) #prints: [4, 5, 6, 7]
#.....................................................

#EXAMPLE 5: prints name if it has less that 5 alophabets
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 5]
long_names = [name.upper() for name in names if len(name) >= 5]

print(short_names) #prints: ['Alex', 'Beth', 'Dave']
print(long_names) #prints: ['CAROLINE', 'ELEANOR', 'FREDDIE']
#......................................................................................................






