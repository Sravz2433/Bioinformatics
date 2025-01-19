# python3

import sys
import queue
import numpy as np
from copy import deepcopy

'''
Given a spectral vector Spectrum', our goal is to find a peptide Peptide maximizing Score(Peptide, Spectrum'). Since the mass 
of a peptide and the parent mass of the spectrum that it generates should be the same, a peptide vector should have the same 
length as the spectral vector under consideration. We will therefore define the score between a peptide vector and a spectral 
vector of different length as −∞.

Peptide Sequencing Problem: Given a spectral vector, find a peptide with maximum score against this spectrum.
     Input: A spectral vector Spectrum'.
     Output: An amino acid string Peptide that maximizes Score(Peptide', Spectrum') among all possible amino acid strings.

Given a spectral vector Spectrum' = (s1, . . . , sm), we will construct a DAG on m + 1 nodes, labeled with the integers from 
0 (source) to m (sink), and then connect node i to node j by a directed edge if j − i is equal to the mass of an amino acid. 
We will further assign weight si to node i (for 1 ≤ i ≤ m) and assign weight zero to node 0.

Any path connecting source to sink in this DAG corresponds to an amino acid string Peptide, and the total weight of nodes on 
this path is equal to Score(Peptide', Spectrum'). We have therefore reduced the Peptide Sequencing Problem to the problem of 
finding a maximum-weight path from source to sink in a node-weighted DAG.

Solve the Peptide Sequencing Problem.
     Given: A space-delimited spectral vector Spectrum'.
     Return: An amino acid string with maximum score against Spectrum'. For masses
     with more than one amino acid, any choice may be used.

Note: When a spectral vector Spectrum' = s1 ... sm is given, it does not have a zero-th element; in your implementations, you 
should assume that s0 is equal to zero.

Sample Input:
0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8
Sample Output:
XZZXX

Input
20 2 -14 -4 -10 -4 5 16 20 -12 -1 -9 11 -11 12 3 -1 0 3 21 3 -2 10 11 -11 15 17 2 4 8 -19 28 28 29 1 21 27 -15 25 -15 10 10 26 -9 -13 7 -6 9 27 -3 2 -12 0 20 26 -14 15 29 10 30 -17 25 21 -6 26 25 24 6 9 29 -13 27 16 -5 27 25 -3 -20 3 12 27 5 29 3 -13 9 6 12 14 -14 -17 -8 -13 17 6 20 0 -20 -7 -4 -12 18 7 11 3 -8 23 0 -6 27 6 -20 6 1 15 -14 -20 -3 22 -13 6 10 10 -18 -6 -1 -14 8 16 -4 -12 -12 -11 30 11 -4 -11 10 -15 23 -19 27 -17 -3 -3 13 12 -19 5 22 -8 19 21 -6 21 -20 -6 4 -20 -5 17 0 2 13 24 22 6 20 -3 17 -12 24 -18 5 -12 -9 -17 17 -3 29 9 -12 1 -17 -4 8 2 17 -20 28 -15 -11 26 16 19 4 23 -18 22 -15 1 16 14 30 3 12 -5 27 14 -5 29 5 13 16 -3 4 -9 -20 11 11 12 13 2 13 -2 -15 3 4 -20 28 -8 4 28 5 28 16 -3 3 19 17 6 -5 6 -15 6 15 -8 29 22 -3 -5 -5 16 24 14 26 -19 13 -17 22 16 -20 -7 14 -11 -10 -19 30 14 28 20 14 12 -11 -19 -4 -19 -20 22 2 -5 9 -10 -4 -12 15 8 22 27 5 9 18 -13 27 27 -12 8 28 29 -12 -9 29 -15 -7 7 18 -6 -4 -15 -11 23 25 27 -8 3 22 29 7 16 -8 11 -17 -9 5 22 4 -17 7 -18 2 0 -8 2 0 3 -6 23 -3 -17 21 9 -6 7 3 20 9 24 -11 21 1 25 30 -17 -11 12 -13 8 7 -12 -17 0 -1 19 20 -11 13 -6 -14 6 -4 27 6 -18 -4 21 20 -11 21 16 -15 2 -8 8 24 24 -15 -12 -5 -20 -15 27 29 25 -19 -20 14 -16 7 18 -15 25 11 -12 -5 1 -4 12 14 -3 -11 14 -14 25 4 21 -2 -1 -17 23 -3 -9 19 26 8 -18 2 3 20 19 -15 -20 3 26 -3 11 -14 8 25 -16 8 8 2 23 29 -10 28 -16 13 -1 11 22 -20 8 18 2 -16 -17 18 30 0 -19 23 -6 -10 11 24 16 27 19 -16 -17 -9 -8 -5 1 5 0 15 9 24 10 18 10 -7 -9 12 10 21 27 -10 4 -13 -17 -1 3 -17 0 -7 -20 20 29 -13 -11 -4 -12 11 3 25 26 20 27 14 29 17 19 -2 8 17 -8 -8 14 -15 -5 0 23 0 23 22 24 13 1 25 -17 -16 7 18 4 24 -9 10 -12 17 8 28 3 29 -2 26 -8 -3 22 23 -19 1 18 -8 -4 21 29 29 6 -5 5 24 -9 -12 -9 -10 3 5 0 -7 23 22 13 11 16 -20 28 -8 -17 -3 13 13 24 8 13 14 6 -5 -3 20 24 -19 14 -9 -6 16 3 28 -20 -18 11 -18 15 7 29 5 11 -14 21 6 16 -4 16 -10 -17 7 10 2 25 -16 1 16 -19 20 5 1 -3 5 11 21 21 -1 6 -11 -7 28 -8 8 -10 3 24 -9 -4 21 -6 1 -1 11 -13 -12 20 20 -13 -14 -20 -19 26 15 -16 -5 -9 10 4 5 -10 23 14 22 9 -16 16 21 9 15 3 30 6 8 22 25 24 22 1 -16 -3 19 6 -4 -7 -6 25 -13 13 15 21 10 30 -12 19 -1 -2 -19 14 29 -16 12 -17 -8 -12 5 8 25 18 22 7 14 13 25 -20
Output
GGPGGPGGAGG
'''

class PeptideSequencing:
    def __init__(self):
        massDict, aaDict = self.AminoAcidMassDict()
        spectralVector = self.readFromFile()
        peptide = self.findPeptide(spectralVector, massDict)
        print(peptide)
        f = open('result.txt', 'w')
        f.write(peptide)
        f.close()
        
    def AminoAcidMassDict(self):
        massTable = '''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186'''
        mass = massTable.split()
        return {int(mass[i+1]):mass[i] for i in range(0, len(mass), 2)}, {mass[i]:int(mass[i+1]) for i in range(0, len(mass), 2)}
    
    def _input(self):
        data = sys.stdin.read().strip().split()
        spectralVector = list(map(int, data))
        spectralVector.insert(0, 0)
        return spectralVector
    
    def readFromFile(self):
        f = open('input.txt', 'r')
        for line in f:
            data = line.strip().split()
        spectralVector = list(map(int, data))
        spectralVector.insert(0, 0)
        return spectralVector
    
    def findPeptide(self, spectralVector, massDict):
        l = len(spectralVector)
        adj = [[] for _ in range(l)]
        for i in range(l):
            for j in range(i, l):
                if j-i in massDict:
                    adj[i].append(j)
        
        # Bellman-Ford algorithm
        dist = [-np.inf] * l
        parent = [None] * l
        dist[0] = 0
        updated = True
        for i in range(l-1):
            if not updated:
                break
            updated = False
            for u in range(l):
                for v in adj[u]:
                    if dist[u] + spectralVector[v] > dist[v]:
                        dist[v] = dist[u] + spectralVector[v]
                        parent[v] = u
                        updated = True
        u = l-1
        path = [u]
        while 0 != u:
            u = parent[u]
            path.insert(0, u)

        peptide = ''.join([massDict[path[i+1]-path[i]] for i in range(len(path)-1)])
        return peptide

if __name__ == "__main__":
    PeptideSequencing()