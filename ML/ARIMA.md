# ARIMA model

![](https://img.shields.io/badge/Required_Chrome_extensions_to_see_correctly-white)[![](https://img.shields.io/static/v1?label=Download&message=mermaid&color=blueviolet)](https://chrome.google.com/webstore/detail/github-%2B-mermaid/goiiopgdnkogdbjmncgedmgpoajilohe/related?hl=en)[![](https://img.shields.io/static/v1?label=Download&message=MathJax_Plugin&color=blue)](https://chrome.google.com/webstore/detail/tex-all-the-things/cbimabofgmfdkicghcadidpemeenbffn/related?hl=en)

##### 참고자료 : 김성범교수 Youtube

### Box-Jenkins ARIMA Procedure

<img src="img/arima_1.png" alt="image" style="zoom:80%;" />



## 1. data processing

#### ACF - check stationarity

- lag 0 일때는 항상 1(자기자신이기때문)
- nonstationary process 의 경우  ACF가 전반적으로 천천히 떨어지는 양상을 보임
- stationary process의 경우 급격히 떨어지거나 패턴이 없다



##### example

<img src="img/arima_2.png" style="zoom:67%;" />

![](img/arima_3.png)

#### nonstationary -> stationary 바꿔 줘야함

- 차분

$$
Y_t = \Delta{X_t}=X_t - X_{t-1}
$$



- 1차 차분후 ACF

<img src="img/arima_4.png" style="zoom: 67%;" />

## 2. Identification ARIMA model

- **Graphical method**(주관적임) : making inferences from the patterns of the sample autocorrelation and partial autocorrelation functions of the series

- 시계열 데이터의 ACF, PACF 를 보고 패턴을 파악한다

|   Model   |                            ACF                             |                         Partial ACF                          |
| :-------: | :--------------------------------------------------------: | :----------------------------------------------------------: |
|   MA(q)   |       Cut off after lag q<br>(q시차 이후 0으로 절단)       | Die out<br />(지수적으로 감소, <br />소멸하는 sine함수 형태) |
|   AR(p)   | Die out<br >(지수적으로 감소,<br />소멸하는 sine함수 형태) |       Cut off after lag p<br />(p시차 이후 0으로 절단)       |
| ARMA(p,q) |          Die out<br />(시차 (q-p)이후 부터 소멸)           |           Die out<br />(시차 (q-p)이후 부터 소멸)            |



##### 각 상황 예시

![](img/arima_5.png)

##### - 아래 결과를 보고 q값으로 1 선정 해본다

![](img/arima_6.png)

- p,q를 시범적으로 결정

- 그후 그주변 값들을 계산해봄
- ex ARIMA(0,1,1)/ p,d,q/ ARIMA(0,1,2)/ ARIMA(0,1,3) \... 

- computing power가 좋기 때문에 p(1~20) d(1~2) q(1~20) 의 grid search를 통해 최적값선정





## 3. Determination of Model

- Determine the model that renders the minimum AIC value
- AIC : 정확도의 척도 ,평가지표 , 낮을 수록 좋음



## 4. Diagnosis - Performance Evaluation

- Once the model has been specified and the parameters estimated, the model should be checked for adequacy
- Use the model to forecast all of the known values of the data and investigate the residuals, and generate the ACF plot for the residuals[($\hat y-y$) 실제값과 예측값의 차이]

- Rule: The model is OK if more than two or three out of 40 fall outside the bound of if one falls far outside the bounds. - 몇개만 예측에서 벗어난것은 괜찮다
- => 최종모델로 결정

<img src="img/arima_7.png" style="zoom:67%;" />

-> 경계값이내로 들어옴

# Seasonal ARIMA Model

- 기존 ARIMA 모델에 계절 변동을 반영
- 줄여서 SARIMA
- SARIMA 모형은 각 계절에 따른 독립적인 ARIMA모델이 합쳐져 있는 모형
- 기존 ARIMA(p,d,q) 모형에 계절성 주기를 나타내는 차수 s가 추가적으로 필요하기 때문에 ARIMA(p,d,q)(P,D,Q)s 로 표기한다.
- s의 값은 월별 계절성을 나타낼 때는 s=12가 되고 분기별 계절성을 나타낼 때는 s=4가 된다.

---


$$
\begin{align*}\\
X_1,X_2,\cdots,X_t \:&:\: \textrm{a sequence of random variable}(X:\text{Random Variables})\\\\

F_X(x) &= P(X\le x)\::\:\text{CDF(Cumulative distribution Fuction)}\\

E(X)&=\mu_x\\

V(X)&=E[(X-\mu_x)^2]=\sigma_x^2\\\\
\end{align*}
$$



$$
\begin{align*}\\
Cov(X_1, X_2)&=E[(X_1-\mu_1)(X_2-\mu_2)]\\
&=\large\sigma_{\small{X_1X_2}}\\∴ Cov(X_1,X_2)&=V(X_1)={\large\sigma_{\small{X_1}}}^2\\\\
Corr(X_1,X_2)&=\frac{Cov(X_1,X_2)}{\sqrt{V(X_1)\cdot V(X_2)}}
=\frac{\large\sigma_{\small{X_1X_2}}}{\sqrt{{\large\sigma_{\small{X_1}}}^2\cdot{\large\sigma_{\small{X_2}}}^2}}
=\frac{\large\sigma_{\small{X_1X_2}}}{\large\sigma_{\small{X_1}}\cdot\large\sigma_{\small{X_2}}}
\\\end{align*}
$$

$$
\begin{align*}

\end{align*}
$$

$$
\begin{align*}X, Y &:\text{independent}\\\\
E(X \cdot Y)&=E(X) \cdot E(Y) \\\nonumber\\
\operatorname{Cov}(X, Y)&=0 \\\nonumber\\
\operatorname{Cov}(X+2,Y)&=\operatorname{Cov}(X, Y)+\operatorname{Cov}(2,Y)\\
&=\operatorname{Cov}(X, Y)+E(2 Y)-E(2) \cdot E(Y)\\
&=\operatorname{Cov}(X, Y)+2E(Y)-2E(Y)\\
&=\operatorname{Cov}(X, Y)\\\nonumber
\\
\operatorname{Cov}(X, Y)&=\operatorname{Cov}(Y, X)\\\\
\operatorname{Cov}(aX, Y)&=a\operatorname{Cov}(X, Y)
\end{align*}
$$



- $\operatorname{Cov}\left(X_{t}, X_{t+h}\right) = \gamma_X(h)$

$\begin{aligned}\text { (a) }\quad \gamma_{X}(0) =\operatorname{Cov}\left(X_{t}, X_{t}\right)=V\left(X_{t}\right)=\sigma_{X t}^{2} \\\end{aligned}$

$\begin{aligned}\text { (b) }\quad \gamma_{X}(-h) &=\operatorname{Cov}\left(X_{t}, X_{t-h}\right) \\ &=\operatorname{Cov}\left(X_{t-h}, X_{t}\right) \\ &=\operatorname{Cov}\left(X_{t-h}, X_{(t-h)+h)}\right.\\ &=\gamma_{X}(h) \\ ∴\gamma_{X}(h)&=\gamma_{X}(-h) \text { for all } h\\
&\to \textbf{Symmetry} \end{aligned}$



##### Autocorrelation

$\begin{aligned}
\rho_{x}(h)=\frac{\operatorname{Cov}\left(X_{t}, X_{t+h}\right)}{\sqrt{V(X_t)\cdot V(X_{t+h})}}
=\frac{\gamma_X(h)}{\sqrt{\gamma_X(0)\cdot \gamma_X(0)}}=\frac{\gamma_X(h)}{\gamma_X(h)}
\end{aligned}$

$\begin{aligned} \text{(a)} \quad \rho_{x}(0)=\frac{\gamma_{x}(0)}{\gamma_{x}(0)}=1 \rightarrow \operatorname{Corr}(X_t,X_t)
\end{aligned}$

$\begin{aligned} \text{(b)}\quad\rho_{x}(-h)=\rho_{x}(h) \quad\text{for all $h$}
\end{aligned}$

$\begin{aligned} \text{(c)}\quad-1\le\rho_{x}(h)\le1
\end{aligned}$



##### White Noise($a_t$, $WN(a_t)$)

- 백색잡음

(a) $E(a_t)=0$, 	$\forall t$ ->  all t를 뜻함

(b)  $V(a_t) = \sigma_a^2$, 	$\forall t$

(c) $Corr(a_t, a_s) = 0$,	 $t\not=s$

(d) $\gamma_a(h)=Cov(a_t, a_{t+h})=\begin{cases}\sigma_a^2,& h=0\\0,&h\not=0\end{cases}$ 
												

(e) $\rho_a(h) = \Large A$ 





