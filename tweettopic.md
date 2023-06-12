# Crypto Tweet Topic Modeling

This project applies Topic Modeling to cryptocurrency-related tweets. We utilize BERTopic, a topic modeling technique that uses BERT embeddings to create meaningful topics.

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)

## Installation

Before getting started, make sure to install the required libraries. You can install them using pip:

```bash
pip install pandas
pip install bertopic[all]
```
## Project Structure
The project should have the following structure:
/content/
├── ico_1.csv
├── ico_2.csv
├── ...
└── ico_n.csv

The project expects ICO tweet datasets in the '/content/' directory. These CSV files, each named after its corresponding ICO, should contain at least two columns: created_at and text.
