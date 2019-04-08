from twython import Twython
from datetime import datetime




from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

message = "was ist das?\n"
twitter.update_status(status= "How can you not love Shiffman? Such a pure genius. ")
print("Tweeted: " + message)
