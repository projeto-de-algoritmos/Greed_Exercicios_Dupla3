def sort_armys(Q, N):
    Q.sort()
    N.sort()

def number_battles_noglonia_win_in_war(S, Q, N):
    sort_armys(Q, N)

    qi = ni = victories = 0

    while ni < S and qi < S:
        if N[ni] > Q[qi]:
            victories += 1
            qi += 1
        ni += 1

    return victories

S = int(input().strip())
Q = list(map(int, input().strip().split()))
N = list(map(int, input().strip().split()))

print(number_battles_noglonia_win_in_war(S, Q, N))
