
class Solution():
    def method(self,string):
        if string == "":
            return 0
        max_list = []
        max = 0
        str2list = list(string)
        for el in range(0,len(str2list)):
            if str2list[el] not in max_list:
                max_list.append(str2list[el])
            elif str2list[el] in max_list:
                if len(max_list) > max:
                    max = len(max_list)
                pos = max_list.index(str2list[el])
                max_list = max_list[pos+1:]+[str2list[el]]
        if len(max_list) > max:
            max = len(max_list)
        return max

if __name__=="__main__":
    sol = Solution()
    print(sol.method("abcvd"))