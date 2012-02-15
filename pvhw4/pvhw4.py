#Peter Vining python assignment 2
#program for linked list


class Node:
	def __init__ (self, _value=None, _next=None):
		self.value = _value
		self.next = _next
	def __str__ (self):
		return str(self.value)

class List:
	def __init__(self):
		self.firstnode=None #define a head node
		self.lastnode=None  #define a tail node
		self.length=0 #start list length at 0
		
	def addNode(self, x):
		if self.firstnode==None:   #If statement to check if first node exists
			self.firstnode=Node(x, None)  #sets first node to x if first node is empty
			self.lastnode=self.firstnode #sets last node to first node for event of 1 element
			self.length+=1
		elif self.lastnode==self.firstnode: #if list has 1 entry
			self.lastnode= Node(x, None) #classify the last node to have no new links after
			self.firstnode.next=self.lastnode #link the first node to the last node
			self.length+=1
		else: #if additional entry is added
			currentval= Node(x, None) #temp variable specified as user input
			self.lastnode.next=currentval #links the previous last node to new current value
			self.lastnode=currentval#reclassifies last node as new current value 
			self.length+=1
					
	def __str__(self): #function to display the current list contents
		if self.firstnode != None: #check to make sure list isnt empty
			currentval= self.firstnode #temp variable for cyclying through list at beginning
			out= '['+str(currentval.value)    #temp variable "out" for appending each new element of list
			while currentval.next !=None:  #cycles through list of current values until it reaches end
				currentval= currentval.next #current value is next element of list
				out+=', '+str(currentval.value)#appends current value to out temp variable, separated by comma
			return out +']' 
		return '[]' #print list
"""		
	def reverse(self):
		if self==None: 
			return
		head=self
		tail=self.firstnode.next
		self.reverse(tail)
		print head,

	def getNode(self, position): #identify a specific node by its position in list
		currentNode=self.firstnode
		for x in range(position):
			currentNode=currentNode.next
		return currentNode
	
	def getNextnode(self): #get next node in list
		return self.next	
	
	def setNextnode(self,nextItem): #sets the next node of current node
		self.next = nextItem	
		
	def poplast(self): #function to pop a node out of list
		previous = self.firstnode
	    for i in range(self):
	        previous = self.getNext()
	 
	    toRemove = previous.getNext()
	    afterNext = None
	    if toRemove.hasNext():
	        afterNext = toRemove.getNext()
	    previous.setNext(afterNext)
	    self.length-=1
	    return toRemove.getElement()
	  	
	def addNodeAfter(self, x, afterx)
		toaddNode=self.getNode(afterx)	
		if self.toaddNode==self.lastnode: #treat additional node as regular addnode if added to end
			currentval= Node(x, None) #temp variable specified as user input
			self.lastnode.next=currentval #links the previous last node to new current value
			self.lastnode=currentval#reclassifies last node as new current value 
			self.length+=1
		else: 
		currentval=Node(x, self.value)
		self.currentval.next+=x
		self.length+=1	
		
		

	def reverse(self): #function to reverse list
		current = self.next
		previous= None
        while current:
			next = current.next
			current.next = previous
			previous= current 
			current = next
			if self.next: 
				self.value = self.next
				self.next = previous	

	def addNodeAfter(self, x, afterx)
		addNode=self.getNode(after)	
		if self.addNode== self.lastnode: #treat additional node as regular addnode
			currentval= Node(x, None) #temp variable specified as user input
			self.lastnode.next=currentval #links the previous last node to new current value
			self.lastnode=currentval#reclassifies last node as new current value 
			self.length+=1
		else: 
		currentval=Node(x, self.value)
		self.currentval.next+=x
		self.length+=1
		
	def removeNode(self, index)
	    if self.first is index:
            self.first = index.next
        if self.last is index:
            self.last = index.value
        if index.next is not None:
            index_next._prev = node._prev
        if node._prev() is not None:
            node._prev()._next = node._next
        node._next = None
        node._prev = _ref(None)
        return node.obj


def addNodeAfter(self, new_value, before_node):

def removeNode(self, node_to_remove):

def removeNodesByValue(self, value):

def reverse(self):

def __str(self)__:
"""	