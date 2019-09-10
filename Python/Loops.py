"""
Task
Read an integer N. For all non-negative integers i < N, print i**2 .
See the sample for details.

Input Format

The first and only line contains the integer,N .

Constraints
1 <= N <= 20

Output Format

Print  lines, one corresponding to each .
"""
if __name__ == '__main__':
    n = int(input())

# Brute force soloution:
m = 0 # dummy variable

while m != n:
    print(m**2)
    m = m + 1
