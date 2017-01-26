import random
from random import *


def count():

    list = [5, 8, 11, 17, 35]
    #list=[17,35]




    result=0
    x=0

    while x < len(list)-2:

        b=randint(1,20)
        c=randint(0,len(list)-1)

        result=result+b*list[c]



        print("%s * %s  " % ( list[c],b))

        list.pop(c)


    answer=int(input("Answer: \n"))




    if answer==result:
        print('Success')
    else:
        print('Fail')
        print(result)



def main():
    for i in range(0,10):
        count()


if __name__ == '__main__':
    main()