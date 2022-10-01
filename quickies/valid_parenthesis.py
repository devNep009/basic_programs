class Solution:
    # Solution by Nandan 18 : https://github.com/Nandan-18

    def is_valid(self, word: str) -> bool:

        stack = []
        bracket_mapper = {"]": "[", "}": "{", ")": "("}    # key:value pairs

        for char in word:
            if char in bracket_mapper.values():
                stack.append(char)
            elif char in bracket_mapper:
                if stack == [] or bracket_mapper[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []
