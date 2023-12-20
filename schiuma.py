from decorator import Decorator

class Schiuma(Decorator):
    def name(self):
        return "Schiuma, " + self.component.name()