class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        n = len(tokens)
        for x in tokens:
            if x not in operators:
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    stack.append(a+b)
                elif x == '-':
                    stack.append(b-a)
                elif x == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack.pop()