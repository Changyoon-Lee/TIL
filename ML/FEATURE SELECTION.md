# FEATURE SELECTION

출처 : https://www.youtube.com/watch?v=YaKMeAlHgqQ

## 1. percent missing values

- drop variables that have a very high % of missing values
  - num of records with missing values / num of total records
- create binary indicators to denote missing (or non-missing) values
- review or visualize varibles with high % of missing values

 

## 2. Amount of variation

- drop or review variables that have a very low variation
  - either standardize all varibles, or use standard deviation $\sigma$ to account for variables with differece scales
  - drop variables with zero variation (unary)

## 3. Pairwise correlation

- Many variables are often correlated with each other, and hence are redundant
- if two variables are highly correlated, keeping only one will help reduce dimensionality without much loss of information
  - which variable to keep? The one that has a highter correlation coefficient with the target

## 4. Multicolinearity

## 5. Principal Component Analysis(PCA)

- Dimensionality reduction technique which emphasizes vaiation.
- Eliminates multicollinearity - but explicability is compromised.
  - uses orthogonal transformation
- when to use:
  - Excessive multicollinearity
  - Explanation of the predictors is not important
  - A slight overhead in implementation is okay
  - More suitable for unsupervised learning

## 6. Cluster analysis

- This returns a pooled value for each cluster(i.e., the centorids), which can then be used to build a supervised learning model.
- In SAS, using PROC VARCLUS you can choose one variable from each cluster that is the most representative of that cluster.
  - use $1 - R^2$ ratio to elect a variable from each cluster.

## 7. Correlation (with the target)

- Drop variables that have a very low correlation with the target.
  - if a variable has a very low correlation with the target, it's not going to useful for the model (prediction)
  - 변수의 결합으로 의미가 있을 수 도 있기때문에 여러 조합을 사용해보면 좋긴함

## 8. Forward selection(-mlxtend)

- Identify the best variable (e.g., based on model accuracy)
- Add the next best variable into the model
- And so on until some predefined criteria is satisfied

## 9. Backward elimiantion(RFE)

- Start with all variables includes in the model
- Drop the least useful variable (e.g., based on the smallest drop in model accuracy)
- And so on until some predefined crieteria is satisfied.

## 10. Stepwise selection

- Similar to forward selection process, but a variable can also be droped if it's deemed as not useful any more after a certain number of steps

## 11. LASSO

- Least Absolute Shrinkage and Selection Operator
- Two birds, one stone: Variable Selection + Regularization
- 규제정도를 변화시키면서 

## 12. Tree-based selection







![image-20201029112827385](FEATURE SELECTION.assets/image-20201029112827385.png)



