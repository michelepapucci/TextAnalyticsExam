from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("mpapucci/it5-gender-classification-tag-it")
model = AutoModelForSeq2SeqLM.from_pretrained("mpapucci/it5-gender-classification-tag-it")

df = pd.read_csv("test_1_filtered.csv")
with open("predictions.tsv", "w") as file:
    file.write("y_true\ty_pred\n")
    for index, row in df.iterrows():
        sentence = "Classifica genere: " + row['Sentence']
        input_ids = tokenizer(sentence, return_tensors="pt").input_ids
        output = model.generate(input_ids)
        text_out = tokenizer.decode(output[0], skip_special_tokens=True)

        if text_out == 'uomo':
            y_pred = 0
        elif text_out == 'donna':
            y_pred = 1
        else:
            y_pred = -1

        if row['Gender'] == 'M':
            y_true = 0
        else:
            y_true = 1

        file.write(f"{y_true}\t{y_pred}\n")
        print(f"{index}: {row['Gender']} - {text_out}")
# Try batching
