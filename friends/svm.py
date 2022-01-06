from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix

# COMMENT THIS
def read_corpus(corpus_file, use_sentiment):
    documents = []
    labels = []
    with open(corpus_file, encoding='utf-8') as f:
        for line in f:
            tokens = line.strip().split()

            documents.append(tokens[3:])

            if use_sentiment:
                # 2-class problem: positive vs negative
                labels.append( tokens[1] )
            else:
                # 6-class problem: books, camera, dvd, health, music, software
                labels.append( tokens[0] )

    return documents, labels


# a dummy function that just returns its input
def identity(x):
    return x


def Multinomial_Naive_Bayes(trainDoc, trainClass, testDoc, testClass, tfIdf):

    # we use a dummy function as tokenizer and preprocessor,
    # since the texts are already preprocessed and tokenized.
    if tfIdf:
        vec = TfidfVectorizer(preprocessor = identity,
                              tokenizer = identity)
    else:
        vec = CountVectorizer(preprocessor = identity,
                              tokenizer = identity)

    # combine the vectorizer with a Naive Bayes classifier
    classifier = SVC(kernel='linear')


    # COMMENT THIS
    classifier.fit(trainDoc, trainClass)

    # COMMENT THIS
    testGuess = classifier.predict(testDoc)

    # COMMENT THIS
    accuracy = accuracy_score(testClass, testGuess)
    print("Accuracy = "+str(accuracy))

    # Showing the Confusion Matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(testClass, testGuess, labels=classifier.classes_)
    print(classifier.classes_)
    print(cm)
    print()


# this is the main function but you can name it anyway you want
def main():
    # COMMENT THIS
    DOC, LBL = read_corpus('dataset.txt', use_sentiment=True)

    # COMMENT THIS
    split_point = int(0.75*len(DOC))
    trainDoc = DOC[:split_point]
    trainClass = LBL[:split_point]
    testDoc = DOC[split_point:]
    testClass = LBL[split_point:]

    # Calling the classifier (let's use the TF-IDF vectorizer)
    Multinomial_Naive_Bayes(trainDoc, trainClass, testDoc, testClass, tfIdf=False)


# program starts from he
