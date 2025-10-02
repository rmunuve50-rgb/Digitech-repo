my_list =[1,2,3,4,]
print(my_list) 

my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
print(my_list)

my_list.insert(2,9)
print(my_list)

phil =my_list.copy()

my_list.remove(9)
print(my_list)

popping =my_list.pop()
print(my_list, "removed element is :", popping)

my_list.index(3)
print(my_list.index(3))

counting = my_list.count(4)
print(counting)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)  

length= len(my_list)
print(length)


maximum = max(my_list)
print(maximum)

minimum = min(my_list)
print(minimum)

checking = 5 in my_list
print(checking)

checking = 3 not in my_list
print(checking)

print(phil)
 