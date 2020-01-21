from controller import Controller


class Application:
    def __init__(self):
        self.controller = Controller()
        pass

    def execute(self):
        self.controller.initialise()
        self.controller.execute()
        self.controller.garbage()

        pass


def main():
    app = Application()

    app.execute()


if __name__ == '__main__':
    main()