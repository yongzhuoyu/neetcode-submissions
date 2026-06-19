class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Check whether token is operand or operator 
        #If it is an operand, convert it to int and push them into stack 
        #If it is an operator, pop the last two elements and calculate the product 
        #The format for calculation should always be left operator right
        #as order matters for subtraction and division 
        #Push the result back into stack and its used as an operand for future operators
        
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    result = left + right
                    stack.append(result)
                elif token == "-":
                    result = left - right 
                    stack.append(result)
                elif token == "*":
                    result = left * right
                    stack.append(result)
                else:
                    result = int(left / right)
                    stack.append(result)
        return stack[-1]