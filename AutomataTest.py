import unittest
from Automata import Automata


class TestAutomata(unittest.TestCase):

    test_unit = None
    state_name = "testState"
    transition_letter = "s"
    from_state_id = 42
    to_state_id = 91

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.test_unit = Automata()

    def test_add_and_get_state(self):
        self.assertIsNone(self.test_unit.get_state(self.state_name))
        self.test_unit.add_state(self.state_name)
        state = self.test_unit.get_state(self.state_name)
        self.assertIsNotNone(state)
        self.assertIs(state.name, self.state_name)

    def test_add_initial_state(self):
        self.test_unit.add_initial_state(self.state_name)
        self.assertTrue(self.test_unit.get_state(self.state_name).initial)

    def test_add_accepting_state(self):
        self.test_unit.add_accepting_state(self.state_name)
        self.assertTrue(self.test_unit.get_state(self.state_name).accepting)

    def test_add_transition(self):
        self.assertIsNone(self.test_unit.get_transition_by_from_state_id(self.from_state_id))
        self.test_unit.add_transition(self.transition_letter, self.from_state_id, self.to_state_id)
        transition = self.test_unit.get_transition_by_from_state_id(self.from_state_id)
        self.assertIsNotNone(transition)
        self.assertIs(transition.from_state_id, self.from_state_id)
        self.assertIs(transition.to_state_id, self.to_state_id)
        self.assertIs(transition.letter, self.transition_letter)

    def test_accepts_rejects_single_char(self):
        # q0 - a -> (q1)
        self.test_unit.add_initial_state('q0')
        self.test_unit.add_accepting_state('q1')
        self.test_unit.add_transition('a', 'q0', 'q1')

        self.assertTrue(self.test_unit.accepts('a'))
        self.assertFalse(self.test_unit.accepts('b'))

    def test_accepts_rejects_three_chars(self):
        # q0 - a -> (q1)
        # (q1) - b -> q0
        self.test_unit.add_initial_state('q0')
        self.test_unit.add_accepting_state('q1')
        self.test_unit.add_transition('a', 'q0', 'q1')
        self.test_unit.add_transition('b', 'q1', 'q0')

        self.assertTrue(self.test_unit.accepts('aba'))
        self.assertFalse(self.test_unit.accepts('ab'))


def main():
    unittest.main()

if __name__ == '__main__':
    main()