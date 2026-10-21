#overloading
#so for overloading i need to use args in python otherwise it is difficult 
class Add:
    def __init__(self):
        pass
    def connectString(self, s1 , s2,*args):
        res = s1+s2
        for string in args:
            res+= string
        return res
    

add = Add()

print(add.connectString(s1 = "Hi ", s2="how"))
print(add.connectString("Hi ","how ","are ", "you "))