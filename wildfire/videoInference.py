import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="path to input video file")
parser.add_argument("output_file", help="path to output video file")
args = parser.parse_args()

# open the input video file
cap = cv2.VideoCapture(args.input_file)
print(cap.isOpened())

# get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# create video writer for output file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args.output_file, fourcc, fps, (width, height), isColor=False)

# loop through video frames
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # convert frame to black and white
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # write the grayscale frame to output video
    out.write(gray)

    # display the frame
    #cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
       break

# release resources
cap.release()
out.release()
#cv2.destroyAllWindows()
