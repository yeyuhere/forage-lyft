from battery.battery import Battery
from datetime import datetime
SERVICE_TIME = 4

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + SERVICE_TIME)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
