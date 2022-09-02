## Experiments & Notes

### 29.07.2022
Il dataset è stato parsato in csv ed è stato filtrato di tutte le frasi che contengono < 10 token.  
Numero di frasi **prima** del filtraggio: 26098  
Numero di frasi **dopo** il filtraggio: 13553  
Valutare se fare un filtraggio anche sulla lunghezza massima o lasciar spezzare a BERT.  


### 03.08.2022
Primo BERT addestrato su Gender, risultati su evaluation set:  
`{'eval_loss': 0.16035252809524536, 'eval_accuracy': 0.9513094798967171, 'eval_runtime': 7.2739, 
'eval_samples_per_second': 372.703, 'eval_steps_per_second': 46.605, 'epoch': 2.0}`

### 17.08.2022
ROC curve funzionante, anche se i risultati sono strani.

Bert Gender test set results:

              precision    recall  f1-score   support

        Male       0.88      0.93      0.91      3978
      Female       0.68      0.55      0.61      1077

    accuracy                           0.85      5055
    macro avg       0.78      0.74     0.76      5055
    weighted avg    0.84      0.85     0.84      5055


### 21.08.2022

Bert Topic test set result:

                         precision    recall  f1-score   support
    
                  ANIME       0.68      0.79      0.73      1078
              AUTO-MOTO       0.66      0.72      0.69       985
                  BIKES       0.00      0.00      0.00       155
            CELEBRITIES       0.69      0.58      0.63       361
          ENTERTAINMENT       0.57      0.34      0.43       115
    MEDICINE-AESTHETICS       0.66      0.58      0.62       137
        METAL-DETECTING       0.54      0.51      0.53       348
                 NATURE       0.61      0.44      0.51       122
                  SMOKE       0.67      0.68      0.67       377
                 SPORTS       0.68      0.76      0.72      1292
             TECHNOLOGY       1.00      0.01      0.02        85
    
               accuracy                           0.66      5055
              macro avg       0.62      0.49      0.50      5055
           weighted avg       0.65      0.66      0.64      5055


### 23.08.2022

Bert Age test set results:

                  precision    recall  f1-score   support
    
            0-19       0.38      0.29      0.33       465
           20-29       0.38      0.55      0.45      1534
           30-39       0.27      0.23      0.25      1157
           40-49       0.24      0.23      0.24       905
          50-100       0.41      0.26      0.32       994
    
        accuracy                           0.34      5055
       macro avg       0.34      0.31      0.32      5055
    weighted avg       0.34      0.34      0.33      5055


### 01.09.2022

IT5 Gender test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|            0 |      0.79 |   0.99 |     0.88 |    3978 |
|            1 |      0.63 |   0.03 |     0.05 |    1076 |
|     accuracy |      0.79 |   5054 |          |         |
|    macro avg |      0.47 |   0.34 |     0.31 |    5054 |
| weighted avg |      0.76 |   0.79 |     0.70 |    5054 |


### 02.09.2022

IT5 Age test set results (with numeric labels):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|            0 |      0.00 |   0.00 |     0.00 |     465 |
|            1 |      0.31 |   0.94 |     0.46 |    1534 |
|            2 |      0.39 |   0.02 |     0.04 |    1157 |
|            3 |      0.40 |   0.00 |     0.00 |     905 |
|            4 |      0.17 |   0.02 |     0.03 |     993 |
|     accuracy |           |        |     0.30 |    5054 |
|    macro avg |      0.21 |   0.16 |     0.09 |    5054 |
| weighted avg |      0.29 |   0.30 |     0.16 |    5054 |

