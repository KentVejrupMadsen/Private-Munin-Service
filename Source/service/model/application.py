from model.controller import Controller


class Application:
    """ """

    def __init__(self):
        self.controller = Controller()
        pass

    def execute(self):
        self.controller.initialise()
        self.controller.execute()
        self.controller.garbage()

        pass

