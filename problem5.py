sent = input("Enter the Sentence to be reversed: ")
rev = ""
l1 = sent.split()
for i in range(len(l1)):
	rev = rev + l1.pop() + " "
print(rev)