print("g++ matrix_memory.cpp -O2 --std=c++14 -o main")
for M in [5, 10]:
    for T in [1.02, 1.04]:
        print(f"echo Running M={M} T={T}")
        print(f"./main > data_{M}_{T}.txt <<EOF")
        print(M, T)
        print("EOF")
print("rm main")
