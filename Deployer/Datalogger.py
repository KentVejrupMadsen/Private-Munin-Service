import subprocess
import time


def main():

    while True:
        result = subprocess.run(['sh', './hooks/processor_temperature'], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))

        result = subprocess.run(['sh', './hooks/graphic_temperature'], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))



        time.sleep(.500)

    pass


if __name__ == '__main__':
    #
    main()