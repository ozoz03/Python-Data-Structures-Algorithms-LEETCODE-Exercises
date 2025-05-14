class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    # def reverse_between(self, start_index, end_index):
    #     if start_index < 0 or end_index >= self.length or start_index >= end_index:
    #         return None

    #     temp = self.head
    #     before = None
    #     after = None
    #     before_start = None
    #     start = None
    #     for i in range(self.length):
    #         if i == start_index - 1:
    #             before_start = temp
    #             print("before_start:",before_start.value)
    #             start = temp.next
    #             print("start:",start.value)
    #         if i == end_index:
    #             end = temp
    #             end_next = temp.next
    #             print("end:",end.value)

    #         if i >= start_index and i <= end_index:
    #             after = temp.next
    #             temp.next = before
    #             before = temp
    #             temp = after
    #             if temp is not None:
    #                 print("reversing:",temp.value)
    #             else:
    #                 print("reversing: None")
    #         else:
    #             temp = temp.next
    #             print("i,temp:",i, '\t',temp.value)

    #     if before_start is not None:
    #         before_start.next = end
    #     if start is not None:    
    #         start.next = end_next     
    # def reverse_between(self, start_index, end_index):
    #     if start_index < 0 or end_index >= self.length or start_index >= end_index:
    #         return None
    #     dummy = Node(0)
    #     current = self.head
    #     dummy.next = self.head
    #     prev = dummy
        # for i in range(end_index):
        #     print("i:", i, "prev:", prev.value, "current:", current.value)
        #     if i == start_index - 1:
        #         prev = current
        #         current = current.next
        #         break

        # print("current:", current.value)
        # start = prev
        # for i in range(end_index - start_index):
        #     to_move = current.next
            
        #     print("to_move:", to_move.value)
        #     print("current:", current.value)
        #     current.next = to_move.next
        #     to_move.next = prev.next
        #     prev = to_move.next
        #     start.next = to_move
            
        # self.head = dummy.next  
    def reverse_between(self, start_index, end_index):
        if start_index < 0 or end_index >= self.length or start_index >= end_index:
            return None
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for i in range(start_index):
            prev = prev.next

        current = prev.next
        print("prev:", prev.value, "current:", current.value)
        for i in range(end_index - start_index):
            to_move = current.next
            print("to_move:", to_move.value)
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        self.head = dummy.next              

  
          

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
# linked_list.append(6)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
