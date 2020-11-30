# 코딩테스트 연습 > Summer/Winter Coding(~2018) > 스킬트리
def solution(skill, skill_trees):
    res=0
    for i in skill_trees:
        k=0
        for j in i:
            if j in skill:
                if j==skill[k]:
                    pass
                else:break
                k+=1
        else:res+=1        

    return res

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))