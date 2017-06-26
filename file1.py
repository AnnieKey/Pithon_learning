from __future__ import division

import random
import math
#створення масиву і обрахунки додатніх і від'ємних чисел + рівних нулю
def calculations():
    dod = 0
    vid = 0
    nul = 0
    for i in range(kst):
        k = int(random.randrange(min, max))
        myArray.append(k)
        if k > 0:
            dod += 1
        elif k < 0:
            vid += 1
        elif k == 0:
            nul += 1

    print("Array:")
    print(myArray)
    print("Greater than 0 is: ", dod)
    print("Less than 0 is: ", vid)
    print("Equal to 0: ", nul)
#обчислення суми елементів масивів
def suma(arr):
    sum=0
    for i in range(kst):
        sum+=arr[i]
    return sum
#обчислення середнього квадратичного відхилення
def deviation():
    sa=0 #середнє арифметичне
    deviation1=0 #відхилення
    deviation2=0 #квадрат відхилення
    saDeviation=0 #шукане с.к.в.

    sum=suma(myArray) #сума елементів основого масиву
    sa=sum/10 #обчислення середнього арнифметичного

    tmpArray1=[] #масив величин відхилення
    for i in range(kst):
        k=myArray[i]-sa
        tmpArray1.append(k)
    sum1=suma(tmpArray1)

    tmpArray2=[] #масив величин квадрату відхилення
    for i in range(kst):
        s=tmpArray1[i]*tmpArray1[i]
        tmpArray2.append(s)
    sum2=suma(tmpArray2)

    tmp=sum2/kst
    saDeviation=math.sqrt(tmp)
    print("Standart deviation is: ", round(saDeviation,3))

print("Task 1")
myArray = []
kst=10 #кількість елементів в масиві
min=-5000 #мінімальна межа
max=5000 #максимальна межа
calculations()
deviation()
