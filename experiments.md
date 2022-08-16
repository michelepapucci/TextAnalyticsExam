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
