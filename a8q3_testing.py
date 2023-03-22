#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

from a8q3 import node

#testing for to_string

# Test empty chain
empty_chain = None
print(to_string(empty_chain))  # Should print "EMPTY"

# Test chain with one node
single_node_chain = node(1)
print(to_string(single_node_chain))  # Should print "[ 1 | / ]"

# Test chain with several nodes
multiple_node_chain = node(1, node(2, node(3)))
print(to_string(multiple_node_chain))  # Should print "[ 1 | * ]-->[ 2 | * ]-->[ 3 | / ]"

#testing for copy

# empty chain
node1 = None
node2 = copy(node1)
print(node1) # should print None
print(node2) # should print None

# chain with one node
node1 = [1, None]
node2 = copy(node1)
node1[0] = 2
print(node1) # should print [2, None]
print(node2) # should print [1, None]

# chain with several nodes
node1 = [1, [2, [3, None]]]
node2 = copy(node1)
node1[0] = 2
print(node1) # should print [2, [2, [3, None]]]
print(node2) # should print [1, [2, [3, None]]]

#testing for replace

# empty chain
node1 = None
replace(node1, 1, 2)
print(node1) # should print None

# chain with no replacements
node1 = [1, [2, [3, None]]]
replace(node1, 4, 5)
print(node1) # should print [1, [2, [3, None]]]

# chain with several replacements
node1 = [1, [2, [3, None]]]
replace(node1, 2, 4)
print(node1) # should print [1, [4, [3, None]]]


