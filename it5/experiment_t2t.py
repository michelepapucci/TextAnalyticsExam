import t2t


def test(trainer):
    import pandas as pd
    df = pd.read_csv("src/data/post_processed/test_1_filtered.csv")
    with open("predictions.tsv", "w") as file:
        file.write("y_true\ty_pred\n")
        for index, row in df.iterrows():
            sentence = "Classifica genere: " + row['Sentence']
            output = trainer.generate_single(sentence, max_length=8)
            file.write(f"{row['Gender']}\t{output}\n")


def main():
    trainer_arguments = t2t.TrainerArguments(
        # model
        model_name_or_path="gsarti/it5-base",
        # data inputs
        train_file="dataset.json",
        max_source_length=128,
        max_target_length=8,
        # taining outputs
        output_dir="/it5-gender",
        overwrite_output_dir=True,
        # training settings
        num_train_epochs=   2,
        per_device_train_batch_size=8,
        learning_rate=1e-5,
        prefix="Classifica genere: ",
        # validation settings
        per_device_eval_batch_size=8,
        evaluation_strategy="epoch",
    )

    trainer = t2t.Trainer(arguments=trainer_arguments)

    trainer.train(valid=False)

    return trainer


if __name__ == "__main__":
    trainer = main()
    test(trainer)
