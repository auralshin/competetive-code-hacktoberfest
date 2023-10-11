# Currently, Trie supports lowercase English characters. So, the character size is 26.
CHAR_SIZE = 26
 
 
# A class to store a Trie node
class Node:
    next = [None] * CHAR_SIZE
    exist = False       # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insertTrie(head, s):
 
    # start from the root node
    node = head
 
    # do for each character in the string
    for c in s:
 
        index = ord(c) - ord('a')
 
        # create a new node if the path doesn't exist
        if node.next[index] is None:
            node.next[index] = Node()
 
        # go to the next node
        node = node.next[index]
 
    # mark the last node as a leaf
    node.exist = True
 
 
# Function to determine if a string can be segmented into space-separated
# sequence of one or more dictionary words
def wordBreak(head, s):
 
    # get the length of the string
    n = len(s)
 
    # `good[i]` is true if the first `i` characters of `s` can be segmented
    good = [None] * (n + 1)
    good[0] = True      # base case
 
    for i in range(n):
        if good[i]:
            node = head
            for j in range(i, n):
                if node is None:
                    break
 
                index = ord(s[j]) - ord('a')
                node = node.next[index]
 
                # we can make [0, i] using our known decomposition
                # and [i+1, j] using this string in a Trie
                if node and node.exist:
                    good[j + 1] = True
 
    # `good[n]` would be true if all characters of `s` can be segmented
    return good[n]
 
 
if __name__ == '__main__':
 
    # List of strings to represent a dictionary
    words = [
        'self', 'th', 'is', 'famous', 'word', 'break', 'b', 'r',
        'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'prob', 'lem'
    ]
 
    # given string
    s = 'wordbreakproblem'
 
    # create a Trie to store the dictionary
    t = Node()
    for word in words:
        insertTrie(t, word)
 
    # check if the string can be segmented or not
    if wordBreak(t, s):
        print('The string can be segmented')
    else:
        print('The string can\'t be segmented')
