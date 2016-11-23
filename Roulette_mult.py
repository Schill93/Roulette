from random import *

list=[5,8,11,17,35]

for i in range (0,10):
    b=randint(1,10)
    c=randint(0,len(list)-1)

    a=int(input("%s * %s \n" % (b,list[c])))

    if a==0:
        break

    if a == b*list[c]:
        print('Success')
    else:
        print('Fail')
        print("Correct answer is %s" % (b*list[c]))

