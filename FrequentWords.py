def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count

def FrequentWords(Text, k):
    FrequentPatterns = set()
    Count = []
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        Count.append(PatternCount(Text, Pattern))
    maxCount = max(Count)
    for i in range(len(Text) - k + 1):
        if Count[i] == maxCount:
            FrequentPatterns.add(Text[i:i + k])
    return FrequentPatterns

# Read text from file
with open("C:/Users/sravy/Downloads/dataset_30272_13 (4).txt", 'r') as file:
    text = file.read()

k = 13
print(FrequentWords(text, k))
