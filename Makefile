run: matrix_memory.cpp
	@g++ matrix_memory.cpp -O2 --std=c++14 -o main
	@./main
	@rm main
