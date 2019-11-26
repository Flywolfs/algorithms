class Solution:
    def findCircleNum(self, friends):
        records = []
        circles = []
        for i in range(0,len(friends)):
            for j in range(0,i+1):
                if friends[i][j] == 1:
                    records.append((i,j))
        circle = set()
        for i in records:
            if circle == {}:
                circle.add(i[0])
                circle.add(i[1])
            else:
                if i[0] not in circle and i[1] not in circle:
                    circles.append(circle)
                    circle = set()
                    circle.add(i[0])
                    circle.add(i[1])
                elif i[0] not in circle:
                    circle.add(i[0])
                else:
                    circle.add(i[1])
        print(circles)
        return len(circles)



if __name__=="__main__":
    sol = Solution()
    print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))