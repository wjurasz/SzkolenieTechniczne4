from math import pi

class square:
    def __init__(self, length):
        self.lenght = length
    def pole(self):
        return 4 * self.lenght
    def obwod(self):
        return self.lenght * self.lenght
    
class circle:
    def __init__(self,radius):
        self.radius = radius
    def obwod(self):
        return 2 * pi * self.radius
    def pole(self):
        return pi * self.radius ** 2
    
class trapeze:
    def __init__(self,lenghta,lenghtb,height,lenghtc,lenghtd):
        self.lenghtA = lenghta
        self.lenghtB = lenghtb
        self.height  =  height
        self.lenghtC = lenghtc
        self.lenghtD = lenghtd
    def pole(self):
        return (self.lenghtA + self.lenghtB)/2 * self.height
    def obwod(self):
        return self.lenghtA + self.lenghtB + self.lenghtC + self.lenghtD


sqr = square(10)
print("Pole to", sqr.obwod)
