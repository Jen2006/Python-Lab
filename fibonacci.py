def fibonacci():
    x=0
    y=1

    print(x)
    print(y)

    for i in range(2,10):
      temp=x+y
      x=y
      y=temp

      print(temp)

if __name__=="__main__":
   fibonacci()     