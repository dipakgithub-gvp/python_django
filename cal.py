#simple calculator

def sum(no1,no2):
	return(no1+no2)
def sub(no1,no2):
	return(no1-no2)
def mul(no1,no2):
	return(no1*no2)
def div(no1,no2):
	return(no1/no2)
		
print("select operator\n""1.add\n""2.sub\n""3.mul\n""4.div\n")
select = input("Select operations form 1, 2, 3, 4 :") 
number1=int(input("enter your first number:"))
number2=int(input("enter second number"))

if select=='1':
	print(sum(number1,number2	))
elif select=='2':
	print(sub(number1,number2))
elif select=='3':
	print(mul(number1,number2))
elif select=='4':
	print(div(number1,number2))
else:
	print("invalid argument")
	