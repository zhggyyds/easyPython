from random import choice

class RandomWalk:
    def __init__(self, num = 5000):
        self.num = num

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, distance, direction):
        """compute the step"""
        return distance * direction

    def fill_walk(self):
        while(len(self.x_values) < self.num):
            direction = [-1, 1]
            distance = [0, 1, 2, 3, 4, 5, 6, 7, 8]

            x_step = self.get_step(choice(distance), choice(direction))
            y_step = self.get_step(choice(distance), choice(direction))

            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


        


