import API_key

#日本のWOEID
woeid = 23424856
#トレンド一覧取得
trends =  API_key.api.get_place_trends(woeid)

trends_top = []
for trend in trends[0]["trends"]:
  trends_top.append(trend["name"])
print(trends_top)