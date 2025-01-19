class DistanceBetweenLeaves:
    def __init__(self, filename):
        n, adjDict = self._input(filename)
        distMatrix = self.calculateDistMatrix(n, adjDict)
        self.printDistMatrix(distMatrix)

    def _input(self, filename):
        with open(filename, 'r') as f:
            data = f.read().strip().splitlines()
        n = int(data[0])
        adjDict = dict()
        for line in data[1:]:
            d = line.split('->')
            d1 = d[1].split(':')
            if int(d[0]) not in adjDict:
                adjDict[int(d[0])] = []
            adjDict[int(d[0])].append((int(d1[0]), int(d1[1])))
        return n, adjDict

    def printDistMatrix(self, distMatrix):
        for row in distMatrix:
            print(' '.join(map(str, row)))

    def calculateDistMatrix(self, n, adjDict):
        distMatrix = [[0] * n for _ in range(n)]

        def bfs(start):
            dist = {start: 0}
            queue = [start]
            while queue:
                currNode = queue.pop(0)
                for neighbor, weight in adjDict.get(currNode, []):
                    if neighbor not in dist:
                        dist[neighbor] = dist[currNode] + weight
                        if neighbor < n:  # Fill only for leaves
                            distMatrix[start][neighbor] = dist[neighbor]
                        queue.append(neighbor)

        for i in range(n):
            bfs(i)
        
        return distMatrix

if __name__ == "__main__":
    # Specify the input file name here
    input_filename = 'input.txt'
    DistanceBetweenLeaves(input_filename)
