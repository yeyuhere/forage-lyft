from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(WilloughbyEngine):
    def __init__(self,  current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        super().__init__(engine, battery)
    def needs_service(self):
        return self.engine.needs_service or self.battery.needs_service
