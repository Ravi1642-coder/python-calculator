# Creating a Python Calculator:
num_1=float(input("enter number 1 :"))
num_2=float(input("enter number 2 :"))
choice=input("Enter your choice of operation on num_1 and num_2 (+,-,*,/,//,%,**):")
if choice=="+":
    print("addition is :",num_1+num_2)
elif choice=="-":
    print("Substraction is :",num_1-num_2)
elif choice=="*":
    print("Multiplication is :",num_1*num_2)        
elif choice=="/":
    print("division is :",num_1/num_2)
elif choice=="//":
    print("Quotient is :",num_1//num_2)
elif choice=="%":
    print("remainder is :",num_1%num_2)
elif choice=="**":
    print(" power of num_1 to the num_2 is :",num_1**num_2)
else:
    print("invalid operation")    