import random
from random import *
import time
import timeit



def count():





    list = [5, 8, 11, 17, 35]
    #list=[17,35]


    x=0
    result=0

    while x < (len(list)-2):


        b=randint(1,20)
        c=randint(0,len(list)-1)

        result=result+b*list[c]





        print("%s * %s  " % ( list[c],b))

        list.pop(c)


    answer=int(input("Answer: \n"))




    if answer==result:
        print('Success')
        correct=True

    else:
        print('Fail')
        correct=False



        print(result)

    return correct


def timer(start,end,nbr):

    time=end-start

    timePer=time/nbr

    print('Total time: ' )
    print(time-time%1)

    print('Time per answer: ')

    print(timePer-timePer%1)




def main():
    nbr=2
    correct = 0

    start=timeit.default_timer()



    for i in range(0,nbr):


        if count() == True:
            correct=correct+1




    end=timeit.default_timer()

    timer(start,end,nbr)



if __name__ == '__main__':
    main()