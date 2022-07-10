import tweepy
import API_key
import time

def search(search_word=None):

  while True:
    try:
      # 検索条件の設定（リストで渡せば複数指定できる）
      search = f"{search_word}　-filter:retweets"
      tweet_max = 50
       
      # ツイートを取得してtweetsという変数に代入
      tweets = tweepy.Cursor(API_key.api.search_tweets, q=search, lang="ja").items(tweet_max)
      break
    except:
      print("ツイートの取得に失敗しました。再度リクエストします")
      time.sleep(5)
   
  # 必要な情報のみを格納する箱(=リスト)を作る
  tweet_data = {}
  tweet_datas = []
  # リストに必要な情報を入れていく
  for tweet in tweets:
    # print(str(tweet.created_at))
    # break
    #本文
    tweet_data["title"]=tweet.text
    #ユーザーname
    tweet_data["username"]=tweet.user.name
    #ユーザーID
    tweet_data["userid"]=tweet.user.screen_name
    #投稿日
    tweet_data["date"]=str(tweet.created_at)
    #リツイート数
    tweet_data["retweet_count"]=tweet.retweet_count
    #いいね数
    tweet_data["favorite_count"]=tweet.favorite_count
    #ツイートURL
    #tweet_data["URL"]=tweet.entities.urls[0].url
    #ハッシュタグ
    if "hashtags" in tweet.entities.keys(): 
      hashtag_data = {}
      hashtags = []
      for hashtag in tweet.entities["hashtags"]:
        hashtag_data["name"] = hashtag["text"]
        hashtags.append(hashtag_data)
        hashtag_data = {}
      tweet_data["hashtags"] = hashtags 
    else:
      tweet_data["medias"] = []
    #プロフィール画像
    try:
      tweet_data["profile_image"] = tweet.user.profile_image_url_https
    except:
      tweet_data["profile_image"]="https://img.icons8.com/ios/250/000000/twitter.png"
    #ヘッダー画像
    try:
      tweet_data["banner"]= tweet.user.profile_banner_url
    except:
      tweet_data["banner"]= "https://img.icons8.com/ios/250/000000/twitter.png"
    #media保存
    try:
      if "media" in tweet.extended_entities.keys():
        media = {}    
        medias = []
        for media_url in tweet.extended_entities["media"]:
          media["type"] = media_url["type"]
          if media["type"] =="video":
            try:
              video_bitrate = 0
              for video_url in media_url["video_info"]["variants"]:
                if "bitrate" in video_url.keys():
                  
                  if video_url["bitrate"] > video_bitrate:
                    media["URL"] = video_url["url"]
                    video_bitrate = video_url["bitrate"]

              if video_bitrate == 0:
                tweet_data["medias"] = []
                break
            except:
              tweet_data["medias"] = []
              break
          else:
            media["URL"] = media_url["media_url_https"]
          medias.append(media)
          media = {} 
        tweet_data["medias"] = medias
      else:
        tweet_data["medias"] = []
    except:
      tweet_data["medias"] = []
    
    tweet_datas.append(tweet_data)
    tweet_data = {}
  
  # 取得したツイートの内容を出力
  return tweet_datas
