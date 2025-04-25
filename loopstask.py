1. l=[3,4,2,5,6,7,23,45,60]
#wap to get a list if number is odd sqare it and if it is even then cube it based on the above list
l=[3,4,2,5,6,7,23,45,60]
results=[]
for i in l:
    if i%2==0:
        results.append(i**3)
    else:
        results.append(i**2)
       
# print(results)
#2. WAp to get a dictionary based on a following list with key is the number xisting in list 
#  and value should be the frequency of that number)
l=[3,2,5,2,3,2,5,2]
results={}
for i in l:
    print(i)
    results[i]=results.get(i,0)+1
    print("srav",results.get(i,0)+1)
print(results)


