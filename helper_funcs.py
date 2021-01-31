import numpy as np
import getpass
from qiskit import QuantumCircuit
import random

from qiskit import Aer
from qiskit_ionq_provider import IonQProvider
key = str(np.genfromtxt('ionQkey.txt',dtype='str'))
provider = IonQProvider(token=key)

def get_players():
    N = 0
    while N < 2:
        N = int(input('How many players are there?\n Enter Number: '))

        if N < 2:
            delay_print('Please have at least two players')
    return N

def get_rounds():
    N = 0
    while N < 1:
        N = int(input('How many rounds would you like?\n Enter Number: '))

        if N < 1:
            delay_print('Please have at 1 round')
    return N

def get_init_state(N):
    qc = QuantumCircuit(N)
    init_string = ''
    for i in np.arange(N):
        state_valid = False
        while not state_valid:
            delay_print("Player %d, select your initial state:" % i)
            delay_print(' 0: |0>')
            delay_print(' 1: |1>')
            delay_print(' 2: (|0> + |1>)/sqrt(2)')
            state = getpass.getpass('')
            print('')

            if (state != '0') and (state != '1') and (state != '2'):
                delay_print('Please input a valid state')
            else:
                state_valid=True

        init_string += state

    for i, s in enumerate(init_string):
        if s=='1':
            qc.x(i)
        if s=='2':
            qc.h(i)
    return qc

def get_gate_and_target(N):

    # Get gate to add
    delay_print("  What gate would you like to add?")
    delay_print("    0:X      (1-qubit)", dt=0.01)
    delay_print("    1:Y      (1-qubit)", dt=0.01)
    delay_print("    2:Z      (1-qubit)", dt=0.01)
    delay_print("    3:H      (1-qubit)", dt=0.01)
    delay_print("    4:RX/4   (1-qubit)", dt=0.01)
    delay_print("    5:CNOT   (2-qubit)", dt=0.01)
    delay_print("    6:CPHASE (2-qubit)", dt=0.01)
    delay_print("    7:Swap   (2-qubit)", dt=0.01)

    while True:
        try:
            gate = int(input('    Input: '))
        except ValueError:
            delay_print(    "Sorry, didn't understand that.")
            continue
        else:
            if gate<8:
                break
            print("    Sorry, choose a gate between 0 and 7.")

    # Get target(s) to add gate to
    delay_print("  Where would you like to add this gate?  (e.g. 0 or 1,2)")
    for i in range(N):
        delay_print("    %d: qubit %d" % (i,i), dt=0.01)

    while True:
        try:
            target = list(map(int, input("    Input: ").split(',')))
            target = [t for t in target]
        except ValueError:
            delay_print(    "Sorry, didn't understand that!")
            continue
        else:

            # Ask for another input if bad qubit index
            if max(target)+1 > N or min(target)+1<1:
                delay_print("    Sorry, use a qubit index between 0 and %d!" % (N-1))
                continue

            # Use this input if we have right number of targets
            if (gate<5 and len(target)==2) or (gate>4 and len(target)==1) or len(target)>2 or len(target)==0:
                delay_print("    Sorry, use the right number of qubits!")
                continue

            break

    return gate, target

def davids_gameplay_loop(N_players, qc_init, N_rounds=1, backend_name='ionq_simulator'):

    qc = QuantumCircuit(N_players)
    qmeas = QuantumCircuit(N_players)
    qmeas.measure_all()

    for i in range(N_rounds):

        delay_print("-"*30 + "Round %d!"%(i+1) + "-"*30)

        for j in range (N_players):

            delay_print("Hello player %d...\n" % j)

            gate, target = get_gate_and_target(N_players)

            if gate == 0:
                qc.x(target[0])
            elif gate == 1:
                qc.y(target[0])
            elif gate == 2:
                qc.z(target[0])
            elif gate == 3:
                qc.h(target[0])
            elif gate == 4:
                qc.rx(np.pi/4, target[0])
            elif gate == 5:
                qc.cx(target[0],target[1])
            elif gate == 6:
                qc.cz(target[0],target[1])
            elif gate == 7:
                qc.swap(target[0],target[1])

            print(qc)

            delay_print('\n'+"-"*50)

        if i+1 < N_rounds:
            delay_print("Preparing a measurement...")
            print(qc+qmeas)
            backend = provider.get_backend(backend_name)
            job = backend.run(qc_init+qc+qmeas, shots=2)
            result = job.result()
            # Since we only have 2 shots, take a random bitstr for the meas.
            meas = random.choice(list(result.data()['counts'].keys()))
            print("Result: %s" % meas[::-1])
            delay_print("The measurement operators will now be removed!\n")

    delay_print("Time for the final results...")
    delay_print("-"*50)

    return qc

def game_end(N, qc_init, qc_game, shots=1000, backend_name='ionq_simulator'):
    qc = qc_init + qc_game
    qc.measure_all()

    f = open("./text_art/final_circuit.txt", "r", encoding="utf8")
    delay_print(f.read(), dt=0.009)
    print(qc)
    delay_print('')

    delay_print('Calculating...')

    backend = provider.get_backend(backend_name)
    job = backend.run(qc, shots=shots)
    result = job.result()
    counts_dict = result.data()['counts']

    player_counts = np.zeros(N)
    for key in counts_dict:
        for i, s, in enumerate(key[::-1]):
            player_counts[i] += int(s) * counts_dict[key]
    player_p1 = player_counts / shots

    return player_p1, np.argmax(player_p1)

import sys
import time
def delay_print(s, dt=0.04):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(dt)
    sys.stdout.write('\n')
    sys.stdout.flush()
