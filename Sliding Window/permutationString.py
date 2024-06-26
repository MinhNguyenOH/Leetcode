class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0]*26
        count_s2 = [0]*26
        
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')] += 1
            count_s2[ord(s2[i])-ord('a')] += 1
        
        l = 0
        matches = 0
        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if count_s1 == count_s2:
                return True
            index = ord(s2[r]) - ord('a')
            count_s2[index] += 1
            if count_s2[index] == count_s1[index]:
                matches += 1
            elif count_s2[index] - 1 == count_s1[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            count_s2[index] -= 1
            if count_s2[index] == count_s1[index]:
                matches += 1
            elif count_s2[index] + 1 == count_s1[index]:
                matches -= 1
            l += 1
        return matches == 26