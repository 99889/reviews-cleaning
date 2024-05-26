import pandas as pd
import string
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'D:/lenovo/P. projetcs/user review/user_review.xls'
df = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
print("Initial dataset preview:")
print(df.head())

# Clean the data by removing null values and unnecessary columns
df.dropna(inplace=True)

# Assuming the reviews are in a column named 'review'
# Modify as needed if the column name is different
if 'review' not in df.columns:
    raise ValueError("The expected 'review' column is not in the dataset. Please check the column names.")

# Basic text preprocessing function
def preprocess_text(text):
    text = text.lower()  # Lowercase the text
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Apply preprocessing to the review column
df['cleaned_review'] = df['review'].apply(preprocess_text)

# Perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return 'Positive'
    elif blob.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['cleaned_review'].apply(analyze_sentiment)

# Generate a summary report
sentiment_distribution = df['sentiment'].value_counts()

print("\nSentiment distribution:")
print(sentiment_distribution)

# Plot the sentiment distribution
plt.figure(figsize=(8, 6))
sentiment_distribution.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Distribution of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.savefig('D:/lenovo/P. projetcs/user review/sentiment_distribution.png')
plt.show()

# Save the summary report to a markdown file
summary_report = f"""
# Sentiment Analysis Report

## Sentiment Distribution
{sentiment_distribution.to_markdown()}

## Approach
1. **Load the Dataset**: Loaded the dataset from the provided Excel file.
2. **Data Cleaning**: Removed null values and unnecessary columns.
3. **Text Preprocessing**: Converted text to lowercase and removed punctuation.
4. **Sentiment Analysis**: Used TextBlob to analyze the sentiment of each review.
5. **Summary Report**: Generated a summary report showing the distribution of sentiments.

## Challenges Faced
- **Column Identification**: Assumed the reviews were in a column named 'review'. Adjustments may be necessary if the column name differs.
- **Sentiment Analysis Limitations**: The sentiment analysis is based on TextBlob, which uses a simple rule-based approach and may not capture complex sentiments.

## Assumptions Made
- The reviews are in a column named 'review'.
- The dataset contains no other necessary preprocessing steps beyond those mentioned.

## Visual Representation
![Sentiment Distribution](sentiment_distribution.png)
"""

with open('D:/lenovo/P. projetcs/user review/summary_report.md', 'w') as file:
    file.write(summary_report)

print("Summary report and sentiment distribution plot saved successfully.")
