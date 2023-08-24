class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {
            "+": ( lambda x, y: operator.add(x, y)),
            "-": ( lambda x, y: operator.sub(x, y)),
            "*": ( lambda x, y: operator.mul(x, y)),
            "/": ( lambda x, y: int(x/y))
        }
        
        stack = []
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                x = stack.pop(-2)
                y = stack.pop()
                stack.append(operators[token](x, y))
        return stack[-1]                