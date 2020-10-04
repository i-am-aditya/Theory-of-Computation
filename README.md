# Theory-of-Computation
This repository contains my assignment work related to Theory of Computation aka Formal Language and Automata where the codes for various concepts in ToC are implemented.

The output for the Python code "FA.py" is:

Enter list of states separated by spaces: q0 q1 q2 q3

Enter input alphabet separated by spaces: 0 1
Enter transitions for state q2. If required, use 'REJECT'.

CURRENT STATE : q2 INPUT ALPHABET : 1 NEXT STATE : q3

CURRENT STATE : q2 INPUT ALPHABET : 0 NEXT STATE : q2
Enter transitions for state q3. If required, use 'REJECT'.

CURRENT STATE : q3 INPUT ALPHABET : 1 NEXT STATE : q3

CURRENT STATE : q3 INPUT ALPHABET : 0 NEXT STATE : q3
Enter transitions for state q0. If required, use 'REJECT'.

CURRENT STATE : q0 INPUT ALPHABET : 1 NEXT STATE : q1

CURRENT STATE : q0 INPUT ALPHABET : 0 NEXT STATE : q0
Enter transitions for state q1. If required, use 'REJECT'.

CURRENT STATE : q1 INPUT ALPHABET : 1 NEXT STATE : q2

CURRENT STATE : q1 INPUT ALPHABET : 0 NEXT STATE : q1

TRANSITION FUNCTION Q X SIGMA -> Q
CURRENT STATE INPUT ALPHABET NEXT STATE
q2		1		q3
q2		0		q2
q3		1		q3
q3		0		q3
q0		1		q1
q0		0		q0
q1		1		q2
q1		0		q1

Enter the START STATE: q0

Enter the FINAL STATES: q0 q1 q2

The DFA is accepted.

Enter the Input String: 011001
Rejected!

The NFA is accepted.

Enter the Input String: aba
Accepted!
The final state that the NFA stopped on: {'q2', 'q1'}

Its Equivalent DFA is accepted.

Enter the Input String: aba
Accepted!
The final state that the Equivalent DFA stopped on: {q1,q2}
