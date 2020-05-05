
class Points():
    
    def __init__(self, group):
        self.group = group 
        self.points = []
        
    def add_point(self, point):
        self.points.append(point)
        
    def get_sorted(self):
        return sorted(self.points)
    
    def get_x_max(self):
        return max([p[0] for p in self.points])     
            
    def get_y_max(self):
        return max([p[1] for p in self.points])
    
    def get_x_min(self):
        return min([p[0] for p in self.points])
        
    def get_y_min(self):
        return min([p[1] for p in self.points])


    
    
    
    

            