# stackoverflow-nlp-posts-classification
StackOverflow NLP Posts Classification

\section*{Project Description: NLP Stack Overflow Post Categorization}

This project focuses on the collection, preprocessing, and categorization of NLP-related questions from Stack Overflow. It employs a rule-based classification system using regular expressions to group posts into meaningful NLP categories.

\subsection*{Key Features}
\begin{itemize}
  \item \textbf{Data Collection}: Retrieved posts from Stack Overflow using the Stack Exchange API.
  \item \textbf{Preprocessing}: Applied text cleaning, lemmatization, and both standard and domain-specific stopword removal using TF-IDF.
  \item \textbf{Rule-Based Categorization}: Used regular expression-based sentence pattern matching to assign posts to predefined NLP categories.
  \item \textbf{Data Visualization}: Generated visual insights such as post trends, category distributions, and answer statistics.
  \item \textbf{Data Export}: Saved the categorized data into separate CSV files for further analysis and exploration.
\end{itemize}

\subsection*{Output Files}
\begin{itemize}
  \item \texttt{data/preprocessed\_nlp\_stackoverflow\_data.csv} -- Fully cleaned and lemmatized dataset.
  \item \texttt{categories/} -- Directory containing categorized post CSV files.
  \item \texttt{output/} -- Contains graphs and visualizations generated during the analysis.
\end{itemize}
