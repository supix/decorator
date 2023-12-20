from decorator import Decorator

class Caffe(Decorator):
    def name(self):
        return "Caffè, " + self.component.name()