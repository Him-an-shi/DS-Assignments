'''In an e-commerce system, customer account IDs are stored in a list, and you are tasked with writing a program that implements the following:
• Linear Search: Check if a particular customer account ID exists in the list.
• Binary Search: Implement Binary search to find if a customer account ID exists, improving the search efficiency over the basic linear search 
'''
def liner_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return f"{key} found at index {i}"
    return f"{key} not found"

def rec_binary_search(arr,low,high,key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"{key} found at index {mid}"
        elif arr[mid] > key:
            return rec_binary_search(arr, low, mid - 1, key)
        else:
            return rec_binary_search(arr, mid + 1, high, key)
    return f"{key} not found"

def binary_search(arr,key):
    low,high=0,len(arr)-1
    while low<high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"{key} found at index {mid}"
        elif arr[mid] > key:
            high= mid - 1
        else:
            low= mid + 1
    return f"{key} not found"
    return

arr=[1,2,3,4,5,6,7,8,9,11]
key=int(input())
print(liner_search(arr,key))
print(rec_binary_search(arr,0,len(arr)-1,key))
print(binary_search(arr,key))