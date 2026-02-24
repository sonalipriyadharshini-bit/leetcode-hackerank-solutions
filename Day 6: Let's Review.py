# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of test cases
T = int(input())
for _ in range(T):
    S = input()
    even_indexed = S[::2]
    odd_indexed = S[1::2]
    print(f"{even_indexed} {odd_indexed}")
