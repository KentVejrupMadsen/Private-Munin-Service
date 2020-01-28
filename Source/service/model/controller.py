from model.persistence import Persistence

from model.business.telemetry import Telemetry

# Business Layer


class Controller:
    def __init__(self):
        # Layer in the system
        self.persistence = Persistence()

        #
        self.telemetry = Telemetry()

        pass

    def initialise(self):

        pass

    def execute(self):

        pass

    def garbage(self):

        pass
