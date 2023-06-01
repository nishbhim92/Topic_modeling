# Topic Modeling Using Top2Vec

This Python script utilizes the Top2Vec algorithm to perform topic modeling on a collection of documents.

## Installation

This project requires Python 3.x and the following Python libraries installed:

[pandas](https://pandas.pydata.org)
[Top2Vec](https://github.com/ddangelov/Top2Vec)
You can install these packages via pip:
pip install pandas
pip install top2vec


## File Descriptions

topic_modeling.py: This is the main file where the topic modeling is performed.

## Data

The dataset is an Excel file ('ABS.xlsx') with a column 'Abstract' containing textual data to be analyzed.

## How to Run

Run the topic_modeling.py file in a terminal: python topic_modeling.py
## Code Overview

The script performs the following steps:

Import necessary libraries.
Load data from an Excel file.
Select the 'Abstract' column and transform it into a list of documents.
Train a Top2Vec model on the documents.
Analyze the topics, and print the total number of topics and their sizes.
Perform hierarchical topic reduction, reducing the number of topics to 1.
Print the number and words of each topic.
Search the documents that belong to topic number 0 and get the top 10.
Print the document ID, score, and text of each document.
Generate a word cloud for the first topic.

## Result

The result of the script is a topic model of the abstracts, including a list of the words most associated with each topic and a word cloud representing the first topic.
