from math import comb

p = 0.01
m_values = [2, 3, 4, 5]

# Calculate P_e for Hamming codes
def calculate_pe(n, p):
    pe = sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(2, n + 1))
    return pe

# Compute results
results = []
for m in m_values:
    n = 2**m - 1
    k = n - m
    R = k / n
    Pe = calculate_pe(n, p)
    results.append((m, n, k, R, Pe))

for result in results:
    print(result)