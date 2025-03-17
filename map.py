# lambda with in map
numbers = [11,22,33,44,55]
#n=int(input("Enter the n value"))
koii = list(map(lambda x: x **4, numbers))
print(koii)

#pow function
base=[2,17,7,4,32,34,69]
exp=[3,4,7,2,3,8,6]
power=tuple(map(lambda x,y: x**y,base,exp))
print(power)

#map with other function
kawai=["jen","Koi","ACTIVITY"]
lower=map(str.lower,kawai)
print(list(lower))

kawai=["jen","Koi","ACTIVITY"]
upper=map(str.upper,kawai)
print(list(upper))