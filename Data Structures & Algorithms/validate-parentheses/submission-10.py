class Solution:
    def isValid(self, s: str) -> bool:
        open = []

        for i in s:
            top_item = open[-1] if open else None

            match i:
                case "(" | "[" | "{":
                    open.append(i)

                case ")":
                    if top_item != "(":
                        return False
                    open.pop()

                case "]":
                    if top_item != "[":
                        return False
                    open.pop()

                case "}":
                    if top_item != "{":
                        return False
                    open.pop()

        return not open
