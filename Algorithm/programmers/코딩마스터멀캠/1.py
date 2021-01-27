from itertools import product

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    pricelist=[priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]
    cnt=0
    def DFS(d, sum):
        nonlocal pricelist, cnt, budgeted
        if sum>budgeted:
            return
        if d==4:
            cnt+=1
            return
        else:
            for i in pricelist[d]:
                
                DFS(d+1, sum)
    

    DFS(0,0)
    return cnt
print(getNumberOfOptions([2,3],[4], [2], [1,2,3] , 10))