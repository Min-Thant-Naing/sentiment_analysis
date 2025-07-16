''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from sentiment_analyzer.sentiment_analyzer import sentiment_analyzer

app = Flask(__name__)

@app.route("/sentimentAnalyzer", methods=["GET", "POST"])
def sent_analyzer():
    data = request.args.get("textToAnalyze")
    try:
        result = sentiment_analyzer(data)
        return f"The given text has been identified as {result['label']} with a score of {result['score']}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

@app.route("/", methods=["GET", "POST"])
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
