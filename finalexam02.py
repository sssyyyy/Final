from math import sqrt
class exam:
    x=0
    y=0
    def __init__(self,c,d):
        self.x=c
        self.y=d
    def distance(self,a,b):
        c=sqrt(pow((self.x-a),2)+pow((self.y-b),2))
        print(c)
    def __add__(self,a,b):
         print("p1+p2={0},{1}".format(x+a,y+b))
ex=exam(1,1)
ex1=exam(2,2)
ex.distance(2,2)