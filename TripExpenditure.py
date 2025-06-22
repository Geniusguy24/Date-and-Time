nights = int(input("How many nights are you going to stay at the hotel? "))
days = int(input("How many days will you rent a rental car? "))
city = input("Which City are you going to? ")
spending_money = int(input("How much money are you going to spend on other things? "))


def hotel_cost(z):

    return 140 * z

def travel_cost(y):

    if y == "Charlotte":

        return 183
    
    elif y == "Tampa":

        return 220
    
    elif y == "Pittsburgh":

        return 225
    
    elif y == "Los Angeles":

        return 475
    
    else:

        print("Do You even know how to type?")

def rental_car_cost(x):

    if days >= 7:

        return 40 * days - 50
    
    elif days >= 3:

        return 40 * days - 20
    
    else:

        return 40 * x

def total_cost(x, y, z):

    return hotel_cost(nights) + travel_cost(city) + rental_car_cost(days) + spending_money

print("Cost of Car Rental: ", rental_car_cost(days))

print("Cost of Plane Travel: ", travel_cost(city))

print("Cost of Hotel Rooms: ", hotel_cost(nights))

print("Total Cost of Trip: ", total_cost(days, city, nights))