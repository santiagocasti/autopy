from State import State
from Transition import Transition


class Automata:
    """ Class representing an FDA
        It contains the states, transitions and an initial state of the automata.
        It has a method to compute if a given word is accepted by the automata.
    """

    def __init__(self):
        self.states = {}
        self.transitions = {}
        self.initial_state = ''

    def add_state(self, name):
        state = State(name)
        self.states[name] = state
        return state

    def get_state(self, name):
        return self.states.get(name)

    def add_initial_state(self, name):
        state = self.add_state(name)
        state.initial = True
        self.initial_state = name
        return state

    def add_accepting_state(self, name):
        state = self.add_state(name)
        state.accepting = True
        return state

    def add_transition(self, letter, from_state_id, to_state_id):
        transition = Transition()
        transition.letter = letter
        transition.from_state_id = from_state_id
        transition.to_state_id = to_state_id
        self.transitions[from_state_id] = transition

    def get_transition_by_from_state_id(self, from_state_id):
        return self.transitions.get(from_state_id)

    def accepts(self, word):
        """ Check if the word is accepted by the automata
        """

        # initialise the stack to the initial state
        stack = [self.states.get(self.initial_state)]

        # For every character in the word:
        for c in word:

            # If the stack length is 0, then it is not accepted
            if len(stack) == 0:
                return False

            # Get the latest state in the stack
            state = stack.pop()
            transition_out = self.transitions.get(state.name)

            # If the transition letter is the current letter, then append the
            # "to state" of the transition to the stack

            # @type transition_out: Transition
            if transition_out.letter == c:
                stack.append(self.states[transition_out.to_state_id])

        # only accept if the end state is accepting
        if len(stack) == 1 and stack.pop().accepting:
            return True
        else:
            return False
