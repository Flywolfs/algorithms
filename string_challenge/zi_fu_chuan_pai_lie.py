class Solution():
    def method(self, s1, s2):
        if len(s1)>len(s2):
            return False
        elif s1 in s2:
            return True
        elif len(s1) == len(s2) and s1 == s2:
            return True
        elif len(s1) == len(s2) and s1 != s2:
            return False
        else:
            s1_list = list(s1)
            return self.permutation(s1_list,0,s2)

    def permutation(self,s, i, s2):
        if i == len(s) and "".join(s) in s2:
            return True
        else:
            for j in range(i, len(s)):
                s[j], s[i] = s[i], s[j]
                if self.permutation(s, i + 1,s2):
                    return True
                s[j], s[i] = s[i], s[j]
        return False

if __name__=="__main__":
    sol = Solution()
    print(sol.method("ab",""))
