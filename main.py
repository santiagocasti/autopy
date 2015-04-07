from Automata import Automata

myAutomata = Automata()
myAutomata.add_initial_state('q0')
myAutomata.add_state('q1')
myAutomata.add_accepting_state('q2')

# q0 - a -> q1
myAutomata.add_transition('a', 'q0', 'q1')
# q1 - b -> (q2)
myAutomata.add_transition('b', 'q1', 'q2')

words = {'ab', 'ba', 'aa', 'bb'}

for word in words:
    if myAutomata.accepts(word):
        print word + " is accepted.\n"
    else:
        print word + " is not accepted.\n"
