class State:
    """A state represent the start, end or intermediate situation of a FDA.
       It has a name, could be accepting and/or initial.
    """
    def __init__(self, name):
        self.name = name
        self.accepting = False
        self.initial = False
