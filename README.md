# censusAmericans
Here is a twitter robot that automatically posts short bios of Americans from census data to twitter.

The data is public and anonymized
censusAmericans takes Public Use Microdata Sample(PUMS) data and reconstitutes it into mini narratives that describe real individuals who participated in the extended census in 2013. The PUMS is a limited subset of the American Community Survey, which is released to allow researchers access to a number of detailed profiles of anonymized individuals from each state. The profiles include items that when assembled has the potential to describe individuals for further study, but not so much detail that they can be deanonymized. For example while including relatable details such as the length, method, and time of a person's daily commute to work, the snapshots presented are also limited by omissions such as the lack of a person's location. 

We made them into bios because what limited information is offered seemed to communicate individuals effectively - thankfully, we only need to know a little about a person in order to relate to them. 
whether it is how much they work, who they take care of, or where they were born, just a few descriptors are enough. we hope some of these qualities are perserved even when we further limit the reconstituted bios of these americans to the length of a tweet. we built the twitter account to generate these bios efficiently and automatically broadcast them every few hours until every person in the data has been covered. even though the limitation on length will result in similar as well as less satisfying bios at times (we ourselves would find it limiting to be described in such spare terms and categorized so broadly), it remains interesting to think about these people because they are real and when they might even shorten distances when they are broadcast ambiently and constantly.

here are some people:
- "I've been married a few times. I work in sporting and athletic goods, and doll industry. I've never served in the military."
- "I was naturalized as an U. S. citizen. I had less than 2 weeks off last year. I work in construction."
- "I live with my parents. I'm unemployed, have not worked for the last 5 years. I've not worked for at least 5 years."
- "I've been taking care of my grandkids for more than 5 years. I work in amusement, gambling, and recreation industries."

you can follow the census here: @censusAmericans

Data:
  - American Community Survey's Public Use Microdata Sample (PUMS) dataset
  - from http://www.census.gov/acs/www/data_documentation/public_use_microdata_sample/

Code: 

The data is processed in 3 steps, so the code here split into 3 python scripts. It is by no means efficient.

  - draft.py isolates columns with content(just taking out identification codes, redundant columns) and turns the raw data from above into human readable form using dictionaries created to make each line of data more conversational sounding. Example: column JWTR with value 06 is translated into "I take a ferryboat to work. " This results in a very large file of "bios" that you can read for a sanity check. 
  
  - refine.py checks each entry from the previous script and randomly combines tweets from 3-4 sentences/columns until each entry is less than 140 chars and ok for tweet.
  
  - censusAmericansBot.py uses tweepy the python twitter api to post a row from the resulting file. Currently it posts 1 line every 4 hours, and keeps a index file to track its progress. Based on everywordbot code from Allison Parrish NYU - her projects: http://www.decontextualize.com/

  - Setting up a twitter account and app to run the script is simple, I followed the instructions here: http://zachwhalen.net/posts/how-to-make-a-twitter-bot-with-google-spreadsheets-version-04

TODO:
  - make notification email for when script fails
  - make geolocated tweets according to state?
