from transformers import pipeline

analysis = pipeline("sentiment-analysis")

def sentiment_analyzer(text_to_analyse):
    output = analysis(text_to_analyse)
    return output