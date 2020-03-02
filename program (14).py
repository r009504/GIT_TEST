class A(object):
    def play(self):
        print ('Playing a sport')
        
class B(A):
    def swim(self):
        print ('Swimming in a pool')
        
class C(B):
    def sing(self):
        print ('Singing a song')
        
# User     
def action(x):
    x.play()

    
a = A()
b = B()
c = C()

action(c)