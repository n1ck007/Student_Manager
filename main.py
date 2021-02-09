#imports
import student

#inits
stu = student.Student()

#script
print('Welcome.\n',stu.firstname, stu.lastname)
print(stu.firstname, stu.lastname)



print('What would you like to do? \nA. View \nB. Add \nC. Edit')

x = input()
x = x.upper()

if x == 'A' or x == 'VIEW':
	print('list students')

elif x == 'B' or x =='ADD':
	print ('add students')

elif x == 'c' or x == 'EDIT':
	print('edit students')

else:
	print('invalid input')

input("press enter to close program")