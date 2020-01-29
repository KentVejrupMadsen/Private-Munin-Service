import subprocess


class SystemProcess:
    def __init__(self):
        self.commands = ['', '' ]
        pass

    def execute(self):
        result = subprocess.run(self.commands, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))

        pass
