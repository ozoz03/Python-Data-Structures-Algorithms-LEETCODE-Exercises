Suppose the linked list is 
1 -> 2 -> 3 -> 4 -> 5, 

and start_index = 2 and end_index = 4. 
Then, the method should modify the linked list to 
1 -> 2 -> 5 -> 4 -> 3 .

        start      end
          I         I
1 -> 2 -> 3 -> 4 -> 5 -> 6
0    1    2    3    4    5     index
1 -> 2 -->5 -> 4 -> 3 --> 6

before_start.next = end
start.next = end.next
