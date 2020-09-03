#deleting duplicate elements
def Remove(arr):
    final =[]
    for num in arr:
        if num not in final:
            final.append(num)
            
    return final
arr=[2,4,10,20,5,2,20,4]
print(arr)
newarr=Remove(arr)
for i in range(0,len(newarr)):
    print(newarr[i])
    
    OUTPUT:
    [2, 4, 10, 20, 5, 2, 20, 4]
2
4
10
20
5
