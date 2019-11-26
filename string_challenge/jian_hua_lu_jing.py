class Solution():
    def method(self, path):
        path_split = []
        simplified = []
        for i in path.split("/"):
            if i != '':
                path_split.append(i)
        for i in path_split:
            if i == ".." and simplified != []:
                simplified.pop()
            elif i == "..":
                pass
            elif i == '.':
                pass
            else:
                simplified.append(i)
        return "/"+"/".join(simplified)


if __name__=="__main__":
    sol = Solution()
    print(sol.method("/a//b////c/d//././/.."))