# Builder Design Pattern
from abc import ABC, abstractmethod
class BallBuilder(ABC):
    @abstractmethod
    def weight(self):
        pass

    @abstractmethod
    def radius(self):
        pass

    @abstractmethod
    def leathertype(self):
        pass

class Football(BallBuilder):
    
    def weight(self):
        print("Football weight")
    
    def radius(self):
        print("Football Radius")
    
    def leathertype(self):
        print("Football Leather Type")
    
    def print_status(self):
        print("Football Completed\n")

class Tennisball(BallBuilder):
    
    def weight(self):
        print("Tennis Ball weight")
    
    def radius(self):
        print("Tennis Ball  Radius")
    
    def leathertype(self):
        print("Tennis Ball  Leather Type")
    
    def print_status(self):
        print("Tennisball Completed\n")

class Director:

    def set_builder(self, obj):
        self.ball_builder = obj # Football() / Tennisball()
    
    def construct(self, ball_name):
        if ball_name == "Football":
            self.ball_builder.weight()
            self.ball_builder.radius()
            self.ball_builder.leathertype()
            self.ball_builder.print_status()
        elif ball_name == "TennisBall":
            self.ball_builder.weight()
            self.ball_builder.radius()
            self.ball_builder.leathertype()
            self.ball_builder.print_status()

class Main:
    # Football Builder
    foot_ball = Football()
    director = Director()
    director.set_builder(foot_ball)
    director.construct('Football')

    # Tennisball Builder
    tennis_ball = Tennisball()
    director.set_builder(tennis_ball)
    director.construct('TennisBall')

if __name__ == '__main__':
    Main()




