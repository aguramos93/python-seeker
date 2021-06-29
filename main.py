#!/usr/bin/python3
import sys, seeker, time

def main(mode_command, roll_command, pitch_command, yaw_command):
    global seeker
    seeker = seeker.Seeker()
    try:
        seeker.open_serial()
        start_time = time.time()
        roll_l, roll_h = seeker.calculate_angle(roll_command)
        pitch_l, pitch_h = seeker.calculate_angle(pitch_command)
        yaw_l, yaw_h = seeker.calculate_angle(yaw_command)
        command = seeker.calculate_command(mode_command, roll_l, roll_h, pitch_l, pitch_h, yaw_l, yaw_h)
        seeker.send_command(command)

    except KeyboardInterrupt:
        pass     

if __name__== '__main__':

    mode = sys.argv[1]
    roll = sys.argv[2]
    pitch = sys.argv[3]
    yaw = sys.argv[4]
    main(int(mode), int(roll), int(pitch), int(yaw))
