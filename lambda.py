#lambda function

#simple eg
power=lambda x:x**4
result=power(2)
print(result)

#multiple arguements
sum=lambda a,b:a+b
result=sum(4,5)
print(result)

#lambda with in a map function
num=[1,5,3,7,9]
square=map(lambda x:x**2,num)
print(tuple(square))

j=[2,678,32,15]
e=[3,64,89,42]
sum=map(lambda x,y:x+y,j,e)
print(list(sum))

#lambda within filter function
n=[2,567,24,732,44,23]
odd=filter(lambda x:x%2!=0,n)
print(set(odd))

#sorted function
name=["Jenisha","Dhaiwik","Lev","Dishanth","Dusya","Ceil"]
sort=sorted(name,key=lambda x:len(x))
print(tuple(sort))