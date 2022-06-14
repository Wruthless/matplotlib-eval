# A random walk is a path that has no clear direction but is determined by a 
# series of random decisions, each of which is left entirely to chance. They 
# have practical applications in many areas. Molecular motion, for example, is
# random. A random walk could be used to model that.

from random import choice

class RandomWalk:
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Fill walk with points and determine direction of each step."""
        
        # Keep taking steps until the walk reaches its desired length
        # num_points = 5000 by default.
        while len(self.x_values) < self.num_points:
            
            # Decide direction and how far to go
            # 1 = right, -1 = left
            x_direction = choice([1,-1])
            
            # How far to move left or right
            x_distance = choice([0,1,3,4])
            
            # Determine the length of each step by multiplying the direction of # movement by the distance chosen.
            x_step = x_direction * x_direction
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # New position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)