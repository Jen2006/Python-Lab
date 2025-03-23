def ticket(a):
    if a<0:
        print("Enter valid age")
    elif a<5:
        cost=0
        print(f"The ticket price is {cost}$")
    elif a<18:
        cost=10
        print(f"The ticket price is {cost}$")  
    elif a>60:
        cost=50
        print(f"The ticket price is {cost}$")  
    else:
        cost=70
        print(f"The ticket price is {cost}$")


if __name__=="__main__":
    a=int(input("Enter the age"))      
    ticket(a)