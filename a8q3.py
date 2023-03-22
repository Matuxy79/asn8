#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

class node(object):

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.__data = data
        self.__next = next


    def get_data(self):
        """
        Retrieve the contents of the data field.
        Return
            the data value stored previously in the node
        """
        return self.__data


    def get_next(self):
        """
        Retrieve the contents of the next field.
        Return
            the value stored previously in the next field
        """
        return self.__next


    def set_data(self, val):
        """
        Set the contents of the data field to val.
        Pre-conditions:
            val:  a data value to be stored
        Post-conditions:
            stores a new data value, replacing  existing value
        Return
            none
        """
        self.__data = val


    def set_next(self, val):
        """
        Set the contents of the next field to val.
        Pre-conditions:
            val:  a node, or the value None
        Post-conditions:
            stores a new next value, replacing existing value
        Return
            none
        """
        self.__next = val
    
    def to_string(node_chain):
        if node_chain is None:
            return "EMPTY"
        elif node_chain._Node__next is None:
            return f"[ {node_chain._Node__data} | / ]"
        else:
            return f"[ {node_chain._Node__data} | * ]-->{to_string(node_chain._Node__next)}"
        
    def copy(node_chain):
        if node_chain is None:
            return None
        else:
            new_node = node(node_chain._Node__data)
            new_node._Node__next = copy(node_chain._Node__next)
            return new_node
   
    def replace(node_chain, target, replacement):
        if node_chain is None:
            return None
        else:
            if node_chain[0] == target:
                node_chain[0] = replacement
            next_node = node_chain[1]
            replace(next_node, target, replacement)
            return node_chain
