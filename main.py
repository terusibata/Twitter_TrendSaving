import keep_alive
import notion_create

def main():
  id = '957fc60a92dc4c998e6e2e7d6ddfbc38'
  notion_create.tweet_database.database(id,"ここにタイトル")



keep_alive.keep_alive()

main()
