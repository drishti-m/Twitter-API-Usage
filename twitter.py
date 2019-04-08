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

message = "your tweet\n"
twitter.update_status(status= "Daylight Savings: " + dt_string)
print("Tweeted: " + message)
