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
|         Male |      0.79 |   0.99 |     0.88 |    3978 |
|       Female |      0.63 |   0.03 |     0.05 |    1076 |
|     accuracy |           |        |     0.79 |    5054 |
|    macro avg |      0.47 |   0.34 |     0.31 |    5054 |
| weighted avg |      0.76 |   0.79 |     0.70 |    5054 |


### 02.09.2022

IT5 Age test set results (with numeric labels):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.00 |   0.00 |     0.00 |     465 |
|        20-29 |      0.31 |   0.94 |     0.46 |    1534 |
|        30-39 |      0.39 |   0.02 |     0.04 |    1157 |
|        40-49 |      0.40 |   0.00 |     0.00 |     905 |
|       50-100 |      0.17 |   0.02 |     0.03 |     993 |
|     accuracy |           |        |     0.30 |    5054 |
|    macro avg |      0.21 |   0.16 |     0.09 |    5054 |
| weighted avg |      0.29 |   0.30 |     0.16 |    5054 |


IT5 Age test set results (with text labels):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|  adolescente |      0.12 |   0.14 |     0.13 |     465 |
|      giovane |      0.31 |   0.24 |     0.27 |    1534 |
|       adulto |      0.23 |   0.29 |     0.25 |    1157 |
|     mezzaetà |      0.19 |   0.14 |     0.16 |     905 |
|      anziano |      0.21 |   0.24 |     0.23 |     993 |
|     accuracy |           |        |     0.22 |    5054 |
|    macro avg |      0.18 |   0.17 |     0.17 |    5054 |
| weighted avg |      0.23 |   0.22 |     0.23 |    5054 |

IT5 Topic test set results:

|                 | precision | recall | f1-score | support |
|----------------:|----------:|-------:|---------:|--------:|
|              -1 |      0.00 |   0.00 |     0.00 |       0 |
|           anime |      0.43 |   0.54 |     0.48 |    1077 |
|   automobilismo |      0.39 |   0.43 |     0.41 |     985 |
|            bici |      0.00 |   0.01 |     0.01 |     155 |
|           sport |      0.41 |   0.57 |     0.48 |    1292 |
|          natura |      0.00 |   0.00 |     0.00 |     122 |
|         metalli |      0.67 |   0.01 |     0.02 |     348 |
|        medicina |      0.67 |   0.01 |     0.03 |     137 |
|       celebrità |      0.07 |   0.01 |     0.02 |     361 |
|            fumo |      0.63 |   0.26 |     0.37 |     377 |
| intrattenimento |      0.00 |   0.00 |     0.00 |     115 |
|      tecnologia |      0.00 |   0.00 |     0.00 |      85 |
|        accuracy |           |        |     0.37 |    5054 |
|       macro avg |      0.27 |   0.15 |     0.15 |    5054 |
|    weighted avg |      0.39 |   0.37 |     0.34 |    5054 |

### 03.09.2022

IT5 Topic multi-task test set results:

|                 |precision|   recall | f1-score| support|
|----------------:|--------:|---------:|--------:|-------:|
|              -1 |    0.00 |     0.00 |    0.00 |      0 |
|           anime |    0.48 |     0.64 |    0.55 |   1077 |
|   automobilismo |    0.55 |     0.59 |    0.57 |    985 |
|            bici |    0.50 |     0.01 |    0.01 |    155 |
|           sport |    0.54 |     0.66 |    0.60 |   1292 |
|          natura |    0.24 |     0.08 |    0.12 |    122 |
|         metalli |    0.24 |     0.19 |    0.21 |    348 |
|        medicina |    0.56 |     0.31 |    0.40 |    137 |
|       celebrità |    0.09 |     0.02 |    0.03 |    361 |
|            fumo |    0.50 |     0.48 |    0.49 |    377 |
| intrattenimento |    0.00 |     0.00 |    0.00 |    115 |
|      tecnologia |    0.00 |     0.00 |    0.00 |     85 |
|        accuracy |         |          |    0.48 |   5054 |
|       macro avg |    0.31 |     0.25 |    0.25 |   5054 |
|    weighted avg |    0.44 |     0.48 |    0.45 |   5054 |

IT5 Gender multi-task test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         uomo |      0.80 |   0.96 |     0.87 |    3978 |
|        donna |      0.38 |   0.06 |     0.11 |    1076 |
|     accuracy |           |        |     0.77 |    5054 |
|    macro avg |      0.39 |   0.34 |     0.33 |    5054 |
| weighted avg |      0.71 |   0.77 |     0.71 |    5054 |

IT5 Age multi-task test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.12 |   0.06 |     0.08 |     465 |
|        20-29 |      0.32 |   0.59 |     0.41 |    1534 |
|        30-39 |      0.24 |   0.12 |     0.16 |    1157 |
|        40-49 |      0.19 |   0.14 |     0.16 |     905 |
|       50-100 |      0.22 |   0.14 |     0.17 |     993 |
|     accuracy |           |        |     0.26 |    5054 |
|    macro avg |      0.18 |   0.17 |     0.16 |    5054 |
| weighted avg |      0.24 |   0.26 |     0.23 |    5054 |

### 05.09.2022

IT5 Topic Shuffled test set results (splittando l'input):

|                 | precision | recall | f1-score | support |
|-----------------|-----------|--------|----------|---------|
| -1              | 0.00      | 0.00   | 0.00     | 0       |
| anime           | 0.00      | 0.00   | 0.00     | 115     |
| automobilismo   | 0.00      | 0.00   | 0.00     | 85      |
| bici            | 0.00      | 0.00   | 0.00     | 361     |
| sport           | 0.21      | 0.24   | 0.24     | 1077    |
| natura          | 0.13      | 0.03   | 0.04     | 377     |
| metalli         | 0.00      | 0.00   | 0.00     | 122     |
| medicina        | 0.00      | 0.00   | 0.00     | 155     |
| celebrità       | 0.18      | 0.28   | 0.22     | 985     |
| fumo            | 0.00      | 0.00   | 0.00     | 137     |
| intrattenimento | 0.05      | 0.04   | 0.05     | 348     |
| tecnologia      | 0.26      | 0.35   | 0.30     | 1292    |
| accuracy        |           |        | 0.20     | 5054    |
| macro avg       | 0.06      | 0.08   | 0.07     | 5054    |
| weighted avg    | 0.15      | 0.20   | 0.17     | 5054    |

### 06.09.2022

IT5 Topic test set results (splittando l'input):

|                 | precision | recall | f1-score | support |
|-----------------|-----------|--------|----------|---------|
| -1              | 0.00      | 0.00   | 0.00     | 0       |
| anime           | 0.43      | 0.76   | 0.55     | 1077    |
| automobilismo   | 0.38      | 0.77   | 0.51     | 985     |
| bici            | 0.00      | 0.00   | 0.00     | 155     |
| sport           | 0.70      | 0.50   | 0.58     | 1292    |
| natura          | 0.00      | 0.00   | 0.00     | 122     |
| metalli         | 0.60      | 0.01   | 0.02     | 348     |
| medicina        | 1.00      | 0.01   | 0.03     | 137     |
| celebrità       | 0.00      | 0.00   | 0.00     | 361     |
| fumo            | 0.90      | 0.40   | 0.55     | 377     |
| intrattenimento | 0.00      | 0.00   | 0.00     | 115     |
| tecnologia      | 0.00      | 0.00   | 0.00     | 85      |
| accuracy        |           |        | 0.47     | 5054    |
| macro avg       | 0.33      | 0.20   | 0.19     | 5054    |
| weighted avg    | 0.48      | 0.47   | 0.41     | 5054    |

IT5 Multi task Topic test set results (splittando l'input):

|                 | precision | recall | f1-score | support |
|-----------------|-----------|--------|----------|---------|
| -1              | 0.00      | 0.00   | 0.00     | 0       |
| anime           | 0.51      | 0.81   | 0.62     | 1077    |
| automobilismo   | 0.56      | 0.70   | 0.62     | 985     |
| bici            | 0.00      | 0.00   | 0.00     | 155     |
| sport           | 0.66      | 0.67   | 0.66     | 1292    |
| natura          | 0.41      | 0.14   | 0.21     | 122     |
| metalli         | 0.35      | 0.34   | 0.35     | 348     |
| medicina        | 0.70      | 0.52   | 0.59     | 137     |
| celebrità       | 0.67      | 0.01   | 0.01     | 361     |
| fumo            | 0.75      | 0.51   | 0.61     | 377     |
| intrattenimento | 0.00      | 0.00   | 0.00     | 115     |
| tecnologia      | 0.00      | 0.00   | 0.00     | 85      |
| accuracy        |           |        | 0.56     | 5054    |
| macro avg       | 0.38      | 0.31   | 0.31     | 5054    |
| weighted avg    | 0.54      | 0.56   | 0.52     | 5054    |

BERT Multitask Topic:

                         precision    recall  f1-score   support
    
                  ANIME       0.65      0.81      0.72      1078
              AUTO-MOTO       0.62      0.74      0.68       985
                  BIKES       0.00      0.00      0.00       155
            CELEBRITIES       0.68      0.61      0.64       361
          ENTERTAINMENT       0.70      0.33      0.45       115
    MEDICINE-AESTHETICS       0.70      0.54      0.61       137
        METAL-DETECTING       0.56      0.51      0.53       348
                 NATURE       0.61      0.47      0.53       122
                  SMOKE       0.71      0.69      0.70       377
                 SPORTS       0.73      0.73      0.73      1292
             TECHNOLOGY       0.00      0.00      0.00        85
    
               accuracy                           0.67      5055
              macro avg       0.54      0.49      0.51      5055
           weighted avg       0.64      0.67      0.65      5055


BERT Multitask Age

                  precision    recall  f1-score   support
    
            0-19       0.40      0.22      0.29       465
           20-29       0.38      0.59      0.46      1534
           30-39       0.26      0.16      0.19      1157
           40-49       0.22      0.22      0.22       905
          50-100       0.35      0.28      0.31       994
    
        accuracy                           0.33      5055
       macro avg       0.32      0.29      0.29      5055
    weighted avg       0.32      0.33      0.31      5055


BERT Multitask Gender
    
                  precision    recall  f1-score   support
    
               M       0.87      0.94      0.91      3978
               F       0.70      0.50      0.58      1077
    
        accuracy                           0.85      5055
       macro avg       0.79      0.72      0.74      5055
    weighted avg       0.84      0.85      0.84      5055

### 07.09.2022

IT5 Gender shuffled test set results:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.00      | 0.00   | 0.00     | 0       |
| uomo         | 0.10      | 0.00   | 0.01     | 1076    |
| donna        | 0.79      | 0.99   | 0.88     | 3978    |
| accuracy     |           |        | 0.78     | 5054    |
| macro avg    | 0.30      | 0.33   | 0.29     | 5054    |
| weighted avg | 0.64      | 0.78   | 0.69     | 5054    |

### 13.09.2022

Dummy classifier Topic test set results (stratified):

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|               ANIME |      0.21 |   0.22 |     0.21 |    1078 |
|           AUTO-MOTO |      0.19 |   0.20 |     0.19 |     985 |
|               BIKES |      0.02 |   0.02 |     0.02 |     155 |
|              SPORTS |      0.27 |   0.28 |     0.27 |    1292 |
|              NATURE |      0.03 |   0.03 |     0.03 |     122 |
|     METAL-DETECTING |      0.08 |   0.08 |     0.08 |     348 |
| MEDICINE-AESTHETICS |      0.02 |   0.01 |     0.02 |     137 |
|         CELEBRITIES |      0.07 |   0.06 |     0.06 |     361 |
|               SMOKE |      0.09 |   0.10 |     0.09 |     377 |
|       ENTERTAINMENT |      0.01 |   0.01 |     0.01 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.17 |    5055 |
|           macro avg |      0.09 |   0.09 |     0.09 |    5055 |
|        weighted avg |      0.17 |   0.17 |     0.17 |    5055 |


Dummy classifier Age test set results (stratified):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|         0-19 |      0.09 |   0.12 |     0.10 |     465 |
|        20-29 |      0.32 |   0.31 |     0.31 |    1534 |
|        30-39 |      0.23 |   0.20 |     0.22 |    1157 |
|        40-49 |      0.15 |   0.17 |     0.16 |     905 |
|       50-100 |      0.20 |   0.19 |     0.20 |     994 |
|     accuracy |           |        |     0.22 |    5055 |
|    macro avg |      0.20 |   0.20 |     0.20 |    5055 |
| weighted avg |      0.22 |   0.22 |     0.22 |    5055 |


Dummy classifier Gender test set results (stratified):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|            M |      0.79 |   0.83 |     0.81 |    3978 |
|            F |      0.22 |   0.18 |     0.19 |    1077 |
|     accuracy |           |        |     0.69 |    5055 |
|    macro avg |      0.50 |   0.50 |     0.50 |    5055 |
| weighted avg |      0.67 |   0.69 |     0.68 |    5055 |

Dummy classifier Topic test set results (most frequent):

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|               ANIME |      0.00 |   0.00 |     0.00 |    1078 |
|           AUTO-MOTO |      0.00 |   0.00 |     0.00 |     985 |
|               BIKES |      0.00 |   0.00 |     0.00 |     155 |
|              SPORTS |      0.26 |   1.00 |     0.41 |    1292 |
|              NATURE |      0.00 |   0.00 |     0.00 |     122 |
|     METAL-DETECTING |      0.00 |   0.00 |     0.00 |     348 |
| MEDICINE-AESTHETICS |      0.00 |   0.00 |     0.00 |     137 |
|         CELEBRITIES |      0.00 |   0.00 |     0.00 |     361 |
|               SMOKE |      0.00 |   0.00 |     0.00 |     377 |
|       ENTERTAINMENT |      0.00 |   0.00 |     0.00 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.26 |    5055 |
|           macro avg |      0.02 |   0.09 |     0.04 |    5055 |
|        weighted avg |      0.07 |   0.26 |     0.10 |    5055 |

Dummy classifier Age test set results (most frequent):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|         0-19 |      0.00 |   0.00 |     0.00 |     465 |
|        20-29 |      0.30 |   1.00 |     0.47 |    1534 |
|        30-39 |      0.00 |   0.00 |     0.00 |    1157 |
|        40-49 |      0.00 |   0.00 |     0.00 |     905 |
|       50-100 |      0.00 |   0.00 |     0.00 |     994 |
|     accuracy |           |        |     0.30 |    5055 |
|    macro avg |      0.06 |   0.20 |     0.09 |    5055 |
| weighted avg |      0.09 |   0.30 |     0.14 |    5055 |

Dummy classifier Gender test set results (most frequent):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|            M |      0.79 |   1.00 |     0.88 |    3978 |
|            F |      0.00 |   0.00 |     0.00 |    1077 |
|     accuracy |           |        |     0.79 |    5055 |
|    macro avg |      0.39 |   0.50 |     0.44 |    5055 |
| weighted avg |      0.62 |   0.79 |     0.69 |    5055 |

### 14.09
Gender with m and f labels test set results:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.00      | 0.00   | 0.00     | 0       |
| 0            | 0.79      | 0.97   | 0.87     | 3978    |
| 1            | 0.35      | 0.05   | 0.08     | 1076    |
| accuracy     |           |        | 0.78     | 5054    |
| macro avg    | 0.38      | 0.34   | 0.32     | 5054    |
| weighted avg | 0.70      | 0.78   | 0.70     | 5054    |


### 21.09
T5 Shuffled Age test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.24 |   0.07 |     0.11 |    1157 |
|        20-29 |      0.18 |   0.28 |     0.22 |     905 |
|        30-39 |      0.20 |   0.61 |     0.30 |     993 |
|        40-49 |      0.00 |   0.00 |     0.00 |     465 |
|       50-100 |      0.00 |   0.00 |     0.00 |    1534 |
|     accuracy |           |        |     0.19 |    5054 |
|    macro avg |      0.10 |   0.16 |     0.10 |    5054 |
| weighted avg |      0.13 |   0.19 |     0.12 |    5054 |

IT5 Topic multi-task test set results (randomizing input):

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|                  -1 |      0.00 |   0.00 |     0.00 |       0 |
|               ANIME |      0.65 |   0.41 |     0.50 |    1077 |
|           AUTO-MOTO |      0.56 |   0.52 |     0.54 |     985 |
|               BIKES |      0.25 |   0.01 |     0.02 |     155 |
|              SPORTS |      0.54 |   0.58 |     0.56 |    1292 |
|              NATURE |      0.14 |   0.13 |     0.13 |     122 |
|     METAL-DETECTING |      0.29 |   0.14 |     0.19 |     348 |
| MEDICINE-AESTHETICS |      0.52 |   0.30 |     0.38 |     137 |
|         CELEBRITIES |      0.11 |   0.07 |     0.08 |     361 |
|               SMOKE |      0.49 |   0.42 |     0.46 |     377 |
|       ENTRATEINMENT |      0.07 |   0.03 |     0.04 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.39 |    5054 |
|           macro avg |      0.30 |   0.22 |     0.24 |    5054 |
|        weighted avg |      0.48 |   0.39 |     0.42 |    5054 |

IT5 Age multi-task test set results (randomizing input):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.07 |   0.03 |     0.04 |     465 |
|        20-29 |      0.31 |   0.59 |     0.41 |    1534 |
|        30-39 |      0.24 |   0.15 |     0.18 |    1157 |
|        40-49 |      0.22 |   0.16 |     0.18 |     905 |
|       50-100 |      0.20 |   0.11 |     0.14 |     993 |
|     accuracy |           |        |     0.26 |    5054 |
|    macro avg |      0.17 |   0.17 |     0.16 |    5054 |
| weighted avg |      0.23 |   0.26 |     0.23 |    5054 |


IT5 Gender multi-task test set results (randomizing input):

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|            M |      0.80 |   0.96 |     0.87 |    3978 |
|            F |      0.40 |   0.07 |     0.11 |    1076 |
|     accuracy |           |        |     0.77 |    5054 |
|    macro avg |      0.40 |   0.34 |     0.33 |    5054 |
| weighted avg |      0.71 |   0.77 |     0.71 |    5054 |

### 22.09

T5 1 shot learning Age test set results:
|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.00 |   0.00 |     0.00 |     465 |
|        20-29 |      0.32 |   0.02 |     0.04 |    1534 |
|        30-39 |      0.10 |   0.00 |     0.00 |    1157 |
|        40-49 |      0.25 |   0.00 |     0.00 |     905 |
|       50-100 |      0.00 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.01 |    5054 |
|    macro avg |      0.11 |   0.00 |     0.01 |    5054 |
| weighted avg |      0.17 |   0.01 |     0.01 |    5054 |

T5 2 shot learning Age test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.13 |   0.02 |     0.03 |     465 |
|        20-29 |      0.30 |   0.17 |     0.22 |    1534 |
|        30-39 |      0.22 |   0.08 |     0.12 |    1157 |
|        40-49 |      0.17 |   0.06 |     0.09 |     905 |
|       50-100 |      0.00 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.08 |    5054 |
|    macro avg |      0.14 |   0.06 |     0.08 |    5054 |
| weighted avg |      0.18 |   0.08 |     0.11 |    5054 |

T5 3 shot learning Age test set results:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.10 |   0.05 |     0.07 |     465 |
|        20-29 |      0.30 |   0.27 |     0.29 |    1534 |
|        30-39 |      0.23 |   0.13 |     0.17 |    1157 |
|        40-49 |      0.18 |   0.16 |     0.17 |     905 |
|       50-100 |      1.00 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.15 |    5054 |
|    macro avg |      0.30 |   0.10 |     0.12 |    5054 |
| weighted avg |      0.38 |   0.15 |     0.16 |    5054 |








