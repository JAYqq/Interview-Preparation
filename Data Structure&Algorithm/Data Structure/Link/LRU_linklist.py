'''单纯链表实现的LRU'''
class Node():
    def __init__(self):
        self.data=None
        self.next=None
link_list=None
head=None
tail=None

'''这里操作的时候为了节省空间，当原来链表中已经有这个节点的时候，不再创建新节点，
而是直接将tail指向这个节点，并把这个节点的next置为None防止循环打印'''
def operateLinklist(number):
    global head,tail
    present=head
    if present.data!=number:
        while present.next is not None:
            if present.next.data==number:
                tempNode=present.next
                present.next=present.next.next
                tail.next=tempNode
                tail=tail.next
                tempNode.next=None
                return
            present=present.next
    else:
        head=head.next
        tail.next=present
        tail=tail.next
        present.next=None
        return
    #执行到这里说明链表中没有该节点
    tempNode=Node()
    tempNode.data=number
    tail.next=tempNode
    tail=tail.next
def print_Linklist():
    global head
    present=head
    while present is not None:
        print(present.data,"--")
        present=present.next
def mainWork():
    global head
    global tail
    while True:
        number=input("Enter a number: ")
        if head is None:
            head=Node()
            head.data=number
            head.next=None
            tail=head
            print_Linklist()
        else:
            operateLinklist(number)
            print_Linklist()
if __name__ == "__main__":
    mainWork()


        