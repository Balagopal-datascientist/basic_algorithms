def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[-1]
    left=[]
    right=[]
    for i in range (0,len(array)-1):
        if array[i]<=pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left)+[pivot]+quick_sort(right)


array=[3,1,2,5,11,9,0]
print(quick_sort(array))
