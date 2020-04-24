# Second attemp:
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        string_length = len(s)
        longest_palindromic = ""
        for i in range(string_length):
            for j in range(string_length, i, -1):
                sub_string = s[i:j]
                # print(f'i: {i}, j: {j}')
                # print(f'sub string: {sub_string}')
                
                # reduce time
                if len(longest_palindromic) > j - i:
                    break
                elif sub_string == sub_string[::-1]:
                    longest_palindromic = sub_string
                    break
                
        return longest_palindromic

# First attemp:
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        string_length = len(s)
        
        if string_length == 1: return s
        
        longest_palindromic = ""
        for i in range(string_length):
            for j in range(string_length - 1, i - 1, -1):
                sub_string = s[i:j + 1]
                # print(f'i: {i}, j: {j}')
                # print(f'sub string: {sub_string}')
                
                if sub_string == sub_string[::-1] and len(sub_string) > len(longest_palindromic):
                    longest_palindromic = sub_string
                
        return longest_palindromic


## Back up solution that get from other place
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        str_len = len(s)
        print("---------")
        if not s or s == s[::-1]:
            return s
        
        move_position, start_position = 1, 0
        
        for index in range(1, str_len):
            current_substring = s[index - move_position - 1: index + 1]
            print(f"current substring={current_substring}, i={index}, move={move_position}")
            
            # still don't have a clear understanding why only check for 2 positions
            if (index - move_position >= 1 and
                current_substring == current_substring[::-1]
            ):
                start_position = index - move_position - 1
                move_position += 2
            else:
                current_substring = s[index - move_position: index + 1]
                print(f"current substring={current_substring}, i={index}, move={move_position}")
                if current_substring == current_substring[::-1]:
                    start_position = index - move_position
                    move_position += 1
                
                
        return s[start_position:start_position + move_position]
            
