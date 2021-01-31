# Imports
from helper_funcs import *

def main():

    delay_print(80*'-', dt=0.003)
    f = open("./text_art/title.txt", "r", encoding="utf8")
    delay_print(f.read(), dt=0.005)
    delay_print(80*'-', dt=0.003)
    delay_print('Would you like instructions (y/n)?', dt=0.003)
    if str(input()) == 'y':
        s0 = " In this game, the players are qubits."
        s1 = " Your goal is to maximize your excitation (expected value of finding your qubit in the |1> state)."
        s2 = " Players will pick the initial state of their qubit, unknown to the other players."
        s3 = " Then, players will consecutively add gates to a circuit, rotating or entangling any qubits."
        s4 = " After every round, a non-projective measurement bitstring will be given, to get a glimpse of the current state."
        s5 = " The player with the maximum excitation probability at the end wins...good luck!~"
        delay_print("Welcome to Quantum Supremacy!"+s1+s2+s3+s4+s5, dt=0.04)

    print('\n')
    N = get_players()
    N_rounds = get_rounds()
    # backend_name = 'ionq_simulator'
    backend_name = 'ionq_qpu'

    delay_print(80*'-', dt=0.005)
    qc_init = get_init_state(N)
    delay_print('Let the game begin! We will start the adding of gates now...\n', dt=0.04)
    qc_game = davids_gameplay_loop(N, qc_init, N_rounds = N_rounds, backend_name = backend_name)

    p1_vec, winner_ind = game_end(N, qc_init, qc_game, backend_name = backend_name) # N argument is temp
    if backend_name is 'ionq_simulator':
        # add some noise since ties are common
        p1_vec += np.random.normal(0,0.1,np.shape(p1_vec))

    import matplotlib.pyplot as plt
    fig = plt.figure()
    players = ['Player %d' % (i) for i in range(N)]
    plt.bar(players,p1_vec, color='maroon')
    plt.ylim([0,1])
    plt.title('Final Excitations: Congrats to Player %d!' % (winner_ind))
    plt.ylabel('Excitation Probability')

    print(p1_vec)
    delay_print('Player ' + str(winner_ind) + ' is the winner!')

    f = open("./text_art/end.txt", "r", encoding="utf8")
    delay_print(f.read(), dt=0.009)

    plt.show()

if __name__ == "__main__":
    main()
