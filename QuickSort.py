import random

def quickSort(array):
    begin = 0;
    end = len(array)-1;
    quickSortExtend(array,begin,end);


def quickSortExtend(array,begin,end):
    if(begin<end):
        value = partition(array,begin,end);
        quickSortExtend(array,value+1,end);
        quickSortExtend(array,begin,value-1);


def partition(array,begin,end):
    pivot = array[begin];
    right = end;
    left = begin+1;

    while (1):
        while (left<=right and array[left]<=pivot):
            left = left+1;

        while (right>=left and array[right]>=pivot):
            right = right-1;

        if (right<left):
            break;
        else:
            temp = array[right];
            array[right] = array[left];
            array[left] = temp;

    temp = array[right];
    array[right] = array[begin];
    array[begin] = temp;

    return right;



############# Test Cases ################

print '+++++++++ Test Cases for Quick Sort +++++++++++\n'
array = [];
print 'Empty array :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [10];
print 'Array with 1 elements :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [2,1,0,10,25,15];
print 'Array with 6 elements :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [2,2,2,2,2];
print 'Array with all element same :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

print 'Rondom numbers Genarate'
array = [x for x in range(20)];
random.shuffle(array);
print 'Randomly genarated Array :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [0,-2,2,3,7,5];
print 'Array with negative numbers :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [0.5,-0.4,-1.5,2.9,1,6,5.5];
print 'Array with decimal numbers :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [1,3,5,6,7,8];
print 'Already sorted array :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

array = [10,8,7,5,2,-1,-20];
print 'Descending order sorted array :',array;
quickSort(array);
print 'Sorted Array :',array;
print '';

