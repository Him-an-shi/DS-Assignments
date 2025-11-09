'''
2. 
	In a company, employee salaries are stored in a list as floating-point numbers. Write a  program that sorts the employee salaries in ascending order using the following two algorithms:
• Selection Sort: Sort the salaries using the selection sort algorithm.
• Bubble Sort: Sort the salaries using the bubble sort algorithm.
Display array after every pass. display number of comparisons and number of swaps
3. 	In a company, employee salaries are stored in a list as floating-point numbers. Write a  program that sorts the employee salaries in ascending order using the following two algorithms:
• Insertion Sort: Sort the salaries using the insertion sort algorithm.
• Bubble Sort: Sort the salaries using the bubble sort algorithm.
Display array after every pass. display number of comparisons and number of swaps
4.	Write a Python/C++/Java program that sorts the students marks in ascending order using Quicksort. Test the program for example arrays demonstrating best case and worst-case time complexity.
'''
def bubble(arr):
    swap=False
    swaps=0
    comp=0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            comp+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
                swap=True
        if swap is False:
            break
    return arr, comp, swaps

def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

def selection(arr):
    for  i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

def quicksort(arr,low,high):
    if low<high:
        idx=partition(arr,low,high)
        quicksort(arr,low,idx-1)
        quicksort(arr,idx+1,high)
    return arr
def partition(arr,low,high):
    pvt=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pvt:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

arr=[3,45,5,6,8,58,1,4,778]
print(bubble(arr))
print(insertion(arr))
print(selection(arr))
print(quicksort(arr,0,len(arr)-1))