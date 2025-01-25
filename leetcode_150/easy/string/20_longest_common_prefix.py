class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the array
        for string in strs[1:]:
            # Reduce the prefix until it matches the start of the string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


d = Solution()
strs = ["interspecies", "interstellar", "interstate"]

res = d.longestCommonPrefix(strs)
print(res)
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
