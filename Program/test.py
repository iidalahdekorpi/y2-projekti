import unittest
from io import StringIO
import os.path


from read_file_IO import ReadFile
from points import Points
from coordinates import Coordinates


class Test(unittest.TestCase):
    
    def setUp(self):
        self.plot = ReadFile()
        
    def test_coordinates_read(self):
        coordinates = self.plot.load_coordinates('esim.txt')
        self.assertEqual("1", coordinates.lines.get('esim')[0], "First x-coordinate not right!")
        self.assertEqual("1", coordinates.lines.get('esim')[1], "First y-coordinate not right!")
    
    def test_wrong_files(self):
        coordinates = self.plot.load_coordinates('esim2.txt')
        self.assertNotEqual("1", coordinates.lines.get('ei')[0], "Program reads wrong format lines!")

    def test_max_min(self):
        coordinates = self.plot.load_coordinates('esim.txt')
        self.assertEqual("6", coordinates.get_x_max(), "Max x-coordinate not right!")
        self.assertEqual("3", coordinates.get_y_max(), "Max y-coordinate not right!")
        self.assertEqual("0", coordinates.get_x_min(), "Min x-coordinate not right!")
        self.assertEqual("0", coordinates.get_x_min(), "Min y-coordinate not right!")   

    def test_range(self):
        coordinates = self.plot.load_coordinates('esim3.txt')
        self.assertEqual("5", coordinates.get_x_range(), "X Range not right!") 
        self.assertEqual("6", coordinates.get_y_range(), "Y Range not right!")    

