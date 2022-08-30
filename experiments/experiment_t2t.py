import t2t


def main():
    trainer_arguments = t2t.TrainerArguments(
        # model
        model_name_or_path="../models/it5"
    )
    trainer = t2t.Trainer(arguments=trainer_arguments)
    input_text = "Classifica genere: Shell 113 alle poste. Domani mattina ritiro. Ciao!"
    trainer.generate_single(input_text, max_length=8)


if __name__ == "__main__":
    main()
