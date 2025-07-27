import pandas as pd

from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

def classify(source, log_message):
    """
    Main logic: routes log messages to regex, BERT, or LLM-based classifiers.
    """
    if source == "LegacyCRM":
        return classify_with_llm(log_message)

    label = classify_with_regex(log_message)
    if label == "Unclassified" or label is None:
        label = classify_with_bert(log_message)

    return label

def classify_logs(logs):
    """
    Classify a list of (source, message) tuples.
    """
    labels = []
    for source, log_msg in logs:
        label = classify(source, log_msg)
        labels.append(label)
    return labels

def classify_csv(input_file):
    """
    Load a CSV, classify the logs, and save results.
    """
    df = pd.read_csv(input_file)
    df["target_label"] = classify_logs(list(zip(df["source"], df["log_message"])))

    output_file = "resources/output.csv"
    df.to_csv(output_file, index=False)
    print(f"Classification saved to: {output_file}")

if __name__ == "__main__":
    classify_csv("resources/test.csv")
