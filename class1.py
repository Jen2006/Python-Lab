def get_location(city):
    loc=[("Newyork",(2.478,3.755)),("Paris",(1.390,2.489)),("Chicago",(4.235,0.123)),("Tokyo",(18.236,5.972))]

    for cit,coord in loc:
        if cit==city:
            return coord
        
if __name__=="__main__":
    city=input("Enter the city")
    coordinates=get_location(city)

    if coordinates:
        print(f"The {city} located in {coordinates}")
    else:
        print(f"The {city} is not located")    
