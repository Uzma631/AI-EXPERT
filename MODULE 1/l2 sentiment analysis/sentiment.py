from textblob import TextBlob
user=input("enter your sentiment")
blob=TextBlob(user).sentiment.polarity
print(blob)