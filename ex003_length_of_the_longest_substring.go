func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 { return 0 }
    
    maxCount := 0
    nonRepeatedWord := ""
    str := ""
    wordLenght := 0
    
    for _, c := range(s) {
        str = string(c)

        if strings.Contains(nonRepeatedWord, str) {
            nonRepeatedWord = strings.Split(nonRepeatedWord, str)[1]
        }
        nonRepeatedWord += str
        
        wordLenght = len(nonRepeatedWord)
        if maxCount < wordLenght {
            maxCount = wordLenght
        }
    }
    
    return maxCount
}