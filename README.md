# Authorship Attribution for Russian

## Project Overview

This project focuses on authorship attribution for Russian literature using various machine learning models. The goal is to identify which of the four renowned Russian authors—Dostoevsky, Tolstoy, Gogol, or Chekhov—is most likely to have written a given sentence.

## Dataset

The dataset used for this project is sourced from Kaggle: [Russian Literature Dataset](https://www.kaggle.com/datasets/d0rj3228/russian-literature). The dataset consists of .txt files which were processed and converted into .csv files for training and testing purposes.

- **Training set**: 10,000 sentences (2,500 per author)
- **Test set**: 1,000 sentences (250 per author)

## Features

The following features were extracted from the text for model training:

1. **Named Entities (NER)**: Using SpaCy's Russian model which identifies PER, LOC, and ORG entities.
2. **5-gram POS Sequences**: Unique and common 5-gram parts of speech sequences.
3. **Punctuation**: Counting various punctuation marks in the text.
4. **Latin Characters**: Detection of Latin characters and special characters from French, German, and Ukrainian languages.

## Models

Seven different models were trained using different combinations of the extracted features:

1. **Model 1**: Named Entities
2. **Model 2 V1.0**: Unique 5-gram POS Sequences (49,912 features)
3. **Model 2 V2.0**: Common 5-gram POS Sequences (14 features)
4. **Model 3**: Punctuation (39 features)
5. **Model 4**: Latin Characters (62 features)
6. **Model 5**: Punctuation + Latin Characters (101 features)
7. **Model 6**: NER + Common 5-gram POS Sequences (17 features)
8. **Model 7**: All Features Combined (118 features)

## Evaluation

The models were evaluated using accuracy, precision, recall, and F1-score. The best-performing model was Model 7, which combined all features.

### Results (ranked by F1-score (weighted average))

1. **Model 7 (all features)**: 0.40
2. **Model 5 (Punctuation + Latin characters)**: 0.37
3. **Model 3 (Punctuation)**: 0.36
4. **Model 2 V 1.0 (all unique 5-gram POS sequences) (49912 features)**: 0.36
5. **Model 6 (NER + Common 5-gram POS sequences)**: 0.23
6. **Model 1 (NER)**: 0.19
7. **Model 2 V. 2.0 (Common 5-gram POS sequences) (14 features)**: 0.16
8. **Model 4 (Latin characters)**: 0.13
9. **Dummy model**: 0.10

## Conclusion

This project successfully demonstrates the application of logistic regression for authorship attribution in Russian literature. The combination of multiple linguistic features leads to improved model performance, with the combined feature model achieving the highest scores.

For more details, please refer to the [project presentation](presentation/Authorship-attribution-for-Russian.pdf).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

For questions or collaboration, please contact [Artur Bondarenco](mailto:artur.bondarenco@gmail.com).
