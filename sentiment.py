from nltk.sentiment.vader import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


text = "this product is okayish"


score = analyzer.polarity_scores(text)


print(score)


compound = score['compound']

if compound >= 0.05:
    print("Positive text")
elif compound <= -0.05:
    print("Negative text")
else:
    print("Neutral text")
