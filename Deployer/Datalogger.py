import subprocess
import time


def main():

    while True:
        result = subprocess.run(['sh', './hooks/processor_temperature.sh'], stdout=subprocess.PIPE)
        print('cpu: ' + result.stdout.decode('utf-8'))

        result = subprocess.run(['sh', './hooks/graphic_temperature.sh'], stdout=subprocess.PIPE)
        print('graphics : ' + result.stdout.decode('utf-8'))



        time.sleep(.500)

    pass


if __name__ == '__main__':
    #
    main()