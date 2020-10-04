"""" This program deals with the concepts of Finite Automata (FA) that includes DFA, NFA and NFA-DFA conversion. """
""" Package used - automata-lib """

from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

""" Deterministic Finite Automata (DFA) """

Q_input = input("Enter list of states separated by spaces: ").split()
Q = set(Q_input)

SIGMA_input = input("Enter input alphabet separated by spaces: ").split()
SIGMA = set(SIGMA_input)

transition_dict = {el : {el_2 : 'REJECT' for el_2 in SIGMA} for el in Q}
for key, dict_value in transition_dict.items():
    print("Enter transitions for state {}. If required, use 'REJECT'.".format(key))
    for input_alphabet, transition_state in dict_value.items():
        transition_dict[key][input_alphabet] = input("CURRENT STATE : {} INPUT ALPHABET : {} NEXT STATE : ".format(key, input_alphabet))
print("\nTRANSITION FUNCTION Q X SIGMA -> Q")
print("CURRENT STATE INPUT ALPHABET NEXT STATE")
for key, dict_value in transition_dict.items():
    for input_alphabet, transition_state in dict_value.items():
        print("{}\t\t{}\t\t{}".format(key, input_alphabet, transition_state))

while(True):
    start = input("Enter the START STATE: ")
    accept = input("Enter the FINAL STATES: ").split()
    #Making sure that start and accept are both in Q and that start and accept are not the state
    if (start in Q) and (set(accept).issubset(Q)):
        initial =  start 
        final = accept
        break
    else:
         print("Please enter STATE_STATE and ACCEPT_STATES that are in Q : {}.\nAccept states should be a valid subset of Q\n".format(Q))
         
CURRENT_STATE = None
dfa = DFA(
    states=Q,
    input_symbols=SIGMA,
    transitions=transition_dict,
    initial_state=initial,
    final_states=set(final)
)
if dfa.validate():
    print("\nThe DFA is accepted.")
    s = input("Enter the Input String: ")
    if dfa.accepts_input(s):
        print('Accepted!')
        print("The final state that the DFA stopped on:", dfa.read_input(s))
    else:
        print('Rejected!')
else:
    print("\nThe DFA is rejected.")
    
""" Non-Deterministic Finite Automata (NFA) """

nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}},
        'q1': {'a': {'q1'}, '': {'q2'}}, # '' refers to empty string (lambda/epsilon) transitions
        'q2': {'b': {'q0'}}
    },
    initial_state='q0',
    final_states={'q1'}
)

if nfa.validate():
    print("\nThe NFA is accepted.")
    s2 = input("Enter the Input String: ")
    if nfa.accepts_input(s2):
        print('Accepted!')
        print("The final state that the NFA stopped on:", nfa.read_input(s2))
    else:
        print('Rejected!')
else:
    print("\nThe new NFA is rejected.")

""" NFA-DFA conversion """

equivalent_dfa = DFA.from_nfa(nfa)
if equivalent_dfa.validate():
    print("\nIts Equivalent DFA is accepted.")
    s3 = input("Enter the Input String: ")
    if equivalent_dfa.accepts_input(s3):
        print('Accepted!')
        print("The final state that the Equivalent DFA stopped on:", equivalent_dfa.read_input(s3))
    else:
        print('Rejected!')
else:
    print("\Its Equivalent DFA is rejected.")