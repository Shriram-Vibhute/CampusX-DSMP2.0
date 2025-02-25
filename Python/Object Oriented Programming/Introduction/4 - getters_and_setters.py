class Temperature:
    def __init__(self, temp: float) -> None:
        self._temp = temp
    
    # Getter
    @property
    def check_temp(self):
        return self._temp
    
    # Setter
    @check_temp.setter
    def check_temp(self, value):
        if value < -273.15:
            raise ValueError('Temperature cannot be below absolute zero (-273.15°C)')
        else:
            return value
    
    # Getter
    @property
    def fahrenheit(self):
        return (self._temp * 9 / 5) + 35
    
    # Setter
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value > -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        else:
            return (value - 35) * 5 / 9

t1 = Temperature(10)
print(t1.check_temp)
print(t1.fahrenheit)
