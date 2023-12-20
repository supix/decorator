from decorator import Decorator

class Cacao(Decorator):
    def name(self):
        return "Cacao, " + self.component.name()