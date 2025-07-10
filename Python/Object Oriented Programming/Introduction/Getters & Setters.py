# @property decorator is used to mention the getter and @getter_name.setter decorator is used to mention the setter
class Temperature:
    def __init__(self, temp: float) -> None:
        self._temp = temp
    
    # Getter for Celsius
    @property
    def celsius(self): # Getter method returns the present value
        return self._temp
    
    # Setter for Celsius
    @celsius.setter
    def celsius(self, value): # Setter method assigns to new value and does not return anything
        if value < -273.15:
            raise ValueError('Temperature cannot be below absolute zero (-273.15°C)')
        self._temp = value  # Actually assign the value
    
    # Getter for Fahrenheit
    @property
    def fahrenheit(self):
        return (self._temp * 9 / 5) + 32  # Fixed conversion formula
    
    # Setter for Fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:  # Fixed condition (< not >)
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        self._temp = (value - 32) * 5 / 9  # Convert and assign to internal storage

# Example usage
t1 = Temperature(10)
print(f"Celsius: {t1.celsius}")      # 10
print(f"Fahrenheit: {t1.fahrenheit}") # 50.0

'''
Observations:
    - You dont need to call getter and setter explicitely, by just calling obj.getter you only call obj.getter inorder to call them both at a time.
    - The calling is different - we dont need to mention () and instead of passing the argument into the method, we need to assign the new value of temperature(varable) to it.
'''

# Using setters
t1.celsius = 25
print(f"After setting celsius to 25:")
print(f"Celsius: {t1.celsius}")      # 25
print(f"Fahrenheit: {t1.fahrenheit}") # 77.0

t1.fahrenheit = 100
print(f"After setting fahrenheit to 100:")
print(f"Celsius: {t1.celsius}")      # 37.77777777777778
print(f"Fahrenheit: {t1.fahrenheit}") # 100.0

# Testing validation - Conditional getter and setter
try:
    t1.celsius = -300  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")