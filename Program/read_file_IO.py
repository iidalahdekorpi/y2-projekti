
from corrupted_coordinate_file_error import CorruptedCoordinateFileError
from points import Point
from coordinates import Coordinates

class ReadFile:
        
    def load_coordinates(self, input):
        
        try:
            x_read = False
            y_read = False
            group_read = False 
            file = open(input, "r")
            for line in file:
                line = line.split(",")
                if len(line) != 3:
                    raise CorruptedCoordinateFileError("ERROR in data format")
                x = line[0]
                y = line[1]
                group = line[2]
                if x.isdigit:
                    x_read = True 
                else:
                    raise CorruptedCoordinateFileError("ERROR in x-coordinate data format")
                if y.isdigit:
                    y_read = True
                else:
                    raise CorruptedCoordinateFileError("ERROR in y-coordinate data format")
                new_point = Coordinates(x,y)
               
                   
            
               
               
               
        except OSError:
            raise CorruptedCoordinateFileError("ERROR reading the file")       
               