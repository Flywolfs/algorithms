class Solution():
    def method(self, string):
        if string == "":
            return ""
        elif len(string) < 4 or len(string) > 12:
            return []
        length = len(string)
        possible = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a+b+c+d == length:
                            splited = [string[0:a],string[a:a+b],string[a+b:a+b+c],string[a+b+c:a+b+c+d]]
                            add = True
                            for each in splited:
                                if   len(each) > 1 and each[0] == '0':
                                    add = False
                                elif int(each)>255 or int(each) < 0:
                                    add = False
                            if add:
                                possible.append(".".join(splited))
        return possible


if __name__=="__main__":
    sol = Solution()
    print(sol.method("010010"))