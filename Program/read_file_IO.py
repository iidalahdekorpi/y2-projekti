from corrupted_coordinate_file_error import CorruptedCoordinateFileError
from points import Points
from coordinates import Coordinates
from lineplot import Lineplot

class ReadFile():
        
    def load_coordinates(self, input):

        self.plot = Lineplot()
        points_read = []
        try:
            file = open(input, "r")
            for line in file:
                line = line.split(",")
                if len(line) != 3:
                    raise CorruptedCoordinateFileError("ERROR in data format")
                x = line[0]
                y = line[1]
                group = line[2]
                if group  not in self.plot.lines:
                    points = Points(group)
                points.add_point(Coordinates(x,y))
                points_read.append(points)
            file.close()
            for p in points_read:
                self.plot.add_line(p.group, p.get_sorted)
            return self.plot


        except OSError:
            raise CorruptedCoordinateFileError("ERROR reading the file")       
               