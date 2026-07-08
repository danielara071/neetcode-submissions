class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "-+/*"
        for token in tokens:
            if token in op:
                b, a = stack.pop(), stack.pop()
                if token == "*":
                    stack.append(a * b)
                elif token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "/":
                    div = a / b 
                    if div > 0 :
                        stack.append(math.floor(div))
                    else:
                        stack.append(math.ceil(div))
            else:
                stack.append(int(token))
        return stack[-1]
