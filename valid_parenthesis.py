class Solution:

    def isValid(self, s: str) -> bool:

        stack = []
        dict1 = {"]": "[", "}": "{", ")": "("}    # key:value pairs

        for i in s:
            if i in dict1.values():
                stack.append(i)
            elif i in dict1.keys():
                if stack == [] or dict1[i] != stack.pop():
                    return False
            else:
                return False

        return stack == []
