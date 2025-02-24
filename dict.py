person={"Name":"Jenisha","Age":18,"City":"Manglore","Hobbies":["sleeping","eating","yapping"]}
print(person)

print(person["Name"])

person["Age"]=19
print(person)

person['Age']=12
print(person)
person["Name"]="Dhaiwik"
print(person)

for values in person.values():
 print(values) 


del person["Hobbies"]
print(person)
