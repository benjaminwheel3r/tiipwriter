# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:52:49 2016
@author: Ben
"""
logloc = 'C:\\Temp\\log.txt'
def tiipWriter(log):
    #Import the necessary methods from tweepy library
    from tweepy.streaming import StreamListener
    from tweepy import OAuthHandler
    from tweepy import Stream
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    global logloc
    logloc = log
    #This is a basic listener that just prints received tweets to stdout.    
    class StdOutListener(StreamListener):
        global logloc
        log = open(logloc,'w')
        
        def on_data(self, data):
            #print(data.decode("utf-8"))
            self.log.write(data.decode("utf-8"))
            #print "writing tweet"
            return True
    
        def on_error(self, status):
            print(status.decode("utf-8"))

        #This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Hillary Clinton', '@HillaryClinton', '#ReadyForHillary', '#HillYes', '#Hillary2016', '#ImWithHer', '#LoveTrumpsHate', '#StandWithBernie', '#Bernie2016', '#Sanders2016', '#VoteTheBern', '#FeelTheBern', '@SenSanders','#CruzControl', '#CruzForPresident', '#Trusted', '#OnlyCruz', '#Trumpers', 'John Kasich', '#JohnKasich', '@JohnKasich', '#AlwaysTrump', 'Donald Trump', '#Trump', '#DumpTrump', '#TrumpTrain', '#IStandWithTrump', '#TrumpIsAlwaysRight', '#DonaldTrump', '@RealDonaldTrump', '#UniteWithCruz', '#ChooseCruz', '#DropOutKasich', '#NeverTrump', '#NeverCruz', '#Cruz2016', '#TedCruz', '#CruzCrew', '@TedCruz', 'Ted Cruz', '#Kasich2016', '#KasichGroundGame', '#KasichWorks', '#Kasich4Us', '#Kasich', '#WeAreTrump', '#VoteTrump', '#TeamTrump', '#VoteTrump2016', '#MakeAmericaGreatAgain', '#TrumpWins', '#Trump2016', 'RealDonaldTrump'])

##############################

#logfile = 'C:\\Temp\\crapfolder\\logger5001.txt'
#tiipWriter(logfile)
if __name__ == '__main__':
    print "google knows who you are"
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Donald Trump', 'Hillary Clinton','Bernie Sanders'])