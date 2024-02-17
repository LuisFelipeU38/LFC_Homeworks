from dfa import DFA

def main():
    # Definir el autómata
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q2'}
    }
    start_state = 'q0'
    accept_states = {'q0'}

    dfa = DFA(states, alphabet, transitions, start_state, accept_states)

    # Leer la cadena de entrada desde la línea de comandos
    input_string = input("Ingrese la cadena a verificar: ")

    # Procesar la cadena
    for symbol in input_string:
        dfa.transition(symbol)

    # Determinar si la cadena es aceptada o no
    if dfa.is_accepting():
        print("La cadena es aceptada por el autómata.")
    else:
        print("La cadena no es aceptada por el autómata.")

if __name__ == "__main__":
    main()
