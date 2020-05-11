# third attempt:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1 or numRows > len(s):
            return s
        
        result, index, step = [''] * numRows, 0, 0
        for c in s:
            result[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            
        return "".join(result)

# second attempt:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        
        results = ["" for _ in range(numRows)]
        
        current_position = 0
        going_down = False
        
        for character in s:
            results[current_position] += character
            
            if current_position == 0 or current_position == numRows - 1:
                going_down = not going_down
            
            current_position += 1 if going_down else -1
        
        output = ""
        for s in results:
            output += s
            
        return output

# first attempt:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        
        results = ["" for _ in range(numRows)]
        positions = [i for i in range(0, numRows)]
        
        results[0] += s[0]
        current_position = 0
        order = []
        for index in range(1, len(s)):
            if not order:
                if current_position == 0:
                    order = list(positions)[::-1]
                else:
                    order = list(positions)
                
            if current_position == order[-1]:
                order.pop()
                
            current_position = order.pop()
            results[current_position] += s[index]
            
        print(results)
        
        output = ""
        for s in results:
            output += s
            
        return output
