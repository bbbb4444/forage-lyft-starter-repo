from datetime import datetime
from car.car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
capulet_engine = CapuletEngine(current_mileage=45000, last_service_mileage=30000)
battery = SpindlerBattery(last_service_date=datetime.today().date())
car = Car(datetime.today().date(), engine=capulet_engine, battery=battery)

print(car.needs_service())
