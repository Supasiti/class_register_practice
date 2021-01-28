from CarRegistry import CarRegistry
# from Car import Car

if __name__ == '__main__':
    car = CarRegistry.create_car('Holden')
    car.drive()