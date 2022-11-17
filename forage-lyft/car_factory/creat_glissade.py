from datetime import datetime
from car import Car

from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(Car):
    def __init__(self,current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.needs_service or self.battery.needs_service
            
