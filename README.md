# 🧠 NLP Stack Overflow Post Categorization

This project focuses on collecting, preprocessing, and categorizing NLP-related questions from Stack Overflow using a rule-based classification system powered by regular expressions. The goal is to identify the types of NLP problems developers face and analyze common discussion patterns within the community.

## 🚀 Key Features

- 🔍 **Data Collection**: Retrieved posts using the Stack Exchange API.
- 🧹 **Preprocessing**: Applied text cleaning, lemmatization, and removal of both standard and domain-specific stopwords using TF-IDF.
- 🧠 **Rule-Based Categorization**: Used regular expressions to match patterns and assign posts to NLP-related categories such as Tokenization, NER, Sentiment Analysis, etc.
- 📊 **Data Visualization**: Generated insights such as post counts per category, yearly trends, and post-answer distributions.
- 💾 **Data Export**: Categorized posts are saved as separate CSV files for further analysis.

## 📂 Output Files

- `data/preprocessed_nlp_stackoverflow_data.csv` – Cleaned and preprocessed dataset.
- `categories/` – Folder containing CSV files for each NLP category.
- `output/` – Contains generated charts and visual summaries.

## 📌 Technologies Used

- Python (Pandas, Regex, NLTK, scikit-learn)
- Stack Exchange API
- Jupyter Notebook

---

Let me know if you'd like to add sections for installation, usage, or demo screenshots!

