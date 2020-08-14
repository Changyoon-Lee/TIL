contents

* [LSTM](#LSTM)

- [GRU](#GRU)

- [Seq2Seq](#Seq2Seq)



[![Stargazers][stars-shield]][stars-url]





[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][contributors-shield] : https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square][https://github.com/othneildrew/Best-README-Template/network/members]







































### LSTM

cell state

forget input output gate

### GRU

forget gate, input gate



### Seq2Seq

- Many to One : 입력 시퀀스가 단일 벡터로 인코딩
- One to Many : 단일 벡터입력으로 시퀀스 출력
- Seq2Seq 입력 시퀀스를 단일 컨텍스트 벡터로 인코딩, 컨텍스트 벡터를 입력으로 시퀀스를 출력





#### encoder

- 입력문장은 단어토큰화를 통해서 단어 단위로 쪼갬
- RNN 셀의 각 시점에 입력이 됨
- 모든 단어를 입력 받은 뒤 RNN 셀의 마지막 시점의 은닉상태가 context vector 이다

#### decoder

훈련과정

encoder가 보낸 context vector와 실제정답인 <sos> je suis étudiant 를 입력 받았을 때 je suis étudiant <eos>가 나와야한다고

알려주며 훈련한다(교사강요)



test과정

- 초키입력으로 <sos> 가 들어감 -> 다음에 등장할 확률이 높은 단어를 예측 -> 예측된 단어는 다음 시점의 RNN으로 입력->반복
- <eos> 가 다음 단어로 예측 될떄까지 반복한다





---

tokenize 방식(영어) :  띄어쓰기 기준으로 토큰화 하고 역순으로 배열 한다

src, trg 함수 : 시작<sos> 끝<eos>

vocab dim = onhot 인듯





### PYTORCH

```python
x = x.new_ones(5, 3, dtype=torch.double) 
x = torch.randn_like(x, dtype=torch.float) #존재하는 텐서를 바탕으로 텐서를 만든다
x = torch.empty(5, 3) #0에 매우 가까운 이상한 값
print(x.size()) #행렬의 크기를 구한다.


x = torch.randn(4, 4)
y = x.view(16) #reshape 같은 느낌
z = x.view(-1, 8)

a.add_(1) # a에 1더하기
b = a.numpy()#넘피이 변환, 저장공간을 공유
torch.from_numpy(a) #토치텐서로 변환
```

```python
# ``torch.device`` 를 사용하여 tensor를 GPU 안팎으로 이동해보겠습니다.
if torch.cuda.is_available():
    device = torch.device("cuda")          # CUDA 장치 객체(Device Object)로
    y = torch.ones_like(x, device=device)  # GPU 상에 바로(directly) tensor를 생성하거나
    x = x.to(device)                       # 단지 ``.to("cuda")`` 라고만 작성하면 됩니다.
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` 는 dtype도 함께 변경합니다!
[출처] [DL] PyTorch 초급 튜토리얼 1 (Pytorch가 무엇인가)|작성자 Jun
```







