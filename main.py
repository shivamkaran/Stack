#Stack Empty
class Stack:
  def __init__(self,limit=10):
    self.arr=[]
    self.limit=limit
  def empty_Stack(self):
    return len(self.arr)<=0
  def push(self,item):
    if len(self.arr)>=self.limit:
      print('Stack Overflow!')
    else:
      self.arr.append(item)
      print('After stack add',self.arr)
  def pop(self):
    if len(self.arr)<=0:
      print('Stack Underflow!')
    else:
      return self.arr.pop()            
  def peek(self):
    if len(self.arr)<=0:
      print('UnderFlow!')
      return 0
    else:
      return self.arr[-1]
  def size(self):
    return len(self.arr)
our_stack=Stack(5)
our_stack.push('1')
our_stack.push('10')
our_stack.push('3')
our_stack.push('5')
print('Stack peek is',our_stack.peek())









