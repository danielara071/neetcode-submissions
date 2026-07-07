class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "/*-+":
                b, a  = stack.pop(), stack.pop()
                if t == "+":
                    stack.append( a + b)
                elif t =="*":
                    stack.append(a * b)
                elif t == "-":
                    stack.append(a - b)
                else:
                    div = a / b
                    if div > 0:
                        stack.append(math.floor(div))
                    else:
                        stack.append(math.ceil(div))
            else:
                stack.append(int(t))
        return stack[-1]

