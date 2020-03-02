class Tree(object):
    
    def __init__(self, leaf_count=0, stem_count=0, trunck_size=0, root_count=0):
        self.leafCount = leaf_count
        self.stemCount = stem_count
        self.trunckSize = trunck_size
        self.rootCount = root_count
        
    def swing_left(self):
        print('<<<<<<<<<<<<<<')
        
    def swing_right(self):
        print('>>>>>>>>>>>>>>')
        
        
class Human(object):

    def __init__(self, shirt, trouser, shoe):

        self.shirt = shirt
        self.trouser = trouser
        self.shoe = shoe


    def walk(self, direction):

        print("Moving ->" + direction)
        return True


    def run(self, direction):

        print("Running ->" + direction)
        return True


    def jump(self, direction):
        print("Jump ->" + direction)
        return True;


    def action(self):
        self.walk("West")
        self.walk("North")
        self.run("East")
        self.jump("Up")



class InHuman(Human):

    def __init__(self, shirt, trouser, shoe, powers):

        super(InHuman, self).__init__(shirt, trouser, shoe)
        self.powers = powers


    def fly(self, direction):

        print("fly ->" + direction)
        return True

    # Overriding
    def action(self):

        self.walk("East");
        self.run("North");
        self.fly("High");
        self.fly("Low");


if __name__ == '__main__':
    h = InHuman(1, 2, 3, 4);
    h.action()

