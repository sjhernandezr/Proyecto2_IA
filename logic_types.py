class Term:
    def __init__(self,name, is_variable=False):
        self.name = name
        self.is_variable = is_variable=False
    def __eq__(self, other):
        return self.name == other.name and self.is_variable == other.is_variable
class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    