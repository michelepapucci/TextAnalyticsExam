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

Gender test set results:

              precision    recall  f1-score   support

        Male       0.88      0.93      0.91      3978
      Female       0.68      0.55      0.61      1077

    accuracy                           0.85      5055
    macro avg       0.78      0.74     0.76      5055
    weighted avg    0.84      0.85     0.84      5055

