import os, time

if __name__ == '__main__':
    folder = 'video-txt'
    for x in range (400):
        with open('../' + folder + '/' + str(x), 'r') as f:
            print(f.read())
        time.sleep(1/30)
        os.system('cls' if os.name == 'nt' else 'clear')
