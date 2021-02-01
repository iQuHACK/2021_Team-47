    ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗
    ██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║
    ██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║
    ╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║
    ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║
    ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝

    ░██████╗██╗░░░██╗██████╗░██████╗░███████╗███╗░░░███╗░█████╗░░█████╗░██╗░░░██╗
    ██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝
    ╚█████╗░██║░░░██║██████╔╝██████╔╝█████╗░░██╔████╔██║███████║██║░░╚═╝░╚████╔╝░
    ░╚═══██╗██║░░░██║██╔═══╝░██╔══██╗██╔══╝░░██║╚██╔╝██║██╔══██║██║░░██╗░░╚██╔╝░░
    ██████╔╝╚██████╔╝██║░░░░░██║░░██║███████╗██║░╚═╝░██║██║░░██║╚█████╔╝░░░██║░░░
    ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

# What is "Quantum Supremacy"?
This is a game designed to help players get an intuition for gate-model quantum computing, quantum entanglement, and measurement!

## Description
In this game, the players are qubits. Your goal is to maximize your excitation (probability of finding your qubit in the |1> state). Players pick the initial state of their qubit, unknown to the other players. Then, players consecutively add gates to a circuit, rotating or entangling any qubits. After every round, a non-projective measurement bitstring will be given, to get a glimpse of the current state. The player with the maximum <sigma_z> at the end wins...good luck!~

## Next Steps
In the future, the game mechanics can be made more rich by adding random gates after every round, introducing more complex gates in the game, or adding projective measurements randomly.

# Usage
1. Clone the repository.
2. Acquire anm IonQ API key, and throw it in the project directory, in a text file named `ionQkey.txt`. This is referenced in line 8 of `helper_funcs.py`.
3. Run the script `quantum_supremacy.py`, and play! 

Note that, the backend used is defined with the variable `backend_name` in `quantum_supremacy.py`- the game has been tested with both the `ionq_simulator` and `ionq_qpu` backends. 
