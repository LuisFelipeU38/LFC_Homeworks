class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = start_state
        self.accept_states = accept_states

    def transition(self, input_symbol):
        if input_symbol in self.alphabet:
            self.current_state = self.transitions[self.current_state][input_symbol]
        else:
            raise ValueError("Input symbol not in alphabet")

    def is_accepting(self):
        return self.current_state in self.accept_states