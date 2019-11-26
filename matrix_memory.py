import random
import math
from collections import deque

DEFEAT = 0
COOPERATE = 1
T = 1.02
WMIN = 0.1
WMAX = 1.0
K = 0.1
M = 5

PAYOFF = [
    [[0, 0], [T, 0]],
    [[0, T], [1, 1]]
] # REF: 囚徒困境博弈模型 P.7

def payoff(a, b):
    return PAYOFF[a][b][0]

def build_graph(L = 100) -> (list, list):
    players = [0] * (L * L)
    edges = []
    directions = [(0, 1), (1, 0)]
    for i in range(L):
        for j in range(L):
            for (dx, dy) in directions:
                i_ = (i + dx) % L # 1 and n row are connected
                j_ = (j + dy) % L
                x = i * L + j
                y = i_ * L + j_
                edges.append((x, y))
    return players, edges

players, edges = build_graph(2)

def play_game(players, edges, memory_window, max_step):
    # first iteration
    N = len(players)
    assert N % 2 == 0
    strategy = [0] * (N // 2) + [1] * (N // 2)
    random.shuffle(strategy)
    memory = [deque() for e in range(N)]
    
    for _iter in range(max_step):
        payoffs = [0] * N
        player_for_decision = [0] * N
        random.shuffle(edges)
        coop_cnt = 0
        for p in range(N):
            if strategy[p] == COOPERATE:
                coop_cnt += 1
        print(f"#{_iter} window = {memory_window} cooperate rate = {coop_cnt / N}")

        for (x, y) in edges:
            payoffs[x] += payoff(strategy[x], strategy[y])
            payoffs[y] += payoff(strategy[y], strategy[x])
            if player_for_decision[x] == 0:
                player_for_decision[x] = y
            if player_for_decision[y] == 0:
                player_for_decision[y] = x
            if random.random() < 0.5:
                player_for_decision[x] = y
            if random.random() < 0.5:
                player_for_decision[y] = x
        # to this point, each player selected a neighbour to learn
        _strategy = strategy[:]
        for p in range(N):
            nx = sum(1 if strategy[p] == x else 0 for x in memory[p])
            wx = WMAX - (WMAX - WMIN) * nx / memory_window
            target_player = player_for_decision[p]
            Dp = payoffs[p] - payoffs[target_player]
            pp = 0.0
            try:
                pp = wx / (1.0 + math.exp(Dp / K))
            except:
                pass

            if random.random() < pp:
                strategy[p] = _strategy[target_player]
            else:
                pass
                # strategy[p] = 1 - strategy[p]
            memory[p].append(strategy[p])
            if len(memory[p]) > memory_window:
                memory[p].popleft()
        # to this point, strategy of next round is updated
play_game(*build_graph(50), M, 50000)
