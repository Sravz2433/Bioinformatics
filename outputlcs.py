# python3

import sys
import numpy as np

'''
Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)

Sample Input:
     ACACTGTGA

Sample Output:
     AACTGG

Pseudocode:
    LCSBackTrack(v, w)
        for i ← 0 to |v|
            si, 0 ← 0
        for j ← 0 to |w| 
            s0, j ← 0
        for i ← 1 to |v|
            for j ← 1 to |w|
                si, j ← max{si-1, j , si,j-1 , si-1, j-1 + 1 (if vi = wj)}
                if si,j = si-1,j
                    Backtracki, j ← "↓"
                else if si, j = si, j-1
                    Backtracki, j ← "→"
                else if si, j = si-1, j-1 + 1 and vi = wj
                    Backtracki, j ← "↘"
        return Backtrack

    OutputLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return
        if backtracki, j = "↓"
            OutputLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "→"
            OutputLCS(backtrack, v, i, j - 1)
        else
            OutputLCS(backtrack, v, i - 1, j - 1)
            output vi
'''



def LCSBackTrack(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    s = np.matrix(np.zeros((n+1)*(m+1), dtype=int).reshape((n+1, m+1)))  # Use int instead of np.int
    backtrack = np.matrix(np.zeros((n+1)*(m+1), dtype=int).reshape((n+1, m+1)))  # Use int instead of np.int

    for i in range(1, n+1):
        for j in range(1, m+1):
            if seq1[i-1] == seq2[j-1]:
                s[i, j] = s[i-1, j-1] + 1
                backtrack[i, j] = 1  # Diagonal (↖)
            elif s[i-1, j] >= s[i, j-1]:
                s[i, j] = s[i-1, j]
                backtrack[i, j] = 2  # Up (↑)
            else:
                s[i, j] = s[i, j-1]
                backtrack[i, j] = 3  # Left (←)

    return backtrack


def OutputLCS( backtrack, v, i, j):
    while i > 0 and j > 0:
        if 1 == backtrack[i, j]:
            i -= 1
            continue
        elif 2 == backtrack[i, j]:
            j -= 1
            continue
        else:
            i -= 1
            j -= 1
            lcs = v[i] + lcs

def OutputLCS0( backtrack, v, i, j):
    if 0 == i or 0 == j:
        return
    if 1 == backtrack[i, j]:
        OutputLCS(backtrack, v, i-1, j)
    elif 2 == backtrack[i, j]:
        OutputLCS(backtrack, v, i, j-1)
    else:
        OutputLCS(backtrack, v, i-1, j-1)
        lcs += v[i-1]


seq1="AACCTTGG"
i=len(seq1)
seq2="ACACTGTGA"
j=len(seq2)
back= LCSBackTrack( seq1, seq2)
print(OutputLCS0( back, seq1, i, j))
