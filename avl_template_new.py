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
		self.height = 0
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
		if self==None:
			return None
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
		if self==None:
			return None
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
		if(self==None or self.height==-1) :
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


	""" returns virtual node
		@param: right is boolean
		@param: right is default
	"""
	def virtual_node(self):
		self.size = 0
		self.height = -1

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
		if(not x.isRealNode()):
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
		virtualNode_right = AVLNode("Virtual")
		virtualNode_left = AVLNode("Virtual")
		current = self.root
		s = AVLNode(val)
		virtualNode_right.virtual_node()
		virtualNode_left.virtual_node()
		s.setLeft(virtualNode_left)
		s.setRight(virtualNode_right)
		if(self.root==None):
			self.root=s
			self.setSize(1)
			self.getRoot().setSize_node(1)
			self.end=self.getRoot()
			self.start=self.getRoot()
			self.getRoot().setHeight(0)
			return 0


		if(i==self.size):
			self.end=s
			maxNode=self.maxNode(current)
			s.setParent(maxNode)
			maxNode.setRight(s)
			s.setSize_node(1)
		elif (i<self.size):
			nodeSelect= self.Tree_Select(i+1)
			if(not AVLNode.isRealNode(nodeSelect.getLeft())):
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
		self.fix_the_Hights(s,True)
		number_of_rotations=self.fix_the_tree(s)
		self.fix_the_Hights(s,True)
		self.fix_sizes(s,True)
		return (number_of_rotations)


	def fix_the_Hights(self,node,insertion):
		parent=AVLNode.getParent(node)
		while(parent !=None):
			parent.setHeight(1+max(AVLNode.getHeight(parent.getRight()),AVLNode.getHeight(parent.getLeft())))
			parent=parent.getParent()



	def fix_sizes(self, node,insertion):
		parent=AVLNode.getParent(node)
		if(parent!=None):
			if(AVLNode.getLeft(parent).isRealNode() and parent.getLeft()!=None):
				parent.getLeft().setSize_node(AVLNode.getSize_node(parent.getLeft().getLeft())+AVLNode.getSize_node(parent.getLeft().getRight())+1)
		if(parent!=None):
			if (AVLNode.getRight(parent).isRealNode() and parent.getRight() != None):
				parent.getRight().setSize_node(parent.getRight().getLeft().getSize_node()+parent.getRight().getRight().getSize_node()+1)

		tmpParent=AVLNode.getParent(parent)
		if(tmpParent!=None):
			if(tmpParent.getLeft().isRealNode()):
				tmpParent.getLeft().setSize_node(tmpParent.getLeft().getLeft().getSize_node()+tmpParent.getLeft().getRight().getSize_node()+1)
			if(tmpParent.getRight().isRealNode()):
				tmpParent.getRight().setSize_node(tmpParent.getRight().getLeft().getSize_node()+tmpParent.getRight().getRight().getSize_node()+1)

		while(parent!=None):
			parent.setSize_node(parent.getLeft().getSize_node()+1+parent.getRight().getSize_node())
			parent=parent.getParent()

	def fix_the_tree(self,node,insert=True):
		counter=0
		y=node.getParent()
		if ((node.getBF() == -2 or node.getBF() == 2)):
			y = node
		while(y!=None):
			Bf=y.getBF()
			if((Bf==1 or Bf==0 or  Bf==-1 ) and AVLNode.getHeight(y.getLeft())==AVLNode.getHeight(y.getRight())):
				if(insert):
					return 0
				else:
					y=y.getParent()
					continue
			if((Bf==1 or Bf==0 or Bf==-1) and  AVLNode.getHeight(y.getLeft())!=AVLNode.getHeight(y.getRight())):
				y=y.getParent()
				continue
			if(Bf==2):
				node = y.getLeft()
				if(node.getBF()==1 or(node.getBF()==0 and not insert)):
					self.rotateRight(y)  ### have/has changed
					counter =counter+1
				elif (node.getBF() == -1):
					self.rotateLeft(node)
					self.rotateRight(y)              # not changed
					counter = counter + 2
				y = y.getParent()
				# node.setHeight(AVLTreeList.fix_the_Hights(self,node))
				# self.fix_the_Hights(node)
				if(insert):
					return counter
				else:continue
			if (Bf==-2):
				node=y.getRight()
				if(node.getBF()==1):
					self.rotateRight(node)       #have/has changed
					self.rotateLeft(y)
					counter = counter + 2
				elif (node.getBF() == -1 or (node.getBF()==0 and not insert)):
					self.rotateLeft(y)
					counter = counter + 1
				y = y.getParent()
				# node.setHeight(AVLTreeList.fix_the_Hights(self,node))
				# self.fix_the_Hights(node)
				# return counter
		return counter









	""" rotate Left and Right 
	"""
	def rotateLeft(self,A):
		A_parent = A.getParent()
		if(A_parent != None):
			bool_right = (A_parent.getRight() == A)
		B = A.getRight()
		B_left = B.getLeft()
		B.setLeft(A)
		A.setParent(B)
		B.setParent(A_parent)
		A.setRight(B_left)
		B_left.setParent(A)

		if(A_parent == None):
			self.root = B
		else:
			if(bool_right):
				A_parent.setRight(B)
			else:
				A_parent.setLeft(B)

		self.fix_after_rotation(A)
		self.fix_after_rotation(B)
		if(A_parent != None):
			self.fix_after_rotation(A_parent)





	def rotateRight(self,B):
		B_parent = B.getParent()
		if(B_parent !=None):
			bool_right = (B_parent.getRight() == B)
		A = B.getLeft()
		A_rightSon =A.getRight()
		A.setRight(B)
		B.setParent(A)
		B.setLeft(A_rightSon)
		A_rightSon.setParent(B)
		A.setParent(B_parent)

		if(B_parent == None):
			self.root = A
		else:
			if(bool_right):
				B_parent.setRight(A)
			else:
				B_parent.setLeft(A)

		self.fix_after_rotation(B)
		self.fix_after_rotation(A)
		if(B_parent != None):
			self.fix_after_rotation(B_parent)


	def fix_after_rotation(self,node):
		node.setHeight(1+max(AVLNode.getHeight(node.getLeft()), AVLNode.getHeight(node.getRight())))
		node.setSize_node(1+AVLNode.getSize_node(node.getLeft()) + AVLNode.getSize_node(node.getRight()))


	"""
	Tree_Select return the k-th element in the tree
	"""
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
		if(x.left.isRealNode()):
			return self.maxNode(x.left)
		y=node.parent
		while(y!=None and x==y.left):
			x=y
			y=x.parent
		return y

	def successor(self,node):     #O(log(n))
		x=node
		if x.right.isRealNode():
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
		if (not left.isRealNode()) : return  node
		while(AVLNode.isRealNode(left.getLeft())):
			left=left.getLeft()
		return left


	def maxNode(self,node): #O(log(n))
		if( not AVLNode.isRealNode(node)): return None
		right=node.getRight()
		if(not right.isRealNode()): return node
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
		rotation=-1
		if(i>=self.size or self.empty()):
			return -1
		else:
			if (self.size == 1 and i==0):
				self.start=None
				self.end=None
			elif(i==0):
				self.start=self.Tree_Select(1)
			elif(i==self.size-1):
				self.end= self.Tree_Select(i)

			curr = self.Tree_Select(i+1)
			#  check if the node that we want to delete is a leaf
			if((not curr.getRight().isRealNode()) and (not curr.getLeft().isRealNode())):
				parent = curr.getParent()
				  #check if we have just one node and we want to delete it
				if(parent == None):
					self.setSize( 0)
					self.setRoot(None)
					return 0
				# else
				virtualNode = AVLNode("Virtual")
				if(parent.getLeft()==curr):
					parent.setLeft(virtualNode)
					parent.setHeight(1+max(parent.getRight().getHeight(),parent.getLeft().getHeight()))
					# parent.setSize_node(parent.getSize_node()-1)
					curr.setParent(None)
				if(parent.getRight()==curr):
					parent.setRight(virtualNode)
					parent.setHeight(1+parent.getLeft().getHeight())
					# parent.setSize_node(parent.setSize_node() - 1)
					curr.setParent(None)
				virtualNode.setParent(parent)
				virtualNode.virtual_node()

				self.fix_the_Hights(virtualNode,False)
				self.fix_sizes(virtualNode,False)
				self.setSize(self.getSize() - 1)
				return ( self.fix_the_tree(virtualNode,False))

			# 	check if the node that we want to delete has one child
			parent = curr.getParent()
			if((not curr.getRight().isRealNode() and curr.getLeft().isRealNode()) or (not curr.getLeft().isRealNode() and curr.getLeft().isRealNode())):
				if(parent == None):
					if(self.getRoot().getRight().isRealNode()):
						right_node = self.getRoot().getRight()
						self.setRoot(right_node)
						right_node.setParent(None)
						self.setSize(1)
						self.getRoot().setSize_node(1)
						self.getRoot().setHeight(0)

						self.start = self.end = self.getRoot()
					else:
						left_node = self.getRoot().getLeft()
						self.setRoot(left_node)
						left_node.setParent(None)
						self.setSize(1)
						self.getRoot().setSize_node(1)
						self.getRoot().setHeight(0)
				else:
					right=parent.getRight()==curr
					if( curr.getLeft().isRealNode()):
						if(right):
							curr.getLeft().setParent(parent)
							parent.setRight(curr.getLeft())

						else:
							curr.getLeft().setParent(parent)
							parent.setLeft(curr.getLeft())
					if ( curr.getRight().isRealNode()):
						if (right):
							curr.getRight().setParent(parent)
							parent.setRight(curr.getRight())

						else:
							curr.getRight().setParent(parent)
							parent.setLeft(curr.getRight())
					parent.setSize_node(parent.getSize_node() - 1)
					parent.setHeight(1 +max( AVLNode.getHeight(parent.getLeft()),AVLNode.getHeight(parent.getRight())))
					# #
					# curr.getLeft().setParent(parent)
					#
					# #
					curr.setParent(None)
					curr.setRight(None)
					curr.setLeft(None)
					self.fix_the_Hights(parent, False)
					self.fix_sizes(parent, False)
					self.setSize(self.getSize() - 1)
					return (self.fix_the_tree(parent,False))
			# if the node that we want to delete have 2 children
			else:
				y=self.successor(curr)      # 		y has no left child
				y_parent = y.getParent()
				left=y.getParent().getLeft()==y
				if(left):
					y.getParent().setLeft(y.getRight())
				else:
					y.getParent().setRight(y.getRight())
				y.getRight().setParent(y.getParent())
				y.getParent().setSize_node(y.getParent().getSize_node() - 1)
				y.getParent().setHeight(1 + max(y.getParent().getLeft().getHeight(), y.getParent().getRight().getHeight()))
				self.fix_the_Hights(AVLNode.getLeft(parent), False)
				self.fix_sizes(AVLNode.getLeft(parent), False)
				y.setParent(None)
				right = AVLNode.getRight(curr.getParent()) == curr
				y.setRight(curr.getRight())
				y.setLeft(curr.getLeft())
				curr.getLeft().setParent(y)
				curr.getRight().setParent(y)
				if(curr==self.getRoot()):
					self.setRoot(y)
				if (right):
					AVLNode.setRight(parent,y)
				else:
					AVLNode.setLeft(parent,y)
				curr.setLeft(None)
				curr.setRight(None)
				curr.setParent(None)
				y.setParent(parent)
				y.setSize_node(y.getLeft().getSize_node()+1+y.getRight().getSize_node())
				y.setHeight(max(y.getLeft().getHeight(),y.getRight().getHeight())+1)
				# y.getParent().setSize_node(y.getParent().getSize_node() - 1)
				y.setHeight(1 + max(y.getLeft().getHeight(), y.getRight().getHeight()))
				if(y_parent == None):
					self.fix_sizes(y, False)
					self.fix_the_Hights(y,False)
					rotation=self.fix_the_tree(y,False)
				else:
					self.fix_sizes(y_parent, False)
					self.fix_the_Hights(y_parent, False)
					rotation = self.fix_the_tree(y_parent, False)
				self.setSize(self.getSize()-1)
		return rotation



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
		return self.start.getValue()
	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):      #O(1)
		if self.empty(): return None
		return self.end.getValue()

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):    #O(n)
		if(self.empty()):
			return []
		else:
			return self.listToArray_rec(self.root)

	def listToArray_rec(self,node):      #O(n)
		if (node == None):
			return []
		else:
			arr = []
			left = self.listToArray_rec(node.getLeft())
			right = self.listToArray_rec(node.getRight())
			if(node.isRealNode()):
				arr = left + [node.getValue()] + right
			else:
				arr=left+right
			return arr



	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):   #O(1)

		if(self.empty()):
			return 0
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
		if(lst.getRoot().getHeight()>=self.getRoot().getHeight()):
			x = self.end
			self.delete(self.size - 1)
			return self.join(x,lst,True)
		else:
			x=lst.start
			lst.delete(0)
			return self.join(x, lst, False)
	def join(self,x,T2,t2IsBigger):
		h=self.getRoot().getHeight()
		start=T2.start
		if(not t2IsBigger):
			h=T2.getRoot().getHeight()
			start=self.end

		while(start.getHeight()<h):
			start=start.getParent()
		if(t2IsBigger):
			x.setLeft(self.getRoot())
			self.getRoot().setParent(x)
			x.setRight(start)
			start.getParent().setLeft(x)
			x.setParent(start.getParent())
			start.setParent(x)
		else:
			x.setLeft(start)
			x.setRight(T2.getRoot())
			T2.getRoot().setParent(x)
			start.getParent().setRight(x)
			x.setParent(start.getParent())
			start.setParent(x)
		x.setSize_node(x.getRight().getSize_node()+1+x.getLeft().getSize_node())
		x.setHeight(1+max(x.getRight().getHeight(),x.getLeft().getHeight()))
		self.setSize(self.getSize()+T2.getSize()+1)
		self.fix_the_Hights(x,False)
		self.fix_the_tree(x,False)
		self.fix_the_Hights(x,False)
		self.fix_sizes(x,False)
		c=x
		while c.getParent()!=None:
			c=c.getParent()
		self.setRoot(c)

		self.end=T2.end
		return
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






tree=AVLTreeList()
tree.insert(0,50000000)
for i in range (1,5):
	tree.insert(i,0)
tree.insert(5,50000000)

tree1=AVLTreeList()
tree1.insert(0,1000000)
for i in range (1,16):
	tree1.insert(i,i)

# tree.concat(tree1)
# tree1.concat(tree)
print(tree)
print(tree1)
tree1.concat(tree)
print(tree1)
# for i in range (tree1.size):
# 	print(tree1.retrieve(i))
# x=3000
# y=0
# sum=0
# tree.insert(4,0)
# for i in range (3000):
# 	rnd=random.randint(0, y);
# 	sum=sum+(tree.insert(rnd,4))
# 	y=y+1
# print(sum)
#
