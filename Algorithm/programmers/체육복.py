def solution(n, lost, reserve):
    student = [1]*n
    for i in lost:
        student[i-1]=0
    for i in reserve:
        student[i-1]+=1
    
    cnt=last1=last2=0
    
    for i in range(n):
        if student[i]==0:
            
            if i>0 and student[i-1]==2:
                student[i-1]=student[i]=1
            elif i<n-1 and student[i+1]==2:
                student[i]=student[i+1]=1
                
        if student[i]!=0:
            cnt+=1

    return cnt