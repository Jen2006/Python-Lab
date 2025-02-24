#creating a list
cam=[1,2,3,"jen","nomu",True]
print(cam)

#accessing elements from the list
print(cam[1])
print(cam[-1])
print(cam[3])

#slicing a list
print(cam[1:4])
doc=cam[2:5]
print(doc)

#modifing a list
cam[2]="alice"
print(cam)

#adding elements into list
cam.append("naruto")
cam.insert(4,45)
cam.extend(["a","b","c"])
print(cam)

#removing an element
cam.remove("naruto")
#cam.pop(1)
del cam[3]
print(cam)

#iteration
for items in cam:
    print(items)

#reverse
cam.reverse()
print(cam) 