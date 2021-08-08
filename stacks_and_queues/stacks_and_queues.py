class Node:
    def __init__(self,value=""):
        self.value=value
        self.next = None
    def __str__(self):
        return str(self.value)    

#######CODE CHALLENGE 10 # # # # ## # ## #### # ## # ######  ## ####

class Stack:
    def __init__(self,node=None):
        self.top=node

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node      
    
    def pop(self):
        if self.top == None:
            return "this is an empty stack amigo"
        else:    
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.top == None:
            return "this is an empty stack amigo"
        else:
            return self.top.value
                          
    def is_empty (self):
        if self.top == None:
            return False
        else:
            return True    

  
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self , value):
        node=Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node    
            self.rear = node    

    def peek(self):
        if self.front==None:
            return "empty queue amigo"
        else:
            return self.front.value    
     
##### END CHALLENGE 10  # # #  # # # ## ## # # ## # # # # # # # ## # ## 
        
 #C#C#C# challenge 11 # # # # ### ## #  # # #       
class pseudo_queue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self,value):
        self.first_stack.push(value)
        return value

    def dequeue(self):
       while self.first_stack.top:
           self.second_stack.push(self.first_stack.pop())
       popped_value = self.second_stack.pop()

       while self.second_stack.top():
           self.enqueue(self.second_stack.pop())
       return popped_value
    #C#C#C# END challenge 11 # # # # ### ## #  # # #
        

# if __name__ == "__main__":
#     node1 = Node(4)
#     node2 = Node(3)
#     node3 = Node(2)
#     node4 = Node(1)
#     node1.next=node2
#     node2.next=node3
#     node3.next=node4
  