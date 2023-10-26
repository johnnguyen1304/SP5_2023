import unittest
from temperature import Temperature

class TestTemperature(unittest.TestCase):
    def testGetCelsius(self):
        # Instantiate a Temperature object with a degree of 27
        temp = Temperature(27)
        
        # Check if getCelsius returns 27
        self.assertEqual(temp.get_celsius(), 27)

    def testZero(self):
        temp = Temperature(0)
        # This test checks if 0°C converts to 32°F
        self.assertEqual(temp.get_fahrenheit(), 32)

    def testHundred(self):
        temp = Temperature(100)
        # This test checks if 100°C converts to 212°F
        self.assertEqual(temp.get_fahrenheit(), 212)
    
    def testTypeError(self):
        with self.assertRaises(TypeError):
            # Try to create a Temperature object with inappropriate data types
            Temperature(True)
            Temperature("100")

if __name__ == '__main__':
    unittest.main()
