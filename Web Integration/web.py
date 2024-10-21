from flask import Flask, render_template, Response
# import cv2
import csv
# import time
from StepperLib import Stepper 
import pyfirmata2 as pyfirmata

app = Flask(__name__, template_folder='/home/rtc/Desktop/rover-sensor-integration/rover-sensor-integration/templates')

# Function to read sensor data from csv file
def read_sensor_data():
    with open('sensor_data.csv', 'r') as file:
        data = list(csv.reader(file))
    # assuming the last ine contains the latest sensor data
        latest_data = data[-1]
        return latest_data
    
# Function to capture video from webcam
# def get_frame():
#     camera = cv2.VideoCapture(0)

#     desired_fps = 10
#     frame_time_interval = 1/desired_fps

#     last_frame_time = 0
#     while True:
#         current_time = time.time()
#         if current_time - last_frame_time >= frame_time_interval:
#             success, frame = camera.read()
#             if not success:
#                 break
#             else:
#                 ret, buffer = cv2.imencode('.jpg', frame)
#                 frame = buffer.tobytes()
#                 yield (b'--frame\r\n'
#                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#     camera.release() #what is this?

# Route for streaming video
# @app.route('/video_feed')
# def video_feed():
#     return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for displaying sensor data
# @app.route('/sensor_data')
# def sensor_data():
#     data = read_sensor_data()
#     return render_template('sensor_data.html', sensor_data=data)

# Default route
@app.route('/')
def index():
    return render_template('index.html')

def get_stepper_data(board):
    motor_1_configs = (22, 23, (1, 2, 3))
    motor_1 = Stepper(board, *motor_1_configs)

    return

if __name__ == '__main__':

    # board = pyfirmata.Arduino(pyfirmata.Arduino.AUTODETECT)
    # reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
    # reader.start()
    # print("Communication Successfully started")

    app.run(host='0.0.0.0', port=5000, debug=True)
    
    while True:
        get_stepper_data(board='')

