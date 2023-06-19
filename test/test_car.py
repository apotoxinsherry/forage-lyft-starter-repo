import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())


    def test_battery_should_not_be_serviced(self):

        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())


class TestNubinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())


    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def engine_should_be_serviced(self):

        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def engine_should_be_serviced(self):

        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())



class TestWiloughbyEngine(unittest.TestCase):
    def engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


    def engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
