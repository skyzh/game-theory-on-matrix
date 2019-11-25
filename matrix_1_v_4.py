import random
import math
from collections import deque

DEFEAT = 0
COOPERATE = 1
T = 2
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

def play_game(players, edges, memory_window):
    # first iteration
    N = len(players)
    assert N % 2 == 0
    strategy = [0] * (N // 2) + [1] * (N // 2)
    random.shuffle(strategy)
    memory = [deque() for e in range(N)]
    for _iter in range(10000):
        payoffs = [0] * N
        payoffs_inv = [0] * N
        coop_cnt = 0
        for p in range(N):
            if strategy[p] == COOPERATE:
                coop_cnt += 1
        if _iter % 100 == 0:
            print(f"window = {memory_window} cooperate rate = {coop_cnt / N}")

        for (x, y) in edges:
            payoffs[x] += payoff(strategy[x], strategy[y])
            payoffs_inv[x] += payoff(1 - strategy[x], strategy[y])
            payoffs[y] += payoff(strategy[y], strategy[x])
            payoffs_inv[y] += payoff(1 - strategy[y], strategy[x])
        # to this point, strategy is played
        for p in range(N):
            if payoffs[p] > payoffs_inv[p]:
                strategy[p] = 1 - strategy[p]
            memory[p].append(strategy[p])
            if len(memory[p]) > memory_window:
                memory[p].popleft()
        # to this point, strategy is the one to be stored into memory
        for p in range(N):
            nx = sum(1 if strategy[p] == x else 0 for x in memory[p])
            qc = nx / memory_window
            if not random.random() < qc:
                strategy[p] = 1 - strategy[p]
        # to this point, strategy of next round is updated

for _m in range(10, 20):
    play_game(*build_graph(), _m)