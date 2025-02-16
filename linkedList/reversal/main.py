class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  
  def stringify_list(self):
    stringified = ""
    if self.head_node != None:
      node = self.head_node
      stringified += str(node.get_value()) + "\n"
      while node.get_next_node() != None:
        node = node.get_next_node()
        stringified += str(node.get_value()) + "\n"
    return stringified
