from tyre.tyre import Tyre

class CarriganTyre(Tyre):

    def __init__(self, tyre_usage):
        self.tyre_usage = tyre_usage

    def needs_service(self):
        return sum(self.tyre_usage)>3
    