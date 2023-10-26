class Temperature:
    def __init__(self, degree):
        if not isinstance(degree, (int, float)):
            raise TypeError("Degree must be a numeric value (int or float).")
        # Initialize the private attribute degree
        self.__degree = degree

    def get_celsius(self):
        # Getter method to return the temperature in Celsius
        return self.__degree

    
    def get_fahrenheit(self):
        fahrenheit = (self.__degree * 9/5) + 32
        return fahrenheit

# Example usage:
# temperature_instance = Temperature(25)
# celsius_temp = temperature_instance.get_celsius()
# print(f"Temperature in Celsius: {celsius_temp}")
