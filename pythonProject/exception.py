
def func1():
    try:
        l = [1,4,5,6,4,3,4]
        i = int(input("Input your number "))
        print(l[i])
        return 1
    except:
        print("There is some error accured")
        return 0
    finally:
        print("I always exucuted")


x = func1()
print(x)