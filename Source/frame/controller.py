from frame.persistence import Persistence

from frame.business.telemetry import Telemetry


class Controller:
    def __init__(self):
        self.persistence = Persistence()
        self.telemetry = Telemetry()

        pass

    def initialise(self):

        pass

    def execute(self):

        pass

    def garbage(self):

        pass
