def binary_search(sorted_array:list,searched_number:int)->int:
    low, high= 0 , len(sorted_array)-1
    while low<=high:
        mid= (low+high)//2
        if sorted_array[mid]==searched_number:
            return mid
        elif sorted_array[mid]<searched_number:
            low=mid+1
        else:
            high= mid-1
    return -1


array=[1,2,3,4,5,6,7,8,9]
value = 10
print(binary_search(array,value))