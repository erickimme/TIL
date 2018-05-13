class Stack(list):
    push = list.append#1   
    
    def empty(self):#2
        if not self:
            return True
        else:
            return False

    def peek(self):#3
        return self[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    while not s.empty():
        data = s.pop()
        print(data)
				#print(data, end = '  ')
