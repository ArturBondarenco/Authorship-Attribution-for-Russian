import numpy
from collections import Counter

def predict_new(i, data_for_prediction, features=None):
    # print sentences
    print(data_for_prediction[0][i])
    # print the features of the index
    print(data_for_prediction[1][i])
    # print all entity types
    if features:
      print(features)
    # print the correct label of the index
    print(data_for_prediction[2][i])

    print()
    print("Prediction:")
    lr_model = data_for_prediction[3]
    # print the prediction for the features of this index
    print(lr_model.predict([data_for_prediction[1][i]]))
    # print the probabilities for each label predictions
    print(lr_model.predict_proba([data_for_prediction[1][i]]))
    print("--------------------------------------------------------")
    print()

def predict2(test_predictions, test_authors, m=0, n=10):
  for prediction, author in zip(test_predictions[m:n], test_authors[m:n]):
    if prediction == author:
        result_is = "Correct"
    else:
        result_is = "Incorrect"
    print(f"{prediction} ({result_is}:{author})")

def model_analysis2(lr_model, features, top_n=5):
    for label, coefs, intercept in zip(lr_model.classes_, lr_model.coef_, lr_model.intercept_):
        print(f"Class: {label}")

        # First get the absolute values for the coeficients
        absolute_coefs = numpy.abs(coefs)
        # Get an array of indices that will sort the absolute coefficients
        indices = numpy.argsort(absolute_coefs)
        # Slice the array to only get the indices of the top N absolute coefficients
        top_indices = indices[-top_n:]
        # Reverse the order to get descending order of absolute values
        reversed_top_indices = top_indices[::-1]

        # Print the top features and their coefficients
        for idx in reversed_top_indices:
            print(f"Feature: {features[idx]}, Coefficient: {coefs[idx]:.4f}")

        print(f"Intercept: {intercept:.4f}")
        print()

def fivegram_pos_extractor_from_sentence(doc):
    n = 5
    fivegram_pos_tags = set()
    for i in range(len(doc) - n + 1):
    # Extract the tokens for the current fivegram
        fivegram_tokens = doc[i : i + n]
        # Extract the POS tags of the tokens and add the POS tag combination to the list
        fivegram_pos = tuple(token.pos_ for token in fivegram_tokens)
        fivegram_pos_tags.add(fivegram_pos)
    unique_fivegram_pos_tags = list(fivegram_pos_tags)

    return unique_fivegram_pos_tags

def fivegram_pos_extractor_unique(list_of_doc_sentences):
    all_fivegram_pos_tags = set()
    for doc in list_of_doc_sentences:
        # Extract unique five-gram POS tags from the current sentence
        doc_fivegrams = fivegram_pos_extractor_from_sentence(doc)
        # Add them to the set
        all_fivegram_pos_tags.update(doc_fivegrams)
    return list(all_fivegram_pos_tags)