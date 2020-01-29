import subprocess
import time
import datetime
import os
import pathlib


def main():

    while True:
        result = subprocess.run(['sh', './hooks/processor_temperature.sh'], stdout=subprocess.PIPE)
        processor_temperature = result.stdout.decode('utf-8')

        result = subprocess.run(['sh', './hooks/graphic_temperature.sh'], stdout=subprocess.PIPE)
        graphic_temperature = result.stdout.decode('utf-8')

        out = None

        if pathlib.Path('text.log').is_file():
            print('log found')
            out = open('text.log', "a")

            out.write('processor, ' + str(processor_temperature) + ', ' + str(datetime.date.today()) + '\r\n')
            out.write('graphic processor, ' + str(graphic_temperature) + ', ' + str(datetime.date.today()) + '\r\n')

            out.close()
        else:
            print('log does not exist')
            out = open('text.log', "w+")
            out.write('type, value, registered \r\n')

            out.write('processor, ' + str(processor_temperature) + ', ' + str(datetime.date.today()) + '\r\n')
            out.write('graphic processor, ' + str(graphic_temperature) + ', ' + str(datetime.date.today()) + '\r\n')

            out.close()



        time.sleep(1)

    pass


if __name__ == '__main__':
    #
    main()