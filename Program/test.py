import unittest
from io import StringIO


from read_file_IO import ReadFile
from points import Points
from coordinates import Coordinates


class Test(unittest.TestCase):
    
    def setUp(self):
        self.plot = ReadFile()
        
    def test_coordinates_read(self):
        coordinates = self.plot.load_coordinates('Program/esim.txt')
        self.assertEqual(0, coordinates.lines.get('ohjelmointi').points[0].x, "First x-coordinate not right!")
        self.assertEqual(0, coordinates.lines.get('ohjelmointi').points[0].y, "First y-coordinate not right!")
        self.assertEqual(4, coordinates.lines.get('on').points[2].x, "Data not saved correctly!")


    def test_wrong_files(self):
        try:
            coordinates = self.plot.load_coordinates('Program/esim2.txt')
            self.assertNotEqual("1", coordinates.lines.get('ei')[0], "Program reads wrong format lines!")
        except ValueError:
            pass

    def test_max_min(self):
        coordinates = self.plot.load_coordinates('Program/esim.txt')
        self.assertEqual(6.0, coordinates.get_x_max(), "Max x-coordinate not right!")
        self.assertEqual(3.0, coordinates.get_y_max(), "Max y-coordinate not right!")
        self.assertEqual(0, coordinates.get_x_min(), "Min x-coordinate not right!")
        self.assertEqual(0, coordinates.get_x_min(), "Min y-coordinate not right!")   

    def test_range(self):
        coordinates = self.plot.load_coordinates('Program/esim3.txt')
        self.assertEqual(4.0, coordinates.get_x_range(), "X Range not right!") 
        self.assertEqual(9.0, coordinates.get_y_range(), "Y Range not right!")    

if __name__ == '__main__':
    unittest.main()