email_set=set()
def add_email(email):
    if email in email_set:
        print("Email already exists")
    else:
        email_set.add(email)
        print("Successfully Registered")

if __name__=="__main__":
    n=int(input("Enter the number of people to be registsered"))
    for i in range (n):
       
      email=input("Enter your email id")

      add_email(email)        