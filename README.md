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
3. **Characters**: Creating features based on various character combinations: whitespaces, digits, Russian characters, non-Russian characters, word characters, punctuation, non-whitespace characters.

## Models

Seven different models were trained using different combinations of the extracted features:

1. **Model 1**: Named Entities
2. **Model 2.1**: Unique 5-gram POS Sequences (49,912 features)
3. **Model 2.2**: Common 5-gram POS Sequences (12 features)
4. **Model 3.1**: Whitespace characters (2 features)
5. **Model 3.2**: Digits (10 features)
6. **Model 3.3**: Russian characters (64 features)
7. **Model 3.4**: Non-Russian characters (53 features)
8. **Model 3.5**: Word characters (127 features)
9. **Model 3.6**: Punctuation (31 features)
10. **Model 3.7**: Non-whitespace characters (158 features)
12. **Model 4**: NER + Common 5-gram POS Sequences (17 features)
13. **Model 5**: All Features Combined (118 features)

## Evaluation

The models were evaluated using accuracy, precision, recall, and F1-score. The best-performing model was Model 7, which combined all features.

### Results (ranked by F1-score (weighted average))
1. **Model 3.7 (Non-whitespace characters):** 0.47
2. **Model 5 (all features):** 0.46
3. **Model 3.6 (Punctuation):** 0.41
4. **Model 3.5 (Word characters):** 0.37
5. **Model 3.3 (Russian characters):** 0.35
6. **Model 2.1 (all unique 5-gram POS sequences) (49912 features):** 0.34
7. **Model 4 (NER + Common 5-gram POS sequences):** 0.21
8. **Model 1 (NER)**: 0.17
9. **Model 2.2 (Common 5-gram POS sequences) (12 features)**: 0.15
10. **Model 3.4 (Non-Russian characters)**: 0.14
11. **Model 3.2 (Digits)**: 0.14
12. **Model 3.1 (Whitespaces)**: 0.12
13. **Dummy model**: 0.10



## Conclusion

This project successfully demonstrates the application of logistic regression for authorship attribution in Russian literature. The combination of multiple linguistic features leads to improved model performance, with the combined feature model achieving the highest scores.

For more details, please refer to the [project presentation](presentation/Authorship-attribution-for-Russian.pdf).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

For questions or collaboration, please contact [Artur Bondarenco](https://www.linkedin.com/in/artur-bondarenco-9b2768184/).
