#username - baselarw
#id1      - 208215673
#name1    - basel erw
#id2      - 212024442
#name2    - gaaidaa haj
import random


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
        return ["-"]

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
		self.size=0

	def setSize_node(self,s):
		self.size=s
	def getSize_node(self):
		if self is None: return 0
		return self.size

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		if self==None : return None
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
		if self is None: return None
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
		if self is None : return -1
		return self.height

	"""sets left child
	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		if self == None : return
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
	def getBF(self):
		if(not self.isRealNode()): return 0
		if(not AVLNode.isRealNode(self.getLeft()) and not AVLNode.isRealNode(self.getRight())): return 0
		right_H = -1
		left_H = -1
		if(AVLNode.isRealNode(self.getLeft())):
			left_H= self.getLeft().getHeight()
		if (AVLNode.isRealNode(self.getRight())):
			right_H= self.getRight().getHeight()
		return left_H-right_H

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
		self.start=None
		self.end=None

		# add your fields here
	def setRoot(self,node):   #O(1)
		self.root=node
	def getRoot(self):   #O(1)
		return  self.root

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):     #O(1)
		return self.root==None

	def getSize(self):     #O(1)
		if self.root is None : return 0
		return self.size
	def setSize(self,i):
		self.size=i

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):       #O(log(n))
		x=self.Tree_Select(i+1)
		if(not x.isRealNode):
			return None
		return x.getValue()

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
			self.setSize(1)
			self.getRoot().setSize_node(1)
			self.end=self.getRoot()
			self.start=self.getRoot()
			self.getRoot().setHeight(0)
			return

		current = self.root
		s = AVLNode(val)
		if(i==self.size):
			maxNode=self.maxNode(current)
			s.setParent(maxNode)
			maxNode.setRight(s)
			s.setSize_node(1)
		elif (i<self.size):
			nodeSelect= self.Tree_Select(i+1)
			if(nodeSelect.left == None):
				s.setParent(nodeSelect)
				nodeSelect.setLeft(s)
				s.setSize_node(1)

			else:
				p = self.predecessor(nodeSelect)
				s.setParent(p)
				p.setRight(s)
			if(i==0):
				self.start = s

		self.setSize(1+self.getSize())
		s.setHeight(0)
		self.fix_the_Hights(s)
		self.fix_the_tree(s)
		self.fix_sizes(s)


		return


	def fix_the_Hights(self,node):
		parent=node.getParent()
		while(parent !=None):
			parent.setHeight(1+max(AVLNode.getHeight(parent.getRight()),AVLNode.getHeight(parent.getLeft())))
			parent=parent.getParent()



	def fix_sizes(self, node):
		parent=node.getParent()
		while(parent!=None):
			parent.setSize_node(parent.getSize_node()+1)
			parent=parent.getParent()
	def fix_the_tree(self,node):
		y=node.getParent()
		while(y!=None):
			Bf=y.getBF()
			if((Bf==1 or Bf==0 or  Bf==-1 ) and AVLNode.getHeight(y.getLeft())==AVLNode.getHeight(y.getRight())):
				return
			if((Bf==1 or Bf==0 or Bf==-1) and  AVLNode.getHeight(y.getLeft())!=AVLNode.getHeight(y.getRight())):
				y=y.getParent()
				continue


			if(Bf==2):
				node = y.getLeft()
				if(node.getBF()==1):self.rotateRight(node)
				if (node.getBF() == -1):
					self.rotateLeft(y)
					self.rotateRight(y)
				y = y.getParent()
				node.setHeight(AVLTreeList.calcHieght(self,node))
				self.fix_the_Hights(node)
				return
			if (Bf==-2):
				node=y.getRight()
				if(node.getBF()==1):
					self.rotateRight(y)
					self.rotateLeft(y)
				if (node.getBF() == -1):
					self.rotateLeft(y)
				y = y.getParent()
				node.setHeight(AVLTreeList.calcHieght(self,node))
				self.fix_the_Hights(node)
				return
	def calcHieght(self,node):
		if node == None: return -1
		if node.getRight()==None and node.getLeft()==None:return 0
		return (1+max(self.calcHieght(node.getLeft()),self.calcHieght(node.getRight())))






	""" rotate Left and Right 
	"""
	def rotateLeft(self,A):      #O(1)
		tmp=AVLNode.getParent(A)
		B = AVLNode.getRight(A)
		left_B = AVLNode.getLeft(B)
		AVLNode.setLeft(B,A)
		A.setParent(B)
		A.setRight(left_B)
		if(AVLNode.getParent(B)==None):
			self.setRoot(B)

		B.setParent(tmp)
		if(A==self.getRoot()):self.setRoot(B)
		A.setHeight(self.calcHieght(A))
		B.setHeight(self.calcHieght(B))
		self.fix_the_Hights(A)
		self.fix_sizes(A)
		return

	def rotateRight(self,A):  #O(1)
		B = A.getParent()
		right_A = A.getRight()
		A.setRight(B)
		B.setLeft(right_A)
		tmp=B.getParent()
		if(AVLNode.getParent(A)==None or self.getRoot()==B):
			self.setRoot(A)
		parentB=B.getParent()
		if parentB is not None:
			if(parentB.getRight==B):
				parentB.setRight(A)
			else:
				parentB.setLeft(A)
		A.setParent(tmp)
		B.setParent(A)
		A.setHeight(self.calcHieght(A))
		B.setHeight(self.calcHieght(B))
		self.fix_sizes(A)
		self.fix_the_Hights(A)
		return


	# Tree_Select return the k-th element in the tree
	def Tree_Select(self,k):     #O(log(n))
		def Tree_Select_rec(node, k):
			x = node
			r = AVLNode.getSize_node(x.getLeft()) + 1
			if k==r:
				return x
			elif (k<r):
				return Tree_Select_rec(node.getLeft(),k)
			else:
				return Tree_Select_rec(node.getRight(),k-r)
		return Tree_Select_rec(self.root, k)

	"""predecessor and successor
	"""
	def predecessor(self,node):     #O(log(n))
		x=node
		if(x.left!=None):
			return self.maxNode(x.left)
		y=node.parent
		while(y!=None and x==y.left):
			x=y
			y=x.parent
		return y 

	def successor(self,node):     #O(log(n))
		x=node
		if x.right != None:
			return self.minNode(x.right)
		y=node.parent
		while(y!=None and x == y.right):
			x=y
			y=x.parent
		return y

	"""min and max node
	"""
	def minNode(self,node):     #O(log(n))
		if( not AVLNode.isRealNode(node)): return None
		left=node.getLeft()
		if left is None : return  node
		while(AVLNode.isRealNode(left.getLeft())):
			left=left.getLeft()
		return left


		return
	def maxNode(self,node): #O(log(n))
		if( not AVLNode.isRealNode(node)): return None
		right=node.getRight()
		if(right is None): return node
		while(AVLNode.isRealNode(right.getRight())):
			right=right.getRight()
		return right


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
	def first(self):      #O(1)
		if self.empty(): return None
		return self.start
	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):      #O(1)
		if self.empty(): return None
		return self.end

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):    #O(n)
		if(self.empty()):
			return []
		else:
			return self.listToArray_rec(self.root)

	def listToArray_rec(node):      #O(n)
		if (node == None):
			return []
		else:
			arr = []
			left = AVLTreeList.listToArray_rec(node.getLeft())
			right = AVLTreeList.listToArray_rec(node.getRight())
			arr = left + [node.value] + right
			return arr



	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):    #O(1)
		return self.size

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self): #O(n)
		if self.empty(): return  None
		arr= self.listToArray()
		arr.sort()
		i=0
		sorted_tree=AVLTreeList()
		for i in range(len(arr)):
			sorted_tree.insert(i,arr[i])
		return sorted_tree


	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):   #O(n)
		arr = self.listToArray()
		result = []
		while(len(arr)!=0):
			random = random.randrange(0,len(arr));
			if(random<len(arr)):
				result+=arr[random]
				arr.pop(random)

		tree= AVLTreeList()
		i=0
		while(i<len(result)):
			tree.insert(i,result[i])
			i=i+1
		return tree

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
	def search(self, val):  # O(n)
		arr=self.listToArray()
		for i in range(len(arr)):
			if arr[i]==val:
				return i
		return -1



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

	def getRoot(self):  #O(1)
		if self.empty() : return None
		return self.root








tree1=AVLTreeList()
tree1.insert(0,6)
tree1.insert(1,7)
tree1.insert(2,8)
tree1.insert(0,0)
tree1.insert(0,11)
tree1.insert(1,4)
tree1.insert(1,67)
print(tree1.getRoot().getLeft().getBF())




print(tree1)
