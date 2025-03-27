from abc import ABC, abstractmethod

# Abstract base class for all states
class State(ABC):
    @abstractmethod
    def on_input(self, char: str) -> 'State':
        """Handles the transition for a given input character ('0' or '1')."""
        pass

    @abstractmethod
    def get_output(self) -> int:
        """Returns the output (remainder) associated with the final state."""
        pass


# State representing remainder 0
class S0(State):
    def on_input(self, char: str) -> State:
        return S0() if char == '0' else S1()

    def get_output(self) -> int:
        return 0


# State representing remainder 1
class S1(State):
    def on_input(self, char: str) -> State:
        return S2() if char == '0' else S0()

    def get_output(self) -> int:
        return 1


# State representing remainder 2
class S2(State):
    def on_input(self, char: str) -> State:
        return S1() if char == '0' else S2()

    def get_output(self) -> int:
        return 2


# Finite State Machine that uses the states to process binary strings
class FSM:
    def __init__(self, start_state: State):
        """
        Initializes the FSM with a given starting state.
        :param start_state: The state at which FSM begins (typically S0).
        """
        self.start_state = start_state
        self.current_state = start_state

    def reset(self):
        """Resets the FSM to the initial starting state."""
        self.current_state = self.start_state

    def process(self, binary_str: str) -> int:
        """
        Processes the binary string and returns the remainder when interpreted as a binary number divided by 3.
        :param binary_str: A string of '0's and '1's.
        :return: The remainder (0, 1, or 2).
        """
        for char in binary_str:
            self.current_state = self.current_state.on_input(char)
        return self.current_state.get_output()


# Entry point for manual testing
if __name__ == "__main__":
    fsm = FSM(S0())
    binary_input = input("Enter binary string: ").strip().replace('"', '')
    result = fsm.process(binary_input)
    print(f"Remainder when {binary_input} is divided by 3 is: {result}")
