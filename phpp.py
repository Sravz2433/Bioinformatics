class ProbHiddenPath:

    def __init__(self):
        path, transition = self.read_from_file(r'D:\resum\input.txt')
        probability = self.calculate_probability(path, transition)
        self.write_result(probability, 'result.txt')

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read().strip().split('\n')
        
        # Path is on the first line
        path = data[0].strip()
        
        # The states are on the third line
        states = data[2].split()
        
        # The transition matrix is given after the "--------"
        transition = {}
        for i in range(4, len(data)):
            line = data[i].split()
            state_from = line[0]
            transition[state_from] = {states[j]: float(line[j+1]) for j in range(len(states))}
        
        return path, transition

    def calculateProb(self, path, transition):
        # Start with a probability of 0.5 as per the assumption
        P = 0.5

        # Multiply by transition probabilities for consecutive states
        for i in range(len(path) - 1):
            P *= transition[path[i]][path[i + 1]]
        
        return P

if __name__ == '__main__':
    ProbHiddenPath()
