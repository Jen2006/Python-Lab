
balance = 5000

choice=input("Enter 'D for deposit and 'W' for withdrawal")
amt=int(input("Enter the amount"))

if choice not in ['D','W']:
    print("Enter 'D' for deposit and 'W' for withdrawal")
elif choice=='D':
   balance += amt
elif choice=='W' and amt>balance:
    print("INsufficient balance")
else:
    balance-=amt

print("The updated amount",{balance})    