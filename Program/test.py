import unittest
from io import StringIO
import os.path


from read_file_IO import ReadFile
from points import Points
from coordinates import Coordinates


class Test(unittest.TestCase):
    
    def setUp(self):
        self.plot = ReadFile()
        
    def test_x_read(self):
        coordinates = self.plot.load_coordinates('esim.txt')
        self.assertEqual("1", coordinates.lines.get('esim')[0], "First coordinate not right")



