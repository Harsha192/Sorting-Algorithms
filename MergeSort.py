import random

def mergeSort(array):
    length = len(array);
    if (length<2):
        return array;

    mid = length/2;
    left = mergeSort(array[:mid]);
    right = mergeSort(array[mid:]);

    i,j,k = 0,0,0;
    while (len(left)>i) and (len(right)>j):
        if (left[i]>=right[j]):
            array[k] = right[j];
            j=j+1;
        else:
            array[k]=left[i];
            i=i+1;

        k=k+1;

    while len(right)>j:
        array[k]=right[j];
        j=j+1;
        k=k+1;

    while len(left)>i:
        array[k]=left[i];
        i=i+1;
        k=k+1;

    return array;


############## Test Cases ################

print '+++++++++ Test Cases for Merge Sort +++++++++++\n'
array = [];
print 'Empty array :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [10];
print 'Array with 1 elements :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [2,1,0,10,25,15];
print 'Array with 6 elements :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [2,2,2,2,2];
print 'Array with all element same :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

print 'Rondom numbers Genarate'
array = [x for x in range(20)];
random.shuffle(array);
print 'Randomly genarated Array :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [0,-2,2,3,7,5];
print 'Array with negative numbers :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [0.5,-0.4,-1.5,2.9,1,6,5.5];
print 'Array with decimal numbers :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [1,3,5,6,7,8];
print 'Already sorted array :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';

array = [10,8,7,5,2,-1,-20];
print 'Descending order sorted array :',array;
array = mergeSort(array);
print 'Sorted Array :',array;
print '';


