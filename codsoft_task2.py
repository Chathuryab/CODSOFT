#SIMPLE CALCULATOR WITHOUT GUI
#USER INPUTS 
num1=float(input("enter number 1:\n"))
num2=float(input("enter number 2:\n"))
#SELECTING OF OPERATOR
choice=input("choose operation:\n1.+\n2.-\n3.x\n4./\n")
#CONCEPTS OF ABSTRACTION
#FUN FOR ADD
def sum(n1,n2):
    return n1+n2
#FUNC FOR SUB
def diff(n1,n2):
    return n1-n2
#FUNC FOR MULTIPLY
def mul(n1,n2):
   return n1*n2
#FUNC FOR DIVISION
def div(n1,n2):
    try:
        return (n1/n2)            #IF NO ERROR
    except ZeroDivisionError:     #IF THERE IS NO ERROR
        print("divide by 0 error")
        return("PLEASE TRY AGAIN")
#SELECTION OF OPERATOR
if choice=='+':
    result=sum(num1,num2)         #CALLING OF FUNC
elif choice=='-':
    result=diff(num1,num2)
elif choice=='x':
    result=mul(num1,num2)
elif choice=='/':
    result=div(num1,num2)
print("result is:",result)        #PRINTING OF RESULT



