class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

    def insert(self, n):
        n.next = self
        return n

def has_cycle(ll):
    if not ll or not ll.next:
        return False
    fp = ll.next
    sp = ll
    while fp and fp.next:
        if fp == sp or fp.next == sp:
            return True
        fp = fp.next.next
        sp = sp.next
    return False

my_list = Node(7).insert(Node(5))
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next}")
print(has_cycle(my_list))
my_list.next.next = my_list
print(f"List {my_list.val} --> {my_list.next.val} --> {my_list.next.next.val}")
print(has_cycle(my_list))