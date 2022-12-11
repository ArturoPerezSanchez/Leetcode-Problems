# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels

class Solution:

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        minw = x
        maxw = x
        minh = y
        maxh = y
        for row in range(len(image)):
            for col in range(len(image[0])):
                if(image[row][col] == "1"):
                    if(row<minw): minw = row
                    elif(row>maxw): maxw = row
                    if(col<minh): minh = col
                    elif(col>maxh): maxh = col
        print(minw, maxw,maxh,minh )
        return (maxw-minw+1)*(maxh-minh+1)

    # Iterative approach
    def minArea1(self, image: List[List[str]], x: int, y: int) -> int:
        self.visited = set()
        self.minw = x
        self.maxw = x
        self.minh = y
        self.maxh = y
        stack = [(x,y)]

        while(stack):
            self.visited
            self.minw
            self.minh
            self.maxw
            self.maxh
            cx, cy = stack.pop()
            if((cx, cy) in self.visited): continue
            self.visited.add((cx, cy))

            if(cx<self.minw): self.minw = cx
            elif(cx>self.maxw): self.maxw = cx
            if(cy<self.minh): self.minh = cy
            elif(cy>self.maxh): self.maxh = cy

            if(cx>0 and image[cx-1][cy] == "1" and (cx-1,cy) not in self.visited): stack.append((cx-1, cy))
            if(cx<len(image)-1 and image[cx+1][cy] == "1" and (cx+1,cy) not in self.visited): stack.append((cx+1, cy))
            if(cy>0 and image[cx][cy-1] == "1" and (cx,cy-1) not in self.visited): stack.append((cx, cy-1))
            if(cy<len(image[0])-1 and image[cx][cy+1] == "1" and (cx,cy+1) not in self.visited): stack.append((cx, cy+1))
        
        return (self.maxw-self.minw+1)*(self.maxh-self.minh+1)

    # Recursive Approach
    def minArea2(self, image: List[List[str]], x: int, y: int) -> int:
        self.visited = set()
        self.minw = x
        self.maxw = x
        self.minh = y
        self.maxh = y

        def rec(cx, cy):
            self.visited
            self.minw
            self.minh
            self.maxw
            self.maxh
            if((cx, cy) in self.visited): return
            self.visited.add((cx, cy))

            if(cx<self.minw): self.minw = cx
            elif(cx>self.maxw): self.maxw = cx
            if(cy<self.minh): self.minh = cy
            elif(cy>self.maxh): self.maxh = cy

            if(cx>0 and image[cx-1][cy] == "1"): rec(cx-1, cy)
            if(cx<len(image)-1 and image[cx+1][cy] == "1"): rec(cx+1, cy)
            if(cy>0 and image[cx][cy-1] == "1"): rec(cx, cy-1)
            if(cy<len(image[0])-1 and image[cx][cy+1] == "1"): rec(cx, cy+1)
        
        rec(x, y)
        return (self.maxw-self.minw+1)*(self.maxh-self.minh+1)
            
