class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # words = s.split()

        # reverse_words = words[::-1]
        # return ' '.join(reverse_words)

        chars = list(s.strip())

        def reverse(start, end):
            while start < end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1

        reverse(0, len(chars) - 1)

        n = len(chars)
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == " ":
                reverse(start, end - 1)
                start = end + 1

        return " ".join("".join(chars).split())


d = Solution()
strs = "the sky is blue"

res = d.reverseWords(strs)
print(res)

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""
