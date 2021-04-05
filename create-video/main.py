from Frame import Frame
import data, strings
import cv2, os, numpy

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

def recieve_int(integer, exception1, exception2, limit=9999):
    if not integer.isnumeric():
        raise Exception(exception1)
    integer = int(integer)
    if integer < 0 or integer > limit:
        raise Exception(exception2)
    return integer

if __name__ == '__main__':
    folder = 'video-txt'
    create_folder(folder)

    video = open_video(input(strings.choose1))

    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = video.get(cv2.CAP_PROP_FPS)
    print('The video has', fps, 'fps')

    new_image_width = set_default(input(strings.choose2), '300')
    new_image_width = recieve_int(new_image_width, strings.exception6, strings.exception7)

    boundary = set_default(input(strings.boundary1), '128')
    boundary = recieve_int(boundary, strings.exception1, strings.exception2, 255)


    skip_frames = set_default(input(strings.fps), '0')
    skip_frames = recieve_int(skip_frames, strings.exception3, strings.exception4)

    boundaryhl = set_default(input(strings.boundary2), 'h')
    if boundaryhl != 'h' and boundaryhl != 'l':
        raise Exception(strings.exception5)

    with open('../' + folder + '/' + str('info'), 'w') as file:
        file.write(str(fps))

    print('Video info created')

    frameIndex = 0
    while(video.isOpened()):
        ret, frame = video.read()
        
        if not ret:
            break

        for x in range(skip_frames):
            video.read()

        frame, width, height = resize_image(frame, width, height, new_image_width)

        frameClass = Frame(width, height, fps, frame, boundary, boundaryhl)

        with open('../' + folder + '/' + str(frameIndex), 'w') as file:
            file.write(frameClass.frame_to_ascii())

        print("Frames done:", frameIndex)
        frameIndex += 1

    print('Video was sucessful converted')
    exit(0)
