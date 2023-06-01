# Import necessary libraries
import pandas as pd
from top2vec import Top2Vec

# Read data from an Excel file
data = pd.read_excel('ABS.xlsx')

# Select the 'Abstract' column
docs = data['Abstract'].tolist()

# Print the second item in the docs list
print(docs[1])

# Train Top2Vec model on the documents
model = Top2Vec(docs)

# Get the sizes of the topics and their corresponding numbers
topic_sizes, topic_nums = model.get_topic_sizes()

# Print the total number of topics
print(model.get_num_topics())

# Print the sizes and numbers of the topics
print(topic_sizes)
print(topic_nums)

# Get the words, word scores and topic numbers for the first topic
topic_words, word_scores, topic_nums = model.get_topics(1)

# Perform hierarchical topic reduction, reducing the number of topics to 1
model.hierarchical_topic_reduction(num_topics=1)

# Print the number and words of each topic
for words, scores, num in zip(topic_words, word_scores, topic_nums):
    print(num)
    print(f"words:{words}")

# Search the documents that belong to topic number 0 and get the top 10
documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=0, num_docs=10)

# Print the document ID, score and text of each document
for doc, score, doc_id in zip(documents, document_scores, document_ids):
    print(f"Document: {doc_id}, Score:{score}")
    print("----------")
    print(doc)
    print("----------")
    print()

# Generate a word cloud for the first topic
model.generate_topic_wordcloud(1)
