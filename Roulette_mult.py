from random import *

list=[5,8,11,17,35]

for i in range (0,20):
    b=randint(1,20)
    c=randint(0,len(list)-1)

    print(b*list[c])

    a=int(input("%s * %s \n" % (b,list[c])))


    if a == b*list[c]:
        print('Success')
    else:
        print('Fail')

