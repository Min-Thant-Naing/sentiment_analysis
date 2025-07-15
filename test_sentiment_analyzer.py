import unittest
from sentiment_analyzer.sentiment_analyzer import sentiment_analyzer

class TestSentiment(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(sentiment_analyzer("I love this new technology")[0]['label'], 'POSITIVE')
        
        self.assertEqual(sentiment_analyzer("I hate this new technology")[0]['label'], 'NEGATIVE')
        self.assertEqual(sentiment_analyzer("I am not sure about this")[0]['label'], 'NEGATIVE')
        
unittest.main()        