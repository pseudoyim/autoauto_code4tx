import car
import serial
import serial.tools.list_ports
import time

port_to_use = None
for port in serial.tools.list_ports.comports():
    if 'uno' in port.description.lower():
        port_to_use = port
        break

ser = serial.Serial(port.device, 9600)

total_seconds = 2.8

print ser.readline()

def forward(secs=total_seconds):
    ser.write('1000\n')
    # print 'forward'
    time.sleep(secs)
    ser.write('0000\n')

def reverse(secs=total_seconds):
    ser.write('0100\n')
    # print 'reverse'
    time.sleep(secs)
    ser.write('0000\n')

# def left():
#     ser.write('0010\n')
#     # print 'left'
#     time.sleep(total_seconds)
#     ser.write('0000\n')

# def right():
#     ser.write('0001\n')
#     # print 'right'
#     time.sleep(total_seconds)
#     ser.write('0000\n')

def left(secs=total_seconds):
    ser.write('1010\n')
    # print 'forward_left'
    time.sleep(secs)
    ser.write('0000\n')

def right(secs=total_seconds):
    ser.write('1001\n')
    # print 'forward_right'
    time.sleep(secs)
    ser.write('0000\n')

def reverse_left(secs=total_seconds):
    ser.write('0110\n')
    # print 'reverse_left'
    time.sleep(secs)
    ser.write('0000\n')

def reverse_right(secs=total_seconds):
    ser.write('0101\n')
    # print 'reverse_right'
    time.sleep(secs)
    ser.write('0000\n')

def stop():
    ser.write('0000\n')

def set(forward, reverse, left, right):
    forward = 1 if forward else 0
    reverse = 1 if reverse else 0
    left = 1 if left else 0
    right = 1 if right else 0
    ser.write("{}{}{}{}\n".format(forward, reverse, left, right))

def pause():
    # print 'pausing...'
    time.sleep(total_seconds)
