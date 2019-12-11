#include <iostream>
#include <deque>
#include <cassert>
#include <vector>
#include <cstring>
#include <array>
#include <algorithm>
#include <random>
#include <cmath>
using namespace std;

const unsigned char D = 0;
const unsigned char C = 1;

const double WMIN = 0.1;
const double WMAX = 1.0;
const double K = 0.1;
double M = 5;
double T = 1.05;

inline double payoff(unsigned char a, unsigned char b) {
    if (a == D && b == D) 
        return 0;
    if (a == D && b == C) 
        return T;
    if (a == C && b == D) 
        return 0;
    if (a == C && b == C)
        return 1;
    return 0;
}

inline int round_player(int i, int N) {
    if (i >= N) return  i - N;
    if (i < 0) return i + N;
    return i;
}

int evolution(int L = 50, int MAX_ITER = 5001) {
    random_device rd;
    mt19937 g(rd());
    uniform_int_distribution <> dir(0, 3);
    uniform_int_distribution <> uuid(0, 9999);
    uniform_real_distribution <double> qqqq(0.0, 1.0);
    int round_uuid = uuid(g);

    int N = L * L;
    assert(N % 2 == 0);

    vector <double> payoffs;
    vector <unsigned char> _strats[2], checkpoint;
    vector <deque<double>> mem;
    payoffs.resize(N, 0);
    _strats[0].resize(N, 0);
    _strats[1].resize(N, 0);
    mem.resize(N);
    checkpoint.resize(N, 0);

    const int direction[4] = { 1, -1, L, -L };

    // 50% coop, 50% defeat
    auto &strats = _strats[0];
    for (int i = 0; i < N / 2; i++) strats[i] = C;
    for (int i = N / 2; i < N; i++) strats[i] = D;
    shuffle(strats.begin(), strats.end(), g);

    cout << "var data_" << M << " = { " << endl;
    cout << "epoch: " << MAX_ITER << "," << endl;
    for (int _iter = 0; _iter < MAX_ITER; _iter++) {
        auto &strats = _strats[_iter % 2];
        auto &next_strats = _strats[(_iter + 1) % 2];
        fill(payoffs.begin(), payoffs.end(), 0);
        // calculate coop rate
        int coop_cnt = 0;
        for (auto&& x : strats)
            if (x == C) ++coop_cnt;

        // calculate payoff
        for (int i = 0; i < N; i++) {
            for (int d = 0; d < 4; d++) {
                const int other_player = round_player(direction[d] + i, N);
                payoffs[i] += payoff(strats[i], strats[other_player]);
            }
        }
        // learn
        for (int p = 0; p < N; p++) {
            // sum up nx num
            int nx = 0;
            for (auto &&q : mem[p])
                if (q == strats[p]) ++nx;
            double wx = WMAX - (WMAX - WMIN) * nx / M;
            const int d = dir(g);
            const int other_player = round_player(direction[d] + p, N);
            double Dp = payoffs[p] - payoffs[other_player];
            double pp = wx / (1.0 + exp(Dp / K));
            if (qqqq(g) < pp) {
                next_strats[p] = strats[other_player];
            } else {
                next_strats[p] = strats[p];
            }
            mem[p].push_back(strats[p]);
            if (mem[p].size() > M) {
                mem[p].pop_front();
            }
        }
        if (_iter % 10 == 0) {
            cout << "\"epoch" << _iter << "\": [" << endl;
            for (int i = 0; i < N; i++) {
                if (checkpoint[i] != strats[i]) cout << i << ", ";
            }
            cout << "], " << endl;
            checkpoint = strats;
        }

    }
    cout << "}" << endl;
    return 0;
}

int main() {
    cin >> M >> T;
    return evolution();
}
