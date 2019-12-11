import random
import math

DEFEAT = 0
COOPERATE = 1
PAYOFF = [
    [[-1, -1], [10, -10]],
    [[-10, 10], [1, 1]]
]

FORGET_SPEED = 50

def payoff(a, b):
    return PAYOFF[a][b]

def decide(history: list):
    cnt = [1, 1]
    d = 0.5
    s = 0.25
    t = len(history)
    for h in history:
        cnt[h] += math.pow(t * FORGET_SPEED, -d)
        t = t - 1
    cnt[0] = math.log(cnt[0])
    cnt[1] = math.log(cnt[1])
    cnt[0] += random.normalvariate(0, math.pi * s / math.sqrt(3))
    cnt[1] += random.normalvariate(0, math.pi * s / math.sqrt(3))
    if cnt[0] > cnt[1]:
        return DEFEAT
    else:
        return COOPERATE

print("DD DC CD CC")

N = 1000
overall_choice = {}
for __iter in range(N):
    history = [[], []]
    payoffs = [0, 0]
    choice = {}
    for _iter in range(300):
        a_decision = decide(history[1])
        b_decision = decide(history[0])
        [p_a, p_b] = payoff(a_decision, b_decision)
        history[0].append(a_decision)
        history[1].append(b_decision)
        payoffs[0] += p_a
        payoffs[1] += p_b
        key = f"{a_decision}{b_decision}"
        choice[key] = choice.get(key, 0) + 1
        overall_choice[_iter] = overall_choice.get(_iter, {})
        overall_choice[_iter][key] = overall_choice[_iter].get(key, 0) + 1

for (k, v) in overall_choice.items():
    print(v.get("00", 0), v.get("01", 0), v.get("10", 0), v.get("11", 0))
