#username - baselarw
#id1      - 208215673
#name1    - basel erw
#id2      - 212024442
#name2    - gaaidaa haj



def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.value) if bykey else str(t.value)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.rank = 0
		self.size=0

	def setRank(self,rank):
		self.rank=rank
	def getRank(self):
		return self.rank
	def setSize(self,s):
		self.size=s
	def getSize_node(self):
		return self.size


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.right



	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left=node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right=node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent=node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value=value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height=h
		return None

	

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if(self==None) :
			return False
		return True


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None

		# add your fields here
	def setRoot(self,node):
		self.root=node
	def getRoot(self):
		return  self.root
	def getSize(self):
		return self.size
	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.root==None

	def getRank(self,v):
		counter = 0
		current = self.root
		while current is not None and not (current.value == v):
			if current.value> v :
				current = current.left
			else:
				counter += current.getsize(current.left) + 1
				current = current.right
		if current is not None:
			counter += current.getsize(current.left) + 1
			current.setRank(counter)
		current.setRank(counter)

	def findRank(self,i):                        ## return the node of rank i
		current = self.root
		while(current.getRank() != i):
			if(i>current.getRank()):
				current=current.right
			else:
				current=current.left
		return current





	def getsize(self):
		if self.root is None : return 0
		return self.root.size

	def calcSize(self):
		def size_rec(node1):
			if node1==None:
				return 0
			else:
				s1 = 1+ size_rec(node1.left)+size_rec(node1.right)
				node1.setSize(s1)
				return s1
		s = size_rec(self.root)
		self.size=s
		self.root.setSize(s)




	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

	def retrieveRec(self, i):
		if(self.root.getRank==i) : return self.root.value
		if(self.root.getRank>i)  : return self.root.left.retrieveRec(i)
		return self.root.right.retrieveRec(i)
	def retrieve(self, i):

		return self.retrieveRec(i+1)




	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		if(self.root==None):
			self.root=AVLNode(val)
			self.size=1
			return
		current = self.root
		if(i==self.size):
			maxNode=self.maxNode(current)
			print(id(maxNode))
			s=AVLNode(val)
			s.setParent(maxNode)
			maxNode.setRight(s)
		elif (i<self.size):
			nodeRank = self.findRank(i+1)
			if(nodeRank.left == None):
				s = AVLNode(val)
				s.setParent(nodeRank)
				nodeRank.setLeft(s)
			else:
				p = nodeRank.predecessor()
				s = AVLNode(val)
				s.setParent(nodeRank)
				p.setRight(s)
		size=self.calcSize()
		self.root.setSize(size)
		return


	""" rotate Left and Right 
	"""
	def rotateLeft(self,A):
		tmp=A.getParent()
		B = A.getRight()
		left_B = B.getLeft()
		B.setLeft(A)
		A.setParent(B)
		A.setRight(left_B)
		if(self.root==B):
		 	B.setParent(None)
		else:
		 	B.setParent(tmp)
		self.setRoot(B)
		return

	def rotateRight(self,A):
		B = A.getParent()
		right_A = A.getRight()
		A.setRight(B)
		B.setLeft(right_A)
		tmp=B.getParent()
		if(self.root == A):
			A.setParent(None)
		else:
			A.setParent(tmp)
		B.setParent(A)
		self.setRoot(A)
		return
		

	"""predecessor and successor
	"""
	def predecessor(self,node):
		x=node
		if(x.left!=None):
			return x.left.maxNode()
		y=self.parent
		while(y!=None and x==y.left):
			x=y
			y=x.parent
		return y 

	def successor(self,node):
		x=node
		if x.right != None:
			return x.right.minNode()
		y=self.parent
		while(y!=None and x == y.right):
			x=y
			y=x.parent
		return y

	"""min and max node
	"""
	def minNode(self,node):
		if node==None: return None
		current = node
		while(current.left!=None):
			current=current.left
		return current

	def maxNode(self,node):
		if node==None: return None
		current=node
		while(current.right!=None):
			current=current.right
		return current



	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1

	def __repr__(self):  # no need to understand the implementation of this one
		out = ""
		for row in printree(self.root):  # need printree.py file
			out = out + row + "\n"
		return out

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root







import sys




tree1=AVLTreeList()
tree1.insert(0,6)
tree1.insert(1,7)
tree1.insert(2,8)
tree1.insert(3,5)
tree1.insert(4,9)
print(tree1)
tree1.rotateLeft(tree1.getRoot().getRight())
print(tree1)
tree1.rotateLeft(tree1.getRoot())
print(tree1)
print("User Current Version:-", sys.version)

print("hi")
print("hi11")
print("tagroba")
print("tagroba111")
