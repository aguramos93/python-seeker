#!/usr/bin/python3
import seeker
import argparse, time

def main(command):
    global seeker 
    seeker = seeker.Seeker()
    try:
        seeker.open_serial()
        start_time = time.time()
        seeker.send_command(command)
        seeker.read_serial()

    except KeyboardInterrupt:
        pass

    except ValueError as e:
        print(e)
    finally:
        seeker.close_serial() 

if __name__== '__main__':
    parser = argparse.ArgumentParser(description = 'This is a script to manage Seeker through serial communication', formatter_class = argparse.RawTextHelpFormatter)
    parser._positionals.title = "Available commands"
    parser.add_argument('command', nargs = '?', 
        choices = ('motor-on', 'motor-off', 
        'return-head', 'center-yaw', 'look-down', 
        'yaw-45'),
        default = 'center-yaw')
    parser.add_argument('--custom', '-c', dest = 'custom_mode', nargs = 1, action = "store", help = "Send custom hex commamd", type=str)
    args = parser.parse_args()

    order = args.command

    if args.custom_mode:
        order = [int((args.custom_mode[0]),16)]

    main(order)
