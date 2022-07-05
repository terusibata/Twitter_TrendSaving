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

headers = {"Authorization": f"Bearer {notion_api_key}",
           "Content-Type": "application/json",
           "Notion-Version": "2022-02-22"}

class block():
  def text(block_id=None,content_text=None):
    create_json = {"children": [
        {
          "object": 'block',
          "type": 'paragraph',
          "paragraph": {
            "rich_text": [
              {
                "type": 'text',
                "text": {
                  "content": content_text,
                },
              },
            ],
          },
        }
    ]}
    response = requests.request('patch', url=get_request_url(f'blocks/{block_id}/children'), headers=headers, json=create_json)
    time.sleep(0.3)
    print("テキスト入力完了")
    pprint(response.json())

  def divider(block_id=None):
    create_json = {"children": [
        {
          "object": 'block',
          "type": 'divider',
          "divider": {}
        }
    ]}
    response = requests.request('patch', url=get_request_url(f'blocks/{block_id}/children'), headers=headers, json=create_json)
    time.sleep(0.3)
    print("区切り線の書き込み完了")
    pprint(response.json())

  def image(block_id=None,img = None):
    create_json ={"children": [
        {
          "type": "image",
          "image": {
            "type": "external",
            "external": {
              "url": img
            }
          }
        }
    ]}
    response = requests.request('patch', url=get_request_url(f'blocks/{block_id}/children'), headers=headers, json=create_json)
    time.sleep(0.3)
    print("画像の埋め込み完了")
    pprint(response.json())

  def Video(block_id=None,Video = None):
    create_json ={"children": [
        {
          "type": "video",
          "video": {
            "type": "external",
            "external": {
              "url": Video
            }
          }
        }
    ]}
    response = requests.request('patch', url=get_request_url(f'blocks/{block_id}/children'), headers=headers, json=create_json)
    time.sleep(0.3)
    print("ビデオの埋め込み完了")
    pprint(response.json())
  
class date_database():
  def database(block_id=None,content_text=None):
    create_json = {
      "parent": {
          "type": "page_id",
          "page_id": block_id
      },
      "icon": {
      	"type": "emoji",
  			"emoji": "📝"
    	},
      "title": [
          {
              "type": "text",
              "text": {
                  "content": content_text,
                  "link": None
              }
          }
      ],
      "properties": {
          "ページタイトル": {
              "title": {}
          },
          "概要": {
              "rich_text": {}
          },
          "タグ": {
              "select": {
                  "options": []
              }
          }
      }
    }
    response = requests.request('post', url=get_request_url('databases'), headers=headers, json=create_json)
    #pprint(response.json())
    time.sleep(0.3)
    print(f'{response.json()["id"]}にデータベースを作成しました')
    return response.json()["id"]


  def database_page(block_id=None,page_title=None,summary=None,tag=None):
    create_json = {
    	"parent": { "database_id": block_id },
      "icon": {
      	"emoji": "📝"
      },
    	"properties": {
    		"ページタイトル": {
    			"title": [
    				{
    					"text": {
    						"content": page_title
    					}
    				}
    			]
    		},
    		"概要": {
    			"rich_text": [
    				{
    					"text": {
    						"content": summary
    					}
    				}
    			]
    		},
    		"タグ": {
    			"select": {
    				"name": tag
    			}
    		}
      }
    }
    response = requests.request('post', url=get_request_url('pages'), headers=headers, json=create_json)
    time.sleep(0.3)
    print(f'{block_id }のデータベースに新しいページを作成しました')
    return response.json()["id"]

class tweet_database():
  def database(block_id=None,content_text=None):
    create_json = {
      "parent": {
          "type": "page_id",
          "page_id": block_id
      },
      "icon": {
      	"emoji": "📝"
      },
      "title": [
          {
              "type": "text",
              "text": {
                  "content": content_text,
                  "link": None
              }
          }
      ],
      "properties": {
          "本文": {
              "title": {}
          },
          "ユーザー名": {
              "rich_text": {}
          },
          "ユーザーID": {
              "rich_text": {}
          },          
          "投稿日": {
              "date": {}
          },
          "リツイート数": {
            "number": {
                "format": "number"
            }
          },
          "いいね数": {
            "number": {
                "format": "number"
            }
          },
          "ハッシュタグ": {
            "type": "multi_select",
            "multi_select": {
                "options": []
            }
          }
      }
    }
    response = requests.request('post', url=get_request_url('databases'), headers=headers, json=create_json)
    #pprint(response.json())
    time.sleep(0.3)
    print(f'{response.json()["id"]}にデータベースを作成しました')
    return response.json()["id"]


  def database_page(block_id=None,page_title=None,summary=None,tag=None):
    create_json = {
    	"parent": { "database_id": block_id },
      "icon": {
        	"type": "external",
          "external": {
          	"url": "https://website.domain/images/image.png"
          }
      },
      "cover": {
        	"type": "external",
          "external": {
          	"url": "https://website.domain/images/image.png"
          }
      },
    	"properties": {
    		"ページタイトル": {
    			"title": [
    				{
    					"text": {
    						"content": page_title
    					}
    				}
    			]
    		},
    		"概要": {
    			"rich_text": [
    				{
    					"text": {
    						"content": summary
    					}
    				}
    			]
    		},
    		"タグ": {
    			"select": {
    				"name": tag
    			}
    		}
      }
    }
    response = requests.request('post', url=get_request_url('pages'), headers=headers, json=create_json)
    time.sleep(0.3)
    print(f'{block_id }のデータベースに新しいページを作成しました')
    return response.json()["id"]
