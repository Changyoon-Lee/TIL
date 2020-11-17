# ARIMA model

[![](https://img.shields.io/static/v1?label=required&message=mermaid&color=blueviolet)](https://chrome.google.com/webstore/detail/github-%2B-mermaid/goiiopgdnkogdbjmncgedmgpoajilohe/related?hl=en)

##### 참고자료 : 김성범교수 Youtube



##### Box-Jenkins ARIMA Procedure

```flow
A=>operation: Data Preprocessing
(transformation, differencing)
B=>operation: Identify Model to be 
Tentatively Entertained

C=>operation: Estimate Parameters
D=>condition: Diagnosis Check
E=>operation: Use Model to Forecast

A->B->C->D
D(no)->B
D(yes)->E
```

## 1. data processing

#### ACF - check stationarity

- lag 0 일때는 항상 1(자기자신이기때문)

- nonstationary process 의 경우  ACF가 전반적으로 천천히 떨어지는 양상을 보임

- stationary process의 경우 급격히 떨어지거나 패턴이 없다



#### nonstationary -> stationary 바꿔 줘야함

- 차분

$$
Y_t = \Delta{X_t}=X_t - X_{t-1}
$$



## 2. Identification ARIMA model

- **Graphical method**(주관적임) : making inferences from the patterns of the sample autocorrelation and partial autocorrelation functions of the series

- 시범적으로 결정을 해보는 방식

|   Model   |                            ACF                             |                         Partial ACF                          |
| :-------: | :--------------------------------------------------------: | :----------------------------------------------------------: |
|   MA(q)   |       Cut off after lag q<br>(q시차 이후 0으로 절단)       | Die out<br />(지수적으로 감소, <br />소멸하는 sine함수 형태) |
|   AR(p)   | Die out<br >(지수적으로 감소,<br />소멸하는 sine함수 형태) |       Cut off after lag p<br />(p시차 이후 0으로 절단)       |
| ARMA(p,q) |          Die out<br />(시차 (q-p)이후 부터 소멸)           |           Die out<br />(시차 (q-p)이후 부터 소멸)            |



