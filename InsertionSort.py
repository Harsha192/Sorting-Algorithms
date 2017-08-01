import random
import time

def insertionSort(array):
    length = len(array);
    start = time.clock();
    for i in range(1,length):
        val = array[i];
        position = i-1;
        while (position>=0 and array[position]>val):
            array[position+1] = array[position];
            position = position-1;

        array[position+1] = val;
    end = time.clock();
    print 'Execution Time :',(end-start);
    return array;


############# Test Cases ################

print '+++++++++ Test Cases for Insertion Sort +++++++++++\n'
array = [];
print 'Empty array :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [10];
print 'Array with 1 elements :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [2,1,0,10,25,15];
print 'Array with 6 elements :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [2,2,2,2,2];
print 'Array with all element same :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

print 'Rondom numbers Genarate'
array = [x for x in range(20)];
random.shuffle(array);
print 'Randomly genarated Array :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [0,-2,2,3,7,5];
print 'Array with negative numbers :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [0.5,-0.4,-1.5,2.9,1,6,5.5];
print 'Array with decimal numbers :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [1,3,5,6,7,8];
print 'Already sorted array :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [10,8,7,5,2,-1,-20];
print 'Descending order sorted array :',array;
array = insertionSort(array);
print 'Sorted Array :',array;
print '';

array = [12, 4, 17, 6, 15, 16, 21, 14, 2, 7, 0, 23, 3, 20, 11, 5, 22, 8, 13, 19, 9, 18, 1, 24, 10];
print 'Randomly Generated Array to feed :', array;
array = insertionSort(array);
print 'Sorted Array :',array;
