class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.current = None
        self.before = None

        self.num_data = 0

    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False

    def size(self):
        return self.num_data

    def append(self, data):
        new_node = Node(data)
        
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.num_data += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.num_data += 1

    def traverse(self, mode = 'next'):
        if self.empty():#1
            return None
        
        if mode == 'first':#2
            self.before = self.head
            self.current = self.head
        else:#3
            if self.current.next == None:#4
                return None

            self.before = self.current#5
            self.current = self.current.next

        return self.current.data#6

    def remove(self):
        ret_data = self.current.data#1
        
        
        #1. 데이터가 하나일 때     
        if self.size() == 1:#2
            self.head = None
            self.tail = None
            self.before = None
            self.current = None
        #2. current == head
        elif self.current is self.head:#3
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next
        else:
            #current == tail
            if self.current is self.tail:#4
                self.tail = self.before
            #일반적인 경우 
            self.before.next = self.current.next#5
            self.current = self.before
            
        self.num_data -= 1
        return ret_data#6

def show_list(slist):
    data = slist.traverse('first')

    if data:
        print(data, end = '  ')
        data = slist.traverse()
        while data:
            print(data, end = '  ')
            data = slist.traverse()
    else:
        print("There is no data")
                
# if __name__ == "__main__":
#     slist = LinkedList()#1
#     print("데이터의 개수 : {}".format(slist.size()))
#     show_list(slist)
#     print("\n")
#
#     slist.append(2)#2
#     slist.append(3)
#     slist.append(1)
#     slist.append(5)
#     slist.append(2)
#     slist.append(10)
#     slist.append(7)
#     slist.append(2)
#
#
#     print("데이터의 개수 : {}".format(slist.size()))
#     show_list(slist)
#     print("\n")
#
#
#     data = slist.traverse('first')#3
#     while data:
#         if data == 2:
#             slist.remove()
#         data = slist.traverse()
#
#     print("데이터의 개수 : {}".format(slist.size()))
#     show_list(slist)
#     print("\n")
#
#     slist.append(3)
#
#     print("데이터의 개수 : {}".format(slist.size()))
#     show_list(slist)

    
   


    
    
    
    
