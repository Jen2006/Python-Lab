due_days = int(input("Enter number of days late: ")) 
i=15

if due_days < 0: 
   print("Days late cannot be negative!") 
   fine = 0  # Assign a default value to avoid NameError 
elif due_days <= 5: 
     fine = due_days * i
elif due_days <= 10: 
    fine = due_days * i 
else: 
    fine = due_days * i

print("Total fine is:", fine) 