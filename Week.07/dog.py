class Dog:
    # def __init__(self, age=None, colour=None, size=None):
    def __init__(self, age=0, colour="brown", size="medium"):
        self.age = age
        self.colour = colour
        self.size = size

    def __str__(self):
        s = "I am a " + self.colour + " dog, of age "
        s += str(self.age)+", of size "+self.size
        return(s)

    def wag_tail(self, speed="slowly"):
        print("See my", self.colour, "tail wagging", speed)

    def bark(self, how="loudly"):
        print("I am barking", how, "said the", self.colour, "dog!")
