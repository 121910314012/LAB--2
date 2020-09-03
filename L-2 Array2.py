# COPY THE CONTENTS FROM ONE ARRAY TO ANOTHER ARRAY
#Intialize the array
ar1=input(" enter the content :")
# Another array ar2 wiht same size of ar1
ar2=[None]*len(ar1)
length=len(ar1)
#Copy elements from one array to another
for i in range(0,length):
    ar2[i]=ar1[length-i-1]
 #Display elements of ar1
print("elements in original array : ")
print(ar1)
print()
#Display elements of aar2
print("elements in new array : ")
for i in range(0,len(ar2)):
    print(ar2[i])
    
    OUTPUT:
    enter the content :1 2 3 4 5
elements in original array : 
1 2 3 4 5

elements in new array : 
5
 
4
 
3
 
2
 
1
