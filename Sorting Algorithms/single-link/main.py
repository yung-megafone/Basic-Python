## First we must create a node with data and reference values
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None


        ##  linked list traversal  ##
    def print_LL(self):
        if self.head is None: # if n becomes None, there are no more items in the list. stop the process
            print("List is empty\n")
        else:
            n = self.head
            while n is not None:  # as long as the next node does not point to null, continue
                print(n.data, "--->",end=" ") # the data in the node, the extra stuff will display the 'link' persay
                n = n.ref   # reference to the next node

    ### Addding a new node to the front of a linked list
    def add_begin(self, data):
        new_node = Node(data)  # create a new node "new_node" and set the data feild to whatever data is to be stored

            ### "head" points to what is currently the first node in the list. 
            ### When you make a new node, you are moving the first node into the second node space in the list.
            ### To link the new first node to the new second node, you must set the reference equal to what is currently the head (what is currently the first node).
            ### Basically, the head points to what will now be the 2nd item in the list
            ### Each node contains a reference to the next node
            ### This is so confusing on paper but once the concept makes sense, it sticks like superglue

        new_node.ref = self.head # the reference for the new node will be equal to self.head because "head" currently points to the first node in the list
        self.head = new_node    # the reference to the newly created node will be stored as "new_node"

    ### Adding a new node to the end of a linked list
    def add_end(self, data):
        new_node = Node(data)   # to create the new node, we use the node class... same as above  [data|none]

        if self.head is None:   # check if the linked list is empty by checking if the head points to None (an empty list has null entries thus None is the default head)
            head = new_node # set the head to the 'new_node
           

                ### we're trying to find the end of the list so we will constantly reassign the value until we get 'n.ref = None'
                ### which will tell us that we have reached the final entry in the linked list... i am horrendus at explaining stuff
            
        else:
            n = self.head   # the first node's location in the list is set as n
            while n.ref is not None:  # if the 'n' reference points to the last node then 'n' should equal 'None'. We are at the end of the list
                n = n.ref   # n was initially 'self.head' and the value is copied to 'n.ref'

            n.ref = new_node  # we change the reference of the last node to point to that of the new node






LL1 = LinkedList() # set variable LL1 to the 'linkedList' object so that we can call it


LL1.add_begin('I\'m last!') # we can add text to the data in the list

LL1.add_begin(12)   # or we can just add an integer | send it to the beginning

LL1.add_end('add me to the very end of the list please')  # this one will be added to the end of the list because he uses add_end rather than add_begin

LL1.add_begin('20, I\'m first!')    # remember, these are being added to the begining so you should see '20' as the most recent entry and '10' as the last


###############
LL1.print_LL()# EXECUTION!!!!!!!!!!!!!!!! i should take a break eh?
###############