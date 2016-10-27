import nltk

class Analyzer():
    """Implements sentiment analysis."""
    # My code
    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        self.posDict = set()
        self.negDict = set()
        
        file = open(positives, "r")
        for line in file:
            if line[0] == ';':
                continue
            self.posDict.add(line.rstrip("\n"))
        file.close()
        
        file = open(negatives, "r")
        for line in file:
            if line[0] == ';':
                continue
            self.negDict.add(line.rstrip("\n"))
        file.close()
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        wordsToCheck = text.split(' ')
        for word in wordsToCheck:
            for line in self.posDict:
                if word.lower() == line:
                    score += 1
                    break
            for line in self.negDict:
                if word.lower() == line:
                    score -= 1
        return score
