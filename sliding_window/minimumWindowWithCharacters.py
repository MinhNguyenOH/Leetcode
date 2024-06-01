class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        window = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        have = 0
        need = len(count_t)
        res_length = 9999
        res_pos = [-1, -1]
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                res_length = r - l + 1
                res_pos = [l, r]

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]: 
                    have -= 1
                l += 1

        l, r = res_pos[0], res_pos[1]
        if res_length == 999:
            return ""
        return s[l:r+1]