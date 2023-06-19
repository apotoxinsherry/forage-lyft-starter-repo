from battery.battery import Battery
from datetime import date



class NubbinBattery(Battery):

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        difference = self.current_date.year - self.last_service_date.year

        if self.current_date.month < self.last_service_date.month or (self.current_date.month == self.last_service_date.month and self.current_date.day < self.last_service_date.day):
            difference -= 1
        
        return difference>4
