import random
import time

def bubbleSort(array):
    length = len(array);
    start = time.clock();
    for i in range(0,length):
        for j in range(1,length-i):
            if array[j-1]>array[j]:
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
    end = time.clock();
    print 'Execution time :',(end-start);
    return array;


############# Test Cases ################
print '++++++++++ Test Cases for Bubble Sort +++++++++++\n';
array = [];
print 'Empty array :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [10];
print 'Array with 1 elements :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [2,1,0,10,25,15];
print 'Array with 6 elements :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [2,2,2,2,2];
print 'Array with all element same :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

print 'Rondom numbers Genarate'
array = [x for x in range(20)];
random.shuffle(array);
print 'Randomly genarated Array :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [0,-2,2,3,7,5];
print 'Array with negative numbers :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [0.5,-0.4,-1.5,2.9,1,6,5.5];
print 'Array with decimal numbers :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [1,3,5,6,7,8];
print 'Already sorted array :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [10,8,7,5,2,-1,-20];
print 'Descending order sorted array :',array;
array = bubbleSort(array);
print 'Sorted Array :',array;
print '';

array = [12, 4, 17, 6, 15, 16, 21, 14, 2, 7, 0, 23, 3, 20, 11, 5, 22, 8, 13, 19, 9, 18, 1, 24, 10];
print 'Randomly Generated Array to feed :', array;
array = bubbleSort(array);
print 'Sorted Array :',array;

