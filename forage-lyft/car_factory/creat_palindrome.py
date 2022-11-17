from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(SternmanEngine):
    def __init__(self, warning_light_on, last_service_date, tire_sensor_data):
        engine = SpindlerBattery(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.needs_service or self.battery.needs_service
    
