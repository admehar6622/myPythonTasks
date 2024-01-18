#pyton dictionaries

my_dic = {'key1':'value1','key2':'value2','key3':'value4','key4':'value4','key5':'value5',}
print(my_dic['key2'])
print(my_dic)
print(my_dic.keys())
print(my_dic.values())


for key in my_dic.keys():
    print(my_dic[key])


    for i in range(9):
        if i == 5:
            break
        print(i)

    else:
        print("Loop successfully run")

    b = 1
    while b <= 9:
        if b == 5:
            break
        print(b)
        b = b + 1

