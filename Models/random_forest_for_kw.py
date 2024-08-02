from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm import tqdm
import re

# Get English stopwords
additional_stopwords = {'to', 'were', 'going', 'Is', 'are', 'am', 'this', 'that', 'me', 'let', 'was', 'were', 'these', 'those', 'so', 'the', 'do', 'etc', 'why', 'from', 'we', 'us','question'}
stop_words = set(stopwords.words('english')).union(additional_stopwords)

# Load the huge list of keywords from the file
with open("allah.txt", "r") as file:
    keywords = list(set(file.read().splitlines()))
    
# Function to preprocess and extract features from transcripts
def extract_features(transcript):
    # Tokenize the transcript into words and phrases of 2-3 words
    words_and_phrases = re.findall(r'\b\w+\b|\"[\w\s]+\"', transcript)
    
    # Remove stop words and words/phrases with length less than 3
    filtered_words_and_phrases = [word for word in words_and_phrases if word.lower() not in stop_words and len(word) >= 3]
    
    # Join the remaining words/phrases back into a single string
    preprocessed_transcript = ' '.join(filtered_words_and_phrases)
    
    # Extract features
    vectorizer = CountVectorizer(ngram_range=(1, 3), vocabulary=keywords, binary=True)
    X = vectorizer.fit_transform([preprocessed_transcript]).toarray()
    return X


# Train the classifier
def train_classifier(X_train, y_train):
    # Flatten the X_train array to make it two-dimensional
    X_train_flat = [sample.flatten() for sample in X_train]
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train_flat, y_train)
    return rf_classifier

# Load transcripts from three text files
transcript_files = ["cs221lecture1.txt","cs221lecture2.txt","cs221lecture3.txt" ,"cs221lecture4.txt","cs221lecture5.txt","cs221lecture6.txt","cs221lecture7.txt","cs221lecture8.txt","cs221lecture9.txt","cs221lecture10.txt","cs221lecture11.txt","cs221lecture12.txt","cs221lecture13.txt","cs221lecture14.txt","cs221lecture15.txt","cs221lecture16.txt","cs221lecture17.txt","cs221lecture18.txt","cs221lecture19.txt"]
X_train = []
y_train = []

for file in transcript_files:
    with open(file, "r") as f:
        transcript = f.read()
        for word in tqdm(transcript.split(), desc="Processing Words", unit="word", leave=False):
            # Extract features for the current word
            word_features = extract_features(word)
            if word.lower() in keywords:
                X_train.append(word_features)
                y_train.append(1)  # Keyword
            else:
                X_train.append(word_features)
                y_train.append(0)  # Normal word
                
# Train the classifier
rf_classifier = train_classifier(X_train, y_train)

# Load the new transcript from the text file
with open("new_tt.txt", "r") as file:
    new_transcript = file.read()

# Tokenize the new transcript into words
new_transcript_words = new_transcript.split()

# Predict labels for each word in the new transcript
predictions = []
for word in new_transcript_words:
    # Extract features for the current word
    word_features = extract_features(word)
    # Flatten the features array to make it two-dimensional
    word_features_flat = word_features.flatten()
    # Predict using the trained classifier
    prediction = rf_classifier.predict([word_features_flat])[0]
    predictions.append(prediction)
sses=set()
# Print the words along with their predicted labels
for word, prediction in zip(new_transcript_words, predictions):
    if prediction == 1:
        sses.add(word)
        

    print (sses)        
    
    
    # Load the actual keywords from kw.txt
with open("zzzz.txt", "r") as file:
    actual_keywords = set(file.read().splitlines())

# Calculate True Positives (TP), False Positives (FP), and False Negatives (FN)
TP = len(actual_keywords.intersection(sses))
FP = len(sses.difference(actual_keywords))
FN = len(actual_keywords.difference(sses))

# Calculate precision
precision = TP / (TP + FP) if (TP + FP) > 0 else 0

# Calculate recall
recall = TP / (TP + FN) if (TP + FN) > 0 else 0

# Calculate frequency
frequency = TP / len(actual_keywords) if len(actual_keywords) > 0 else 0

# Calculate accuracy
accuracy = (TP + len(new_transcript_words) - len(sses)) / len(new_transcript_words) if len(new_transcript_words) > 0 else 0

# Print the results
print("Precision:", precision)
print("Recall:", recall)
print("Frequency:", frequency)
print("Accuracy:", accuracy)
