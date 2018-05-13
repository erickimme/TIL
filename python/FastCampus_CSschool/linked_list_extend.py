from linked_list import *

class LinkedListEx(LinkedList):
    # search (target, mode = 'next') -> data(없으면 none)
    def search(self, target, mode = 'next'):
        if mode == 'first':
            data = self.traverse('first')
        else:
            data = self.traverse('next')

        while data: #data가 있다면 while을 돌면서
            if data == target:
                return data
            data = self.traverse()

        return None

    # current 가 가리키는 노드의 데이터를 업데이트
    # update(data) -> None
    def update(self, data):
        self.current.data = data

    #remove 찾은 데이터 하나만 지움
    # remove(target) -> data
    def remove(self, target):
        data = self.traverse('first')

        while data:
            if data == target:
                return super().remove(data)
            data = self.traverse()
        return None # 못 찾은 경우 none을 반환

    #count : 찾는 데이터의 개수
    # count(target) -> num of target
    def count(self, target):
        cnt = 0
        data = self.search(target, 'first')
        while data: #데이터가 있을 경우
            cnt += 1
            data = self.search(target)


    #replace (target, f) -> None
    def replace(self, target, f):
        data = slist.search(2, 'first')
        while data:
            slist.update(f(data))
            data = slist.search(target)


if __name__ == "__main__":
    slist = LinkedListEx()  # 1
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")

    slist.append(2)  # 2
    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)
    slist.append(10)
    slist.append(7)
    slist.append(2)

    print("\n데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")

    # data = slist.traverse('first')  # 3
    #
    # while data:
    #     if data == 2:
    #         slist.remove()
    #     data = slist.traverse()
    #
    # print("데이터의 개수 : {}".format(slist.size()))
    # show_list(slist)
    # print("\n")
    #
    # slist.append(3)


    # print("\n---extended function test---")
    # ext_slist = LinkedListEx()
    #R
    # ext_slist.append(2)
    # ext_slist.append(3)
    # ext_slist.append(5)
    # ext_slist.append(6)
    # ext_slist.append(9)
    # ext_slist.append(8)
    #
    # print("데이터의 개수 : {}".format(ext_slist.size()))
    # show_list(ext_slist)
    #
    # print("\n----searching 데이터----")
    # ext_slist.search(5)
    #
    #
    # print("\n----updating 데이터----")


    # Client code
    # data = slist.search(2, 'first')
    # while data:
    #     slist.update(4)
    #     data = slist.search(2)


    slist.replace(2, lambda x : x*2)
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print('')
