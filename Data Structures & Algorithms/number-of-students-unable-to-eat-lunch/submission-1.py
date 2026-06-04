# from collections import deque

class Solution:
    from collections import deque

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Students is a queue
        # Sandwiches is a stack
        # The lists are both the same size
        # Circle = 0 and Square = 1
        #
        # If student at the front likes sandwich, 
        # take it from stack and leave queue (Remove both!)
        #
        # If not, do NOT take the sandwich, go to back of the line!
        q = deque(students)
        print(f"Start: {q}")
        
        while q:
            if q[0] == sandwiches[0]: # The problem says 0 is top of stack
                q.popleft() # Student leaves the queue
                sandwiches.pop(0) # This pops the proper index
                print(f"yes: {q}")
            elif sandwiches[0] not in q: # Breaks the loop once no more matches are present
                break
            else:
                q.append(q.popleft()) # Leave the line, go to the back
                print(f"no: {q}")

        return len(q)
