import data
import numpy, cv2
from io import StringIO

class Frame:

    def __init__(self, width, height, frame, threshold, negative):
        self.width = width - (width % 2)
        self.height = height - (height % 4)
        self.frame = frame
        self.threshold = threshold
        self.negative = negative

    def matrix_to_ascii(self, matrix):
        ascii_value = 0
        for i in range(2):
            for j in range(4):
                if self.negative:
                    if matrix[i][j] > self.threshold:
                        ascii_value += 2 ** ((i//2) + (j*2))
                else:
                    if matrix[i][j] < self.threshold:
                        ascii_value += 2 ** ((i//2) + (j*2))

        return chr(data.brailleData[ascii_value])

    def frame_to_ascii(self):
        grayscale_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        line_index = 0
        column_index = 0
        ascii_frame = StringIO()

        while column_index < self.height:
            while line_index < self.width:
                matrix = numpy.zeros((2, 4))
                for i in range(2):
                    for j in range(4):
                        matrix[i][j] = grayscale_frame[column_index + j][line_index + i]
                ascii_frame.write(self.matrix_to_ascii(matrix))
                line_index += 2
            ascii_frame.write("\n")
            line_index = 0
            column_index += 4

        return ascii_frame.getvalue()
