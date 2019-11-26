class Solution():
    def method(self, s1, s2):
        if s1 == '0' or s2 == '0':
            return '0'
        elif s1 == '1':
            return s2
        elif s2 == '1':
            return s1
        else:
            if len(s1) < len(s2):
                temp = s1
                s1 = s2
                s2 = temp
            s1_list = []
            s2_list = []
            for i in range(len(s1)-1,-1,-1):
                s1_list.append(s1[i]+'0'*(len(s1)-i-1))
            for i in range(len(s2)-1,-1,-1):
                s2_list.append(s2[i])
            sum_outer = 0
            for i in range(0,len(s2_list)):
                sum_inner = 0
                for j in range(0,len(s1_list)):
                    sum_inner += int(s2_list[i]) * int(s1_list[j])
                sum_outer += int(str(sum_inner)+"0"*i)
            return str(sum_outer)

if __name__== "__main__":
    sol = Solution()
    print(sol.method("8000","8000"))