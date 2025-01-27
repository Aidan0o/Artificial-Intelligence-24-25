import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

def load_data(file_path):
    # Load data from CSV
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    # Split the data into features and labels
    X = data['text']
    y = data['label']

    # Split into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Convert text data to feature vectors
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train Decision Tree classifier
    model = DecisionTreeClassifier()
    model.fit(X_train_vec, y_train)

    # Test the model
    y_pred = model.predict(X_test_vec)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Classification Report (precision, recall, F1 score)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Extracting the weighted average metrics (for overall precision, recall, F1 score)
    weighted_precision = report['weighted avg']['precision']
    weighted_recall = report['weighted avg']['recall']
    weighted_f1 = report['weighted avg']['f1-score']

    print(f"\nOverall Precision: {weighted_precision * 100:.4f}%")
    print(f"Overall Recall: {weighted_recall * 100:.4f}%")
    print(f"Overall F1 Score: {weighted_f1 * 100:.4f}%")
    print(f"Overall Accuracy: {accuracy * 100:.4f}%")

    # Confusion Matrix: True/False Positives/Negatives (for each class)
    cm = confusion_matrix(y_test, y_pred)

    # For multi-class, print the matrix and the per-class results
    for i, label in enumerate(np.unique(y_test)):
        tn = cm[i, i]
        fp = cm[:, i].sum() - tn
        fn = cm[i, :].sum() - tn
        tp = cm.sum() - tn - fp - fn
        if label == 1:
            labelName = "Spam"
        else:
            labelName = "Ham"

        print(f"\nClass {labelName}:")
        print(f"True Positives: {tp}")
        print(f"False Positives: {fp}")
        print(f"True Negatives: {tn}")
        print(f"False Negatives: {fn}")

    return model, vectorizer

def classify_email(model, vectorizer, email):
    # Transform the email into the feature space
    email_vec = vectorizer.transform([email])
    prediction = model.predict(email_vec)
    return "Spam" if prediction[0] == 1 else "Ham"

def main():
    # Load dataset
    file_path = "combined_data.csv"
    data = load_data(file_path)

    # Train the model
    model, vectorizer = train_model(data)

    # Allow user to classify their own emails
    while True:
        email = input("\nEnter an email to classify (or type 'exit' to quit): ")
        if email.lower() == 'exit':
            break
        result = classify_email(model, vectorizer, email)
        print(f"The email is classified as: {result}")

if __name__ == "__main__":
    main()
