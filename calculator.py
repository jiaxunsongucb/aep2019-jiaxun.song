class Calculator(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        s += " "
        l = len(s)

        def basic(i):
            stack = []
            curVal, sign = 0, "+"
            sign = "+"
            while i < l:
                curr = s[i]
                if curr.isdigit():
                    while s[i].isdigit():
                        curVal = curVal * 10 + int(s[i])
                        i += 1
                elif curr == "(":
                    curVal, i = basic(i + 1)
                else:
                    if sign == "+":
                        stack.append(curVal)
                    elif sign == "-":
                        stack.append(-curVal)
                    elif sign == "*":
                        stack.append(stack.pop() * curVal)
                    elif sign == "/":
                        stack.append(int(stack.pop() / curVal))

                    curVal, sign = 0, curr
                    i += 1
                    if sign == ")":
                        return sum(stack), i
            return sum(stack)

        return basic(0)
