def hms2s(t):
    a = list(map(int, t.split(':')))
    s = a[0]*60*60+a[1]*60+a[2]
    return s

def s2hms(second):
    h = str(second//3600).zfill(2)
    m = str((second%3600)//60).zfill(2)
    s = str(second%60).zfill(2)
    return h+':'+m+':'+s

def solution(play_time, adv_time, logs):
    play_time = hms2s(play_time)
    adv_time = hms2s(adv_time)
    timedic={}
    timedic[0]=0
    loglist=[]
    for i in logs:
        a = i.split('-')
        loglist.append((hms2s(a[0]),0))
        loglist.append((hms2s(a[1]),1))

    loglist.sort()
    cnt=0
    for i in loglist:
        if i[1]==0:
            cnt+=1
            timedic[i[0]]=cnt
        else:
            cnt-=1
            timedic[i[0]]=cnt
            
    startpoint_list = [i for i in timedic.keys()]#+[i-adv_time for i in timedic.keys() if i-adv_time>=0]

    max = (0, 0)#시작지점, 누적시청시간
    for i in startpoint_list:
        Q=[]
        for j in startpoint_list:
            if i<=j<i+adv_time:
                Q.append(j)
        if i+adv_time<=play_time:
            Q.append(i+adv_time)
        else :
            continue
        size=len(Q)
        last=0
        sum=0
        for _ in range(size):
            ck = Q.pop(0)
            if last:
                sum+=(ck-last)*timedic[last]
            last = ck

        if sum>max[1]:
            max = (i, sum)

    return s2hms(max[0])


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))