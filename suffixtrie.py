class Node:
    def __init__(self):
        self.children = {}
        self.start = -1
        self.end = -1

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = Node()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        for i in range(len(self.text)):
            current_node = self.root
            suffix = self.text[i:]
            j = i
            while j < len(self.text):
                char = self.text[j]
                if char in current_node.children:
                    child = current_node.children[char]
                    label = self.text[child.start:child.end]
                    k = 0
                    # Find the common prefix between the edge label and the suffix
                    while k < len(label) and j < len(self.text) and label[k] == self.text[j]:
                        k += 1
                        j += 1
                    if k == len(label):
                        # Complete match, move to the next node
                        current_node = child
                    else:
                        # Partial match, need to split the edge
                        mid_node = Node()
                        mid_node.start = child.start
                        mid_node.end = child.start + k

                        # Adjust the existing child
                        child.start += k
                        mid_node.children[self.text[child.start]] = child

                        # Create a new leaf for the new part of the suffix
                        new_leaf = Node()
                        new_leaf.start = j
                        new_leaf.end = len(self.text)

                        # Attach the new nodes
                        mid_node.children[self.text[j]] = new_leaf
                        current_node.children[char] = mid_node
                        return
                else:
                    # No match, add a new leaf node
                    new_leaf = Node()
                    new_leaf.start = j
                    new_leaf.end = len(self.text)
                    current_node.children[char] = new_leaf
                    break

    def get_edge_labels(self):
        labels = []
        self.collect_edge_labels(self.root, labels)
        return labels

    def collect_edge_labels(self, node, labels):
        for child in node.children.values():
            labels.append(self.text[child.start:child.end])
            self.collect_edge_labels(child, labels)

def suffix_tree_construction(text):
    tree = SuffixTree(text)
    return ' '.join(tree.get_edge_labels())

# Example usage:
text = "panamabananas$"
print(suffix_tree_construction(text))
