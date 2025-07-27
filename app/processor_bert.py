from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

# Load transformer model and classifier
transformer_model = SentenceTransformer("all-MiniLM-L6-v2")
classifier_model = joblib.load("models/log_classifier.joblib")

def classify_with_bert(log_message):
    """
    Classifies a log message using BERT-based embeddings and a pre-trained classifier.

    Parameters:
        log_message (str): A single log message.

    Returns:
        str: The predicted class label or 'Unclassified' if confidence is low.
    """
    # Encode the message
    message_embedding = transformer_model.encode([log_message])  # List input to preserve shape

    # Predict class probabilities
    probabilities = classifier_model.predict_proba(message_embedding)[0]

    # Confidence threshold
    if max(probabilities) < 0.5:
        return "Unclassified"

    # Predict class
    predicted_class = classifier_model.predict(message_embedding)[0]

    return predicted_class

if __name__ == "__main__":
    sample = "System reboot initiated by user Admin"
    print(f"Predicted label: {classify_with_bert(sample)}")
