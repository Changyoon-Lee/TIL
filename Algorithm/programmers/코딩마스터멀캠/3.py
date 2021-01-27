

def largestSubgrid(grid, maxSum):
    # Write your code here
    l = len(grid)
    k = len(grid)

    def sumgird(grid, l,k):#행,열,size
        for i in range(l-k):
            for j in range(l-k):
                ressum=0
                for row in range(i, k+i):
                    ressum+= sum(grid[row][j:k+j]) 
                if ressum>maxSum:
                    return False

        return True
                    
        
    res = sumgird(grid, l ,k)
    return res

print(largestSubgrid([[1,1,1],[1,1,1],[1,1,1]], 4))