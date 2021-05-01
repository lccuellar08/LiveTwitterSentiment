# LiveTwitterSentiment

Live Twitter Sentiment is a simple script that given a string, will begin live streaming all to the command line all tweets that contain that string. In addition, a sentiment (from 0 to 1) will be calculated for every tweet, as well as the aggregate score.

### Preqrequisites

In order to run this project, one requires to have API credentials for Twitter's API. The credentials will then be entered into config.py

### Installing

Download the repository

```
git clone https://github.com/lccuellar08/LiveTwitterSentiment.git
```

Install the requirements

```
pip install requirements.txt
```

## Running

To run the end to the script, all you need are Twitter API credentials.

First enter the credentials into config.py

Then run main.py and pass the string you would like to stream as an argument. 

Example:
```
python main.py "2020 elections"
```