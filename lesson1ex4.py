my_list_1 = [2, 5, 8, 2, 12, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

print(my_list_1)
print(my_list_2)

my_list_1 = [x for x in my_list_1 if x not in my_list_2]


print(my_list_1)
