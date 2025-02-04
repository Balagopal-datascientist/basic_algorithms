def bubble_sort(array:list)-> list:
    swapped=False
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
        if not swapped:
            break

    return array
array=[3,1,2,5,11,9,0]
print(bubble_sort(array))