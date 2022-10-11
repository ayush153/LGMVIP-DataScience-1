class PowerSet():
    def __init__(self,x):
        if type(x)==set:
            self.x=x
        else:
            print("not a set")
    def __add__(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("Union result: ",self.x.union(other.x))
    def __mul__(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("Intersection result: ",self.x.intersection(other.x))
    def __sub__(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("difference result: ",self.x.difference(other.x))
