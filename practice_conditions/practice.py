"""
marks = int(input())

if 100 >= marks >= 90:
    print("grade : A")
else:
    if 90 > marks >= 80:
        print("grade : B")
    else:
        if 80 > marks >= 70:
            print("grade : C")
        else:
            if 70 > marks:
                print("grade =D ")
            else:
                print("invalid marks")
                
print()

if 100 >= marks >= 90:
    print("grade : A")
elif 90 > marks >= 80:
    print("grade : b")
elif 70 > marks >= 60:
    print("grade : c")
elif  marks <= 60:
    print("grade : d")
else :
    print("invalid input")
    
############################################################################
num = int(input("enter a number :"))
if num%2 == 0:
    print("number is even")
else:
    print("number is odd")

#################################################################################

num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
num3 = int(input("enter a number : "))

if num1 > num2 and num1 > num3 :
    print("gretest number is:",num1)
elif num2 > num1 and num2 > num3 :
    print("gretest number is :",num2)
else :
    print("gretest number is :",num3) 
    


#####################################################################################

num = int(input("enter a number:"))

if (num % 7) == 0 :
    print("number is multiple of : 7")
else:
    print("number is not multiple of : 7")

"""    
#########################################################################################

ch = input("enter a character : ")
x = 'aeiou'
y = 'AEIOU'

if (ch == x[0::1] or  y[0::1]) :
    print("vowel",ch)
else:
    print('consolunt',ch)
