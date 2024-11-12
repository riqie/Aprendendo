class Vehicle:
    def __init__(self, speed=0 , degrees = 0, pilot_name = ""):
        self._speed = speed
        self._degrees = degrees
        self._pilot_name = pilot_name

    def verify_speed(self, speed):
        if speed >= 0:
            return True
        return False

    def verify_degrees(self, degrees):
        if 0 <= degrees <= 360:
            return True
        return False

    def set_speed(self, speed):
        if self.verify_speed(self, speed):
            self._speed= speed
        else:
            print("Speed must be greater than 0!")

    def set_degrees(self, degrees):
        if self.verify_degrees(self, degrees):
            self._degrees = degrees
        else:
            print("The car must be between 0 and 360 degrees!")

    def set_pilot(self, pilot):
        self._pilot_name = pilot

    def get_speed(self):
        return self._speed
    
    def get_degrees(self):
        return self._degrees
    
    def get_pilot_name(self):
        return self._pilot_name

    def get_infos(self):
        return f"Pilot: {self._pilot_name}\nSpeed: {self._speed}km/h\nDegrees: {self._degrees}"