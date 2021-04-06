from Frame import Frame
import data, strings
import cv2, os, numpy

def calculate_boundary(frame):
    total = [0, 0, 0]
    for row in frame:
        for pixel in row:
            for RGB in range(3):
                total[RGB] += pixel[RGB]

    for RGB in range(3):
        total[RGB] = total[RGB] // (len(frame)* len(frame[0]))
    average = (total[0] + total[1] + total[2]) // 3

    return average

def open_video(name):
    try:
        video = cv2.VideoCapture(name)
    except:
        print('Error: Open video')
    return video

def create_folder(name):
    try:
        if not os.path.exists(name):
            os.makedirs('../' + name)
    except OSError:
        print('Error: Create video directory')

def set_default(string, default_value):
    if string == '':
        return default_value
    else:
        return string

def resize_image(image, width, height, new_width):
    ratio = height / width
    new_height = int(new_width * ratio)
    image = cv2.resize(image,(new_width, new_height))
    return image, new_width, new_height

def receive_int(integer, exception1, exception2, limit=9999):
    if not integer.isnumeric():
        raise Exception(exception1)
    integer = int(integer)
    if integer < 0 or integer > limit:
        raise Exception(exception2)
    return integer

if __name__ == '__main__':
    folder = 'video-txt'
    create_folder(folder)

    path = input(strings.choose1)
    video = open_video(path)

    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv2.CAP_PROP_FPS)
    print('The video have', fps, 'fps')

    new_image_width = set_default(input(strings.choose2), '300')
    new_image_width = receive_int(new_image_width, strings.exception6, strings.exception7)

    relative = set_default(input(strings.choose3), 'y')
    if relative != 'y' and relative != 'n':
        raise Exception(strings.exception7)

    boundary = 0
    if relative == 'n':
        boundary = set_default(input(strings.boundary1), '128')
        boundary = receive_int(boundary, strings.exception1, strings.exception2, 255)

    skip_frames = set_default(input(strings.fps), '0')
    skip_frames = receive_int(skip_frames, strings.exception3, strings.exception4)

    boundaryhl = set_default(input(strings.boundary2), 'h')
    if boundaryhl != 'h' and boundaryhl != 'l':
        raise Exception(strings.exception5)

    frameIndex = 0
    while(video.isOpened()):
        ret, frame = video.read()

        if not ret:
            break

        for x in range(skip_frames):
            video.read()

        frame, width, height = resize_image(frame, width, height, new_image_width)

        if relative == 'y':
            boundary = calculate_boundary(frame)

        frameClass = Frame(width, height, frame, boundary, boundaryhl)

        with open('../' + folder + '/' + str(frameIndex), 'w') as file:
            file.write(frameClass.frame_to_ascii())

        if frameIndex % 100 == 0:
            print("Frames done:", frameIndex)
        frameIndex += 1

    print("Frames done:", frameIndex)

    with open('../' + folder + '/' + str('info'), 'w') as file:
        file.write(str(frameIndex) + '\n')
        file.write('FPS: ' + str(fps))

    print('Video info created')

    print('Video was sucessful converted')
    exit(0)
