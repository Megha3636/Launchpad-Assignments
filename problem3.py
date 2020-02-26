list1 = list2 = list()
list1 = eval(input("Enter th elements of your list: "))
key = int(input("Enter the element to be searched: "))
for i in range(len(list1)):
	if(list1[i]==key):
		list2.append(i)
print(list2)