import requests
from pprint import pprint
import time
import os

class OneselfError(Exception):
    """自作プログラムのエラーを知らせる例外クラスです。"""
    pass

def get_request_url(end_point):
    return f'https://api.notion.com/v1/{end_point}'

notion_api_key = os.environ['notion_api_key']
id = '957fc60a92dc4c998e6e2e7d6ddfbc38'

headers = {"Authorization": f"Bearer {notion_api_key}",
           "Content-Type": "application/json",
           "Notion-Version": "2022-02-22"}


def getpages(page_id=None):
  if not page_id:
    raise OneselfError("page_idが引数にありません")
  
  lists = []
  datas = {}
  start_cursor = None
  
  while True:
    if start_cursor is None:
      response = requests.request('GET', url=get_request_url(f'blocks/{id}/children?page_size=100'), headers=headers)
    else:
      response = requests.request('GET', url=get_request_url(f'blocks/{id}/children?page_size=100&start_cursor={start_cursor}'), headers=headers)
    pprint(response.json())
    res = response.json()
  
    for data in res["results"]:
      try:
        #データベースの場合
        datas["title"] = data["child_database"]["title"]
        datas["id"] = data["parent"]["page_id"]
      except:
        #データベースではない場合はスキップ
        continue
      lists.append(datas)
  
    time.sleep(0.3)
    if not res["has_more"]:
      break
    else:
      start_cursor = res["next_cursor"]

  return lists
