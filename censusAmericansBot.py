#code - everywordbot by allison parrish
import tweepy
import os
import time

class EverywordBot(object):

    def __init__(self, consumer_key, consumer_secret,
                 access_token, token_secret,
                 source_file_name, index_file_name,
                 lat=None, long=None, place_id=None):
        self.source_file_name = source_file_name
        self.index_file_name = index_file_name
        self.lat = lat
        self.long = long
        self.place_id = place_id

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        self.twitter = tweepy.API(auth)

    def _get_current_index(self):
        if not(os.path.isfile(self.index_file_name)):
            return 0
        with open(self.index_file_name) as index_fh:
            return int(index_fh.read().strip())

    def _increment_index(self, index):
        with open(self.index_file_name, "w") as index_fh:
            index_fh.truncate()
            index_fh.write("%d" % (index + 1))
            index_fh.close()

    def _get_current_line(self, index):
        with open(self.source_file_name) as source_fh:
            # read the desired line
            for i, status_str in enumerate(source_fh):
                if i == index:
                    break
            return status_str.strip()

    def post(self):
        index = self._get_current_index()
        status_str = self._get_current_line(index)
        self.twitter.update_status(status=status_str,
                                   lat=self.lat, long=self.long,
                                   place_id=self.place_id)
        self._increment_index(index)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--consumer_key', dest='consumer_key',
                      help="twitter consumer key")
    parser.add_option('--consumer_secret', dest='consumer_secret',
                      help="twitter consumer secret")
    parser.add_option('--access_token', dest='access_token',
                      help="twitter token key")
    parser.add_option('--token_secret', dest='token_secret',
                      help="twitter token secret")
    parser.add_option('--source_file', dest='source_file',
                      default="tweet_list.txt",
                      help="source file (one line per tweet)")
    parser.add_option('--index_file', dest='index_file',
                      default="index",
                      help="index file (must be able to write to this file)")
    parser.add_option('--lat', dest='lat',
                      help="The latitude for tweets")
    parser.add_option('--long', dest='long',
                      help="The longitude for tweets")
    parser.add_option('--place_id', dest='place_id',
                      help="Twitter ID of location for tweets")
    (options, args) = parser.parse_args()

    bot = EverywordBot(options.consumer_key, options.consumer_secret,
                       options.access_token, options.token_secret,
                       options.source_file, options.index_file,
                       options.lat, options.long, options.place_id)
    numberOfTweets = 0
    while True:
        numberOfTweets +=1
        bot.post()
        print "tweeeeet ..."+str(numberOfTweets)+ " ... %s" % time.ctime()
        time.sleep(14400)
