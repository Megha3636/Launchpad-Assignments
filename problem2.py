list1 = list()
list2 = list()
list1 = eval(input("Enter the list elements"))
for i in range(len(list1)):
	if(list1[i]<5):
		list2.append(list1[i])
print(list2)