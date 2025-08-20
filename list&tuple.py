#wap to get input of 3 movies and make them a list
 movie1= input("movie1:",)
movie2= input("movie2:",)
movie3= input("movie3:",)
movie=[]
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)
print (movie)
#2nd method
movies=[]
movies.append(input("movie1:"))
movies.append(input("movie2:"))
movies.append(input("movie3:"))
print(movies)
#wap to check if a list contains palindrom of elements
list=[1,2,3,4,1](own method works for simple list which we know the count)
if list[0]==list[-1] and list[1]==list[-2]:
    print("list is a palindrom")
else:
    print('list is not a palindrom')
#another method main method
list=[1,2,3,5,3,3,1]
list2=list.copy()
list2.reverse()
print(list2)
if list==list2:
    print('list is a palindrom')
else :
    print('list is not palindrom')
#tuples
#WAP to count the number of students with "A" grade in the following tuple
tuple=("a","a","b",'c',"d","a",'b')
print(tuple.count('a'))
list=list(tuple)
print (list)    
list.sort()
print(list)
list=[1,2,3,4]
print(list)
tuple=tuple(list)
print (tuple)
