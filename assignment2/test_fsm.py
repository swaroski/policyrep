import unittest
from assignment2.fsm import FSM, S0


class TestMod3FSM(unittest.TestCase):
    def setUp(self):
        """Initialize the FSM with starting state S0 before each test."""
        self.fsm = FSM(S0())

    def test_examples(self):
        """Test known examples provided in the assignment2."""
        self.assertEqual(self.fsm.process("1101"), 1)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("1110"), 2)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("1111"), 0)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("1010"), 1)

    def test_single_digits(self):
        """Test single-bit binary strings."""
        self.fsm.reset()
        self.assertEqual(self.fsm.process("0"), 0)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("1"), 1)

    def test_double_digits(self):
        """Test two-bit binary strings."""
        self.fsm.reset()
        self.assertEqual(self.fsm.process("00"), 0)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("01"), 1)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("10"), 2)
        self.fsm.reset()
        self.assertEqual(self.fsm.process("11"), 0)

    def test_empty_string(self):
        """Test behavior when an empty string is passed."""
        self.fsm.reset()
        self.assertEqual(self.fsm.process(""), 0)


if __name__ == "__main__":
    unittest.main()