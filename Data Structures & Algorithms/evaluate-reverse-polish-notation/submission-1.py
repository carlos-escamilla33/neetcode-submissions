import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "*": operator.mul,
            "-": operator.sub,
            "+": operator.add,
        }
        stack = []

        for token in tokens:
            if token not in op and token != "/":
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if token == "/":
                    stack.append(int(first_num / second_num))  # truncate toward zero
                else:
                    stack.append(op[token](first_num, second_num))
            
        return stack[0]


""""
always have two integers in the stack

after you reach length two / have two integers in the array you want to take them and use the current symbol
"""