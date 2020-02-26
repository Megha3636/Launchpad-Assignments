list1 = list2 = list()
list1 = eval(input("Enter the List: "))
for i in range(len(list1)):
	counter = 0
	for j in range(i):
		if list1[i]==list1[j]:
			counter = 1
	if counter==1:
		continue
	else:
		list2.append(list1[i])
print(list2)