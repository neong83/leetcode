func longestPalindrome(s string) string {
	res := ""
	for i := 0; i < len(s); i++ {
		s1 := palidrome(s, i, i);
		s2 := palidrome(s, i, i + 1);
		
		if len(res) < len(s1) {
			res = s1
		}

		if len(res) < len(s2) {
			res = s2
		}
	}

	return res
}

func palidrome(s string, left int, right int) string {
	for {
		if left >= 0 && right < len(s) && s[left] == s[right] {
			left -= 1
			right += 1
		} else {
			break
		}
	}

	left += 1 //why? this will fix the left-1 operation from line 22 when output the substring

	return s[left:right]
}

/*
walk thought

input string: "babaa"

when i = 1
s1 = left => 1 right =>1
s2 = left => 1 right =>2

enter palidrome function as s1
enter for loop
position 1 is letter a 
	1. left is greater than 0
	2. right is less than lenght of input
	3. position 1 is equal to position 1 of the input string s[1] = s[1]
so left will minus 1 and right will add 1 (execute line 22 and 23)

repeat for loop
position left = 0 and right = 2
	1. left is greater than 0
	2. right is less than length of input
	3. psoition 0 is equal to psoition 2 of the inputer string s[0] = s[2] => b = b
so left will minus 1 and right will add 1

repeat for loop
position left = -1 and right = 3
	1. left is less than 0
if condition break
for loop break at line 25

as the condition had execute before we break 
so we need to restore left to its last good condition at line 29

but why we do not need to do so from right?
the reason is language (golang for example) is taken the last index of substring as its upper bound, meaning it will extract substring only to the location that is less than it

to put it as exmaple, s[1:5]
this will extract s[1], s[2], s[3], and s[4]
*/