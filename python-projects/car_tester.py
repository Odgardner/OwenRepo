from car_class import car

cars = []
with open("cars.txt") as file:
    for line in file:
        s_line = line.strip()
        tokens = s_line.split()
        cars.append(tokens)

car1 = car(*cars[0])
print(car1.drive())
print(car1.get_gas_tank())
print(car1)

car2 = car(*cars[1])
print(car2.get_odometer())
print(car2)


