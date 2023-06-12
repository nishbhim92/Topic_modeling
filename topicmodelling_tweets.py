!pip install pandas
!pip install bertopic[all]
import os
import re
import pandas as pd
from bertopic import BERTopic
ico_files = [f for f in os.listdir('/content/') if f.endswith('.csv')]
all_tweets = pd.DataFrame(columns=['created_at', 'text', 'ico'])
# Iterate over each file to merge all data into one dataframe
for ico_file in ico_files:
    # Extract the ico_name from the filename
    ico_name = ico_file.replace('.csv', '')
    # Load data
    ico_data = pd.read_csv(f'/content/{ico_file}')

    # Clean the data
    ico_data['text'] = ico_data['text'].apply(lambda row: re.sub(r"http\S+", "", row).lower())
    ico_data['text'] = ico_data['text'].apply(lambda row: " ".join(filter(lambda x:x[0]!="@", row.split())))
    ico_data['text'] = ico_data['text'].apply(lambda row: " ".join(re.sub("[^a-zA-Z]+", " ", row).split()))

    # Add an 'ico' column to keep track of the ico
    ico_data['ico'] = ico_name

    # Append this ico's data to the all_tweets dataframe
    all_tweets = all_tweets.append(ico_data, ignore_index=True)
    # Topic Modeling on all tweets
topic_model = BERTopic(min_topic_size=35, verbose=True)
topics, _ = topic_model.fit_transform(all_tweets['text'].tolist())
# Get the topics
common_topics = topic_model.get_topic_freq()
# Initialize a dictionary to store the dominant topic for each ICO
ico_dominant_topics = {}
# Print all the ICO names and their dominant topics
for ico, topic in ico_dominant_topics.items():
    print(f"ICO: {ico}, Dominant Topic: {topic}")
    # Get the most frequent words for this topic
    topic_words = topic_model.get_topic(topic)
    if topic_words is not None:  # check if the topic_words is not None
        print("Associated Words: ", topic_words)
    else:
        print("No words found for this topic.")
    print("\n")
    for topic in common_topics['Topic']:
    topic_words = topic_model.get_topic(topic)
    print(f"Topic {topic}:")
    print(topic_words)
    print("\n")
