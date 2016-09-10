class RPN(object):
    def evaluate(self, expr):
        """Evaluates an expression given in Reverse Polish Notation (RPN.)"""
        stack = []
        for c in expr.split():
            print c
            try:
                if c == "+":
                    y, x = stack.pop(), stack.pop()
                    stack.append(x + y)
                elif c == "-":
                    y, x = stack.pop(), stack.pop()
                    stack.append(x - y)
                elif c == "*":
                    y, x = stack.pop(), stack.pop()
                    stack.append(x * y)
                elif c == "~":
                    x = stack.pop()
                    stack.append(-x)
                else:
                    stack.append(int(c))
            except IndexError:
                return -999
        ans = stack.pop()
        return ans if not stack else -999
