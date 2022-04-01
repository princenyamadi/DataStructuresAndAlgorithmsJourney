

from enum import Enum


class SecurityDevice:
    def __init__(self, active):
        print("init for SecurityDevice")
        self.active = active

    def reset(self):
        print("Resetting...")
        self.active = True


class Sensor(SecurityDevice):
    def __init__(self, active, silent, distance):
        self.active = active
        self.silent = silent
        self.distance = distance


security_device = SecurityDevice(True)
print(security_device)

sensor = Sensor(True, False, 30)
print(sensor)
sensor.reset()
print(type(sensor))
print(isinstance(sensor, Sensor))


class Position:
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def log(self):
        print("Pan: {}, Tilt: {}, Zoom: {}".format(
            self.pan, self.tilt, self.zoom))


# p = Position(10, 11, 12)

# p.log()

class Camera:
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def log(self):
        print("Camera: {}".format(self.serial_number))
        self.position.log()
        print("Camera Type: {}".format(self.camera_type))

    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2


c = Camera(123, Position(10, 11, 12), Camera.CameraType.ptz)
c.log()

# inheritance
# polymorphism
# encapsulation
# abstraction
# abstraction is hiding the details
