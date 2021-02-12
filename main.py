#imports
import csv
import student

#defines
studentarchive = []

#functions
def add_student():
	#requests info from the user
	print('Please enter the new students information.')
	firstname = input('First Name: ').capitalize()
	lastname = input('Last Name: ').capitalize()
	instrument = input('Instrument: ').capitalize()
	age = input('Age: ').capitalize()
	tuition = input('tuition: $').capitalize()
	tuition = f'${tuition}'

	#creates student obj with inputs 
	newstudent = student.Student(firstname, lastname, instrument, age, tuition)
	print(newstudent.firstname, newstudent.lastname, newstudent.instrument, newstudent.age, newstudent.tuition)

	#saves student's properties to a csv file
	with open('student_info.txt', 'a') as student_info:
		stuwriter = csv.writer(student_info, delimiter = ',')
		stuwriter.writerow([newstudent.firstname, newstudent.lastname, newstudent.instrument, newstudent.age, newstudent.tuition])




#script
print('Welcome.')
continueloop = True
while continueloop == True:
	#this if tree returns an UPPERCASE string
	#strings used in comparisons must be UPPERCASE
	print('What would you like to do?\n(V) View\n(A) Add\n(E) Edit\n(X) Exit')
	userinput = input()
	userinput = userinput.upper() 
	if userinput == 'V' or userinput == 'VIEW':
		userinput = 'VIEW'
		continueloop = True		

	elif userinput == 'A' or userinput =='ADD':
		userinput = 'ADD'
		add_student()
		continueloop = True

	elif userinput == 'E' or userinput == 'EDIT':
		userinput = 'EDIT'
		continueloop = True

	elif userinput == 'X' or userinput == 'EXIT':
		userinput = 'EXIT'
		continueloop = False

	else:
		userinput = 'INVALID'
		continueloop = True

	pass
	