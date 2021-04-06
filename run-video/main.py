from sys import stdin, stdout
import os, time

if __name__ == '__main__':
    folder = 'video-txt'
    total = 0
    fps = 0

    repeat = input('Repeat (y/n) ? ')
    if repeat != 'n' and repeat != 'y':
        raise Exception('Repeat need to be y or n')

    with open('../' + folder + '/' + str('info'), 'r') as file:
        total = int(file.readline())
        fps = float(file.read()[5:])

    x = 0
    sleep_time = 1/fps
    while x < int(total):
        with open('../' + folder + '/' + str(x), 'r') as f:
            stdout.write(f.read())
        time.sleep(sleep_time)
        os.system('cls' if os.name == 'nt' else 'clear')
        x += 1
        if repeat  == 'y' and x == total - 1:
            x = 0
