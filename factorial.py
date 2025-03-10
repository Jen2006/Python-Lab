def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    print(result)

if __name__=="__main__":
    n=int(input("Enter the numbe you want to get the factorial of:"))
    factorial(n)