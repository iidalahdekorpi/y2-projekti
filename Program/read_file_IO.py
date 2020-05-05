from corrupted_coordinate_file_error import CorruptedCoordinateFileError
from points import Points
from coordinates import Coordinates
from lineplot import Lineplot

class ReadFile():
        
    def load_coordinates(self, input):

        self.plot = Lineplot()
        groups_read = []
        try:
            f = open(input, "r")
            for line in f:
                line = line.split(",")
                if len(line) != 3:
                    raise CorruptedCoordinateFileError("ERROR in data format")
                x = float(line[0])
                y = float(line[1])
                coordinate = Coordinates(x,y)
                group = line[2].strip()
                if group not in groups_read:
                    if groups_read != []:
                        self.plot.add_line(points.group, points)
                    points = Points(group)
                    groups_read.append(group)
                points.add_point(coordinate)
            self.plot.add_line(points.group, points)
            f.close()
            return self.plot


        except OSError:
            raise CorruptedCoordinateFileError("ERROR reading the file")       
               