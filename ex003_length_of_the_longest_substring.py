# Third attemp:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        non_repeated_string = ""
        
        for c in s:
            
            if c in non_repeated_string:
                non_repeated_string = non_repeated_string.split(c)[1]
                
            non_repeated_string += c
            longest_length = result if (result := len(non_repeated_string)) > longest_length else longest_length
            
            # max() is better way to visual what the code is doing
            # but it take additional 20ms to allocate the function and get its result
            #longest_length = max(len(non_repeated_string), longest_length)
            
        return longest_length

# Second attemp:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        non_repeated_string = list()
        
        for c in s:
            
            if c in non_repeated_string:
                # located the index of the duplicate character
                # move cursor to next character
                # reset the substring with what is left behind
                non_repeated_string = non_repeated_string[non_repeated_string.index(c) + 1:]
            
            non_repeated_string.append(c)
            longest_length = max(len(non_repeated_string), longest_length)
            
        return longest_length
                

# First attemp:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)
        if string_length <= 1:
            return string_length
        
        non_repeated_string, longest_length = [], 0
        for i in range(string_length):
            non_repeated_string = [s[i]]
            
            for j in range(i, string_length):
                if j + 1 < string_length:
                    j = j + 1
                else:
                    break
                
                if s[j] not in non_repeated_string:
                    non_repeated_string.append(s[j])
                else:
                    break
                
                if (temp := len(non_repeated_string)) > longest_length:
                    longest_length = temp
                    
        if (result := len(non_repeated_string)) > longest_length:
            return result
        return longest_length
