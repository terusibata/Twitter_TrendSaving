import keep_alive
import notion_create
import trends
import datetime
import notion_search
import tweet_search
import time

def main():
  id = '957fc60a92dc4c998e6e2e7d6ddfbc38'

  #notionに現在の時間の親ページIDを取得する
  #現在の時間を取得　  
  dt_now = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
  )
  now = {
    "year":dt_now.year,
    "month":dt_now.month,
    "day":dt_now.day,
    "hour":dt_now.hour,
    "minute":dt_now.minute
  }
  #print(now)
  year_pageid = notion_search.search_page(id,f"{now['year']}年のトレンド")
  month_pageid = notion_search.search_database(year_pageid,f"{now['month']}月のトレンド")
  day_pageid = notion_search.search_page(month_pageid,f"{now['month']}月{now['day']}日のトレンド")
  list_pageid = notion_search.search_database(day_pageid,f"{now['hour']}時{now['minute']}分のトレンド")
  print(list_pageid)
  
  #トレンド一覧(30件)を取得する
  trends_list = trends.search()
  #トレンド一覧
  for count,trend in enumerate(trends_list):
    #1位から順番に実行していく
    #ヘッダー2を入力
    notion_create.block.heading_2(list_pageid,f"{count+1}位 {trend}")
    #データベース作成
    tweet_pageid = notion_create.tweet_database.database(list_pageid,f"「{trend}」の関連ツイート")
    #関連ツイート50件取得
    tweet_list = tweet_search.search(trend)
    for tweet in tweet_list:
      inline_page = notion_create.tweet_database.database_page(tweet_pageid,tweet)
      if inline_page:
        if tweet["medias"]:
          print(tweet["medias"])
          for media_url in tweet["medias"]:
            if media_url["type"] == "video":
              notion_create.block.Video(inline_page,media_url["URL"])
            else:
              notion_create.block.image(inline_page,media_url["URL"])
      else:
        continue

      print("1.2秒待機")
      time.sleep(1.2)
      
    #空白
    notion_create.block.text(list_pageid,"")
    #区切り線
    notion_create.block.divider(list_pageid)
  
  # notion_create.tweet_database.database(id,"ここにタイトル")


keep_alive.keep_alive()

#notion_create.database_page()
while True:
  main()
  print("一周完了しました。繰り返します")
