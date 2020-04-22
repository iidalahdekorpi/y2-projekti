
class Lineplot():

    def __init__(self):
        self.lines = {}
    
    def add_line(self, group, points):
        self.lines[group] = points

    def get_x_max(self):
        max_x = 0
        for key, value in self.lines.items():
            if max([p[0] for p in value]) > max_x:
                max_x =  max([p[0] for p in value])
        return max_x

    def get_y_max(self):
        max_y = 0
        for key, value in self.lines.items():
            if max([p[1] for p in value]) > max_y:
                max_y = max([p[1] for p in value])
        return max_y

    def get_x_min(self):
        min_x = 0 
        for key, value in self.lines.items():
            if min([p[0] for p in value]) < min_x:
                min_x = min([p[0] for p in value])
        return min_x  

    def get_y_min(self):
        min_y = 0
        for key, value in self.lines.items():
            if min([p[1] for p in value]) < min_y:
                min_y = min([p[1] for p in value])
        return min_y  
