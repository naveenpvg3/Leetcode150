class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for char in s:
            if char not in s_freq:
                s_freq[char] = 1
            s_freq[char] += 1
            #ALT = s_freq[char] = s_freq.get(char,0) + 1
        for char in t:
            if char not in t_freq:
                t_freq[char] = 1
            t_freq[char] += 1
            #ALT = t_freq[char] = t_freq.get(char,0) + 1
        return s_freq == t_freq
    
     #Time Complexity: O(max(len(s), len(t)))
     #Space Complexity: O(len(s) + len(t))