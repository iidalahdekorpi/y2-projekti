
class Lineplot():

    # Stores all the lines in one Lineplot object

    def __init__(self):
        self.lines = {}
    
    def add_line(self, group, points):
        self.lines[group] = points

    def get_x_max(self):
        max_x = -float('Inf')
        for group, points in self.lines.items():
            if max([p.x for p in points.points]) > max_x:
                max_x =  max([p.x for p in points.points])
        return max_x

    def get_y_max(self):
        max_y = -float('Inf')
        for group, points in self.lines.items():
            if max([p.y for p in points.points]) > max_y:
                max_y = max([p.y for p in points.points])
        return max_y

    def get_x_min(self):
        min_x = float('Inf')
        for group, points  in self.lines.items():
            if min([p.x for p in points.points]) < min_x:
                min_x = min([p.x for p in points.points])
        return min_x  

    def get_y_min(self):
        min_y = float('Inf')
        for group, points in self.lines.items():
            if min([p.y for p in points.points]) < min_y:
                min_y = min([p.y for p in points.points])
        return min_y  

    def get_x_range(self):
        if self.get_x_max() < 0:
            return self.get_x_max() + self.get_x_min()
        return self.get_x_max() - self.get_x_min()
    
    def get_y_range(self):
        if self.get_y_max() < 0:
            return self.get_y_max() + self.get_y_min()
        return self.get_y_max() - self.get_y_min()
        