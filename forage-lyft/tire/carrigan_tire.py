from tire.tire import Tire

class CarriganTire:
    def __init__(self, tire_data) -> None:
        self.tire_data = tire_data
    
    def needs_service(self):
        for num in self.tire_data:
            if num >= 0.9:
                return True
        return False
