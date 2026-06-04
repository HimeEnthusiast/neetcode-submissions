class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        stack_pos = -1

        for op in operations:
            match op:
                case "C":
                    record.pop()
                    stack_pos -= 1
                    print(record)
                case "D":
                    if stack_pos > -1:
                        record.append(record[stack_pos] * 2)
                        stack_pos += 1
                    print(record)
                case "+":
                    if stack_pos > 0:
                        record.append(record[stack_pos] + record[stack_pos-1])
                        stack_pos += 1
                    print(record)
                case _:
                    record.append(int(op))
                    stack_pos += 1
                    print(record)
        
        return sum(record)