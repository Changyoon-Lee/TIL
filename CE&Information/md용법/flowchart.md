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







```mermaid
graph LR
MyApp --> DB(<font color=white>fa:fa-database MySQL)
style DB fill:#00758f
```

```mermaid
graph LR
   id1[Rectangle] -->|comment in line| id2((Circle))
   id2 --> C{diamond}
   C -->|Laptop| D[fa:fa-laptop Laptop icon]
   C ==>|Phone| E[fa:fa-mobile Phone icon]
   C -->|Car| F[fa:fa-car Car icon]
   id1===C


    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#ccf,stroke:#f66,stroke-width:8px,stroke-dasharray: 1, 10
```

```mermaid

```

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid
        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d
        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d
```

```mermaid
graph LR
MyApp --> DB(<font color=white>fa:fa-database MySQL)
style DB fill:#00758f
```

