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
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                print(f"yes: {q}")
            elif sandwiches[0] not in q:
                break
            else:
                q.append(q.popleft())
                print(f"no: {q}")

        return len(q)
