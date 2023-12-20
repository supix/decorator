from decorator import Decorator

class Zucchero(Decorator):
    def name(self):
        return "Zucchero, " + self.component.name()