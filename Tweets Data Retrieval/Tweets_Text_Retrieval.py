from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Twitter developer account's credentials
cKey = ''
csecret = ''
atoken= ''
asecret = ''

tId = 0
class listener(StreamListener):
    def on_data(self,data):
        try:
            extract = data.split(',"text":"')[1].split('","source')[0]
            #print(extract)
            global tId
            tId += 1
            print(tId)
            saveT = str(tId)+','+extract
            saveData = open('Raw_Tweets.csv','a')
            saveData.write(saveT)
            saveData.write('\n')
            saveData.close()
            return True
        except Exception as e:
            print('failed on data !',str(e))
      

    def on_error(self,status):
        print(status)

auth = OAuthHandler(cKey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[" suicide "])
