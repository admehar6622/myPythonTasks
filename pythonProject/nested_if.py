num = int(input("Enter the number "))
if(num < 0):
    print("Number is negetive")
elif (num > 0):
    if(num <= 10):
        print("Number is between 0-10")
    elif(num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater then 20")
else:
    print("Number is zero.")

print("Thank you for submitting your number")