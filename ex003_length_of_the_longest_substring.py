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
