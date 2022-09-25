## T5 few shots learning

### 23/09

T5 Age 1shot learning test predictions:
|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.00 |   0.00 |     0.00 |     465 |
|        20-29 |      0.30 |   0.03 |     0.06 |    1534 |
|        30-39 |      0.23 |   0.00 |     0.01 |    1157 |
|        40-49 |      0.11 |   0.00 |     0.00 |     905 |
|       50-100 |      0.00 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.01 |    5054 |
|    macro avg |      0.11 |   0.01 |     0.01 |    5054 |
| weighted avg |      0.16 |   0.01 |     0.02 |    5054 |

T5 Age 2shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.14 |   0.04 |     0.06 |     465 |
|        20-29 |      0.32 |   0.21 |     0.25 |    1534 |
|        30-39 |      0.20 |   0.05 |     0.09 |    1157 |
|        40-49 |      0.20 |   0.15 |     0.17 |     905 |
|       50-100 |      0.00 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.11 |    5054 |
|    macro avg |      0.14 |   0.08 |     0.09 |    5054 |
| weighted avg |      0.19 |   0.11 |     0.13 |    5054 |

T5 Age 3shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         0-19 |      0.08 |   0.05 |     0.06 |     465 |
|        20-29 |      0.31 |   0.34 |     0.32 |    1534 |
|        30-39 |      0.20 |   0.09 |     0.13 |    1157 |
|        40-49 |      0.20 |   0.22 |     0.21 |     905 |
|       50-100 |      0.33 |   0.00 |     0.00 |     993 |
|     accuracy |           |        |     0.17 |    5054 |
|    macro avg |      0.19 |   0.12 |     0.12 |    5054 |
| weighted avg |      0.25 |   0.17 |     0.17 |    5054 |

T5 Age 4 shot learning test predictions:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| -1           | 0.00      | 0.00   | 0.00     | 0       |
| 0-19         | 0.12      | 0.05   | 0.07     | 465     |
| 20-29        | 0.30      | 0.49   | 0.37     | 1534    |
| 30-39        | 0.23      | 0.14   | 0.17     | 1157    |
| 40-49        | 0.19      | 0.20   | 0.20     | 905     |
| 50-100       | 0.19      | 0.05   | 0.08     | 993     |
| accuracy     |           |        | 0.23     | 5054    |
| macro avg    | 0.17      | 0.15   | 0.15     | 5054    |
| weighted avg | 0.23      | 0.23   | 0.21     | 5054    |

T5 Gender 1 shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         uomo |      0.00 |   0.00 |     0.00 |    3978 |
|        donna |      0.00 |   0.00 |     0.00 |    1076 |
|     accuracy |           |        |     0.00 |    5054 |
|    macro avg |      0.00 |   0.00 |     0.00 |    5054 |
| weighted avg |      0.00 |   0.00 |     0.00 |    5054 |

T5 Gender 2 shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         uomo |      0.00 |   0.00 |     0.00 |    3978 |
|        donna |      0.00 |   0.00 |     0.00 |    1076 |
|     accuracy |           |        |     0.00 |    5054 |
|    macro avg |      0.00 |   0.00 |     0.00 |    5054 |
| weighted avg |      0.00 |   0.00 |     0.00 |    5054 |

T5 Gender 3 shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         uomo |      0.00 |   0.00 |     0.00 |    3978 |
|        donna |      0.40 |   0.00 |     0.01 |    1076 |
|     accuracy |           |        |     0.00 |    5054 |
|    macro avg |      0.13 |   0.00 |     0.00 |    5054 |
| weighted avg |      0.09 |   0.00 |     0.00 |    5054 |

T5 Gender 4 shot learning test predictions:

|              | precision | recall | f1-score | support |
|-------------:|----------:|-------:|---------:|--------:|
|           -1 |      0.00 |   0.00 |     0.00 |       0 |
|         uomo |      0.87 |   0.03 |     0.05 |    3978 |
|        donna |      0.21 |   0.98 |     0.35 |    1076 |
|     accuracy |           |        |     0.23 |    5054 |
|    macro avg |      0.36 |   0.34 |     0.13 |    5054 |
| weighted avg |      0.73 |   0.23 |     0.11 |    5054 |

T5 Topic 1 shot learning test predictions:

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|                  -1 |      0.00 |   0.00 |     0.00 |       0 |
|               ANIME |      0.00 |   0.00 |     0.00 |    1077 |
|           AUTO-MOTO |      0.00 |   0.00 |     0.00 |     985 |
|               BIKES |      0.00 |   0.00 |     0.00 |     155 |
|         CELEBRITIES |      0.00 |   0.00 |     0.00 |    1292 |
|       ENTERTAINMENT |      0.00 |   0.00 |     0.00 |     122 |
| MEDICINE-AESTHETICS |      0.00 |   0.00 |     0.00 |     348 |
|     METAL-DETECTING |      0.00 |   0.00 |     0.00 |     137 |
|              NATURE |      0.00 |   0.00 |     0.00 |     361 |
|               SMOKE |      0.00 |   0.00 |     0.00 |     377 |
|              SPORTS |      0.00 |   0.00 |     0.00 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.00 |    5054 |
|           macro avg |      0.00 |   0.00 |     0.00 |    5054 |
|        weighted avg |      0.00 |   0.00 |     0.00 |    5054 |

T5 Topic 2 shot learning test predictions:

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|                  -1 |      0.00 |   0.00 |     0.00 |       0 |
|               ANIME |      0.00 |   0.00 |     0.00 |    1077 |
|           AUTO-MOTO |      0.00 |   0.00 |     0.00 |     985 |
|               BIKES |      0.00 |   0.00 |     0.00 |     155 |
|         CELEBRITIES |      0.00 |   0.00 |     0.00 |    1292 |
|       ENTERTAINMENT |      0.00 |   0.00 |     0.00 |     122 |
| MEDICINE-AESTHETICS |      0.00 |   0.00 |     0.00 |     348 |
|     METAL-DETECTING |      0.00 |   0.00 |     0.00 |     137 |
|              NATURE |      0.50 |   0.01 |     0.01 |     361 |
|               SMOKE |      0.00 |   0.00 |     0.00 |     377 |
|              SPORTS |      0.00 |   0.00 |     0.00 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.00 |    5054 |
|           macro avg |      0.04 |   0.00 |     0.00 |    5054 |
|        weighted avg |      0.04 |   0.00 |     0.00 |    5054 |

T5 Topic 3 shot learning test predictions:

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|                  -1 |      0.00 |   0.00 |     0.00 |       0 |
|               ANIME |      0.00 |   0.00 |     0.00 |    1077 |
|           AUTO-MOTO |      0.00 |   0.00 |     0.00 |     985 |
|               BIKES |      0.00 |   0.00 |     0.00 |     155 |
|         CELEBRITIES |      0.00 |   0.00 |     0.00 |    1292 |
|       ENTERTAINMENT |      0.00 |   0.00 |     0.00 |     122 |
| MEDICINE-AESTHETICS |      0.00 |   0.00 |     0.00 |     348 |
|     METAL-DETECTING |      0.00 |   0.00 |     0.00 |     137 |
|              NATURE |      0.04 |   0.01 |     0.02 |     361 |
|               SMOKE |      0.00 |   0.00 |     0.00 |     377 |
|              SPORTS |      0.00 |   0.00 |     0.00 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.00 |    5054 |
|           macro avg |      0.04 |   0.00 |     0.00 |    5054 |
|        weighted avg |      0.04 |   0.00 |     0.00 |    5054 |

T5 Topic 4 shot learning test predictions:

|                     | precision | recall | f1-score | support |
|--------------------:|----------:|-------:|---------:|--------:|
|                  -1 |      0.00 |   0.00 |     0.00 |       0 |
|               ANIME |      0.43 |   0.55 |     0.48 |    1077 |
|           AUTO-MOTO |      0.45 |   0.50 |     0.47 |     985 |
|               BIKES |      0.00 |   0.00 |     0.00 |     155 |
|         CELEBRITIES |      0.44 |   0.60 |     0.51 |    1292 |
|       ENTERTAINMENT |      0.00 |   0.00 |     0.00 |     122 |
| MEDICINE-AESTHETICS |      0.28 |   0.06 |     0.10 |     348 |
|     METAL-DETECTING |      0.00 |   0.00 |     0.00 |     137 |
|              NATURE |      0.08 |   0.02 |     0.03 |     361 |
|               SMOKE |      0.44 |   0.34 |     0.39 |     377 |
|              SPORTS |      0.08 |   0.01 |     0.02 |     115 |
|          TECHNOLOGY |      0.00 |   0.00 |     0.00 |      85 |
|            accuracy |           |        |     0.40 |    5054 |
|           macro avg |      0.18 |   0.17 |     0.17 |    5054 |
|        weighted avg |      0.35 |   0.40 |     0.36 |    5054 |
