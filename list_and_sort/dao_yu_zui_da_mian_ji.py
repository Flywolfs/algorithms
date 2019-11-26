class Solution():
    def method(self, grid):
        if grid == [[]]:
            return 0
        max_size = 0
        coords = list()
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1 and [i,j] not in coords:
                    size = 0
                    self.search(grid,i,j,'up',coords,size)
                    if size > max_size:
                        max_size = size
        return max_size

    def search(self,grid,x,y,pre_dire, coords,size):
        if x < len(grid)-1 and x > 0  and y < len(grid[0])-1 and y > 0:
            # xia
            if grid[x+1][y] == 1 and [x+1,y] not in coords:
                coords.append([x+1,y])
                size += 1
                self.search(grid,x+1,y,coords)
            # you
            elif grid[x][y+1] == 1 and [x,y+1] not in coords:
                coords.append([x,y+1])
                size += 1
                self.search(grid,x,y+1,coords)
            # shang
            elif grid[x-1][y] == 1 and [x-1,y] not in coords:
                coords.append([x-1, y])
                size += 1
                self.search(grid, x-1, y, coords)
            # zuo
            elif grid[x][y-1] == 1 and [x,y-1] not in coords:
                coords.append([x,y-1])
                size += 1
                self.search(grid, x, y-1, coords)
        elif x == 0 and y == 0 and grid[x][y] == 1:
            pass
        # di
        elif x == len(grid)-1 and grid[x,y+1] == 1:
            coords.append([x,y+1])
            self.search(grid,x,y+1,coords)
        # zui_you_lie
        elif y == len(grid)-1 and grid[x+1,y] == 1:
            coords.append([x+1,y])
            self.search(grid,x+1,y,coords)


    def search_up(self,grid,x,y,pre_direc,coords,size):
        if grid[x - 1][y] == 1 and [x - 1, y] not in coords:
            coords.append([x - 1, y])
            size += 1
            self.search(grid, x - 1, y, coords)
