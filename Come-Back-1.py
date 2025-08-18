#Roman To Integer Language System
class Solution(object):
    D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    S = 0

    def romanToInt(self, s):
        for i in range(len(s) - 1):
            if (self.D[s[i]] >= self.D[s[i + 1]]):
                self.S += self.D[s[i]]
            else:
                self.S -= self.D[s[i]]
        self.S += self.D[s[len(s) - 1]]
        return self.S
X=Solution()
print('I was born in',X.romanToInt('MMIII'))