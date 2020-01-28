from model.persistence import Persistence

from model.business.telemetry import Telemetry

# Business Layer


class Controller:
    def __init__(self):
        # Layer in the system
        self.persistence = Persistence()

        #
        self.telemetry = Telemetry()

        self.state = True

        pass

    def initialise(self):

        pass

    def execute(self):
        while self.state:
            self.telemetry.execution()
            pass

        pass

    def garbage(self):

        pass
