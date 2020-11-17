# Principal Componet Analysis

- 변수의 수가 많으면 불필요한 변수 존재할 가능성이 높다
- 시각적표현 어려움
- 계산 복잡도 높아 모델링 비효율적
- 중요한 변수만 선택필요



변수 선택(feature selection) : 목적에 부합하는 소수의 예측 변수만을 선택

- 장점 : 선택한 변수 해석 용이
- 단점 : 변수간 상관관계 고려 어려움

변수 추출(feature extraction)

- 장점 : 변수간 상관관계 고려, 일반적으로 변수의 개수를 많이 줄일 수 있음
- 단점 : 추출된 변수의 해석이 어려움


```
Supervised 			 	feature selection
Unsupervised 			feature extraction

총 4가지 조합
```

#### 변수 선택/추출을 통한 차원 축소

1. **Supervised feature selection** : Information gain, Stepwise regression, 
   LASSO, Genetic algorithm...

2. **Supervised feature extraction** : Partial least squares (PLS)
3. **Unsupervised feature selection** : PCA loading(별로 연구 되어있지 않음)

4. **Unsupervised feature extraction** : <u>Principal</u> component analysis (PCA), 
   Wavelets transforms, Autoencoder



### PCA 개요

​	고차원 데이터를 효과적으로 분석하기 위한 대표적 분석 기법

​	차원 축소, 시각화 ,군집화, 압축

- \mbox{n} 개의 관측치와 p개의 변수로 구성된 데이터를 상관관계가 없는 k개의 변수로 구성된 데이터 (n 개의 관측치)로 요약하는 방식, 요약된 변수는 기존변수의 선형조합으로 생성됨
- 원래 데이터의 분산을 최대한 보존하는 새로운 축을 찾고, 그 축에 데이터를 사영(Projection) 시키는 방법
- 전체 분석 과정 중 초기에 사용

Z is a linear combination (선형결합) of the original p variables in X
$$
\fbox{
Z_1 = a_1^TX =  a_{11}X_1 + a_{12}X_2 + ··· \~{}\\mbox{d}

}
$$
