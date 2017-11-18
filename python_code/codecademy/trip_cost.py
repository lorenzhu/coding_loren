
# calculate the trip cost consists of four parts

def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    plane_dict = {"Charlotte": 183,
                  "Tampa": 220,
                  "Pittsburgh": 222,
                  "Los Angeles": 475}
    return plane_dict[city]


def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days

def trip_cost(city, days, spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money

print(trip_cost("Los Angeles", 5, 600))