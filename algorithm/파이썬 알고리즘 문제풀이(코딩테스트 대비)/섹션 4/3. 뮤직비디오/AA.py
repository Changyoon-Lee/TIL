import sys
sys.stdin = open('섹션 4/3. 뮤직비디오/in5.txt')

n_song, n_dvd = map(int, input().split())
song_list = list(map(int, input().split()))

upper = max(song_list)*(n_song//n_dvd+1)
search = upper//2
lower = 0

while True:
    temp = 0
    cnt = 1 #DVD의 갯수 counting 1부터 시작
    for song in song_list:
        temp+=song
        if temp > search: #제한시간 넘어가면 다음 DVD로 시작
            cnt+=1
            temp = song

    if (search==lower or search==upper) and cnt<=n_dvd:
        print(search)
        break

    if cnt > n_dvd:
        lower = search
        search = (search+upper+1)//2
    else :
        upper = search
        search = (search+lower)//2
    

