import pandas as pd
from google_play_scraper import app, Sort, reviews_all, reviews
from app_store_scraper  import AppStore

DATA_DIR_PATH = "data/"

#Google play store
def google_to_csv(app_name=None, data_src="google"):
  results = reviews_all(app_name)
  df = pd.DataFrame(results)
  df.to_csv(DATA_DIR_PATH + data_src + "_reviews.csv", index=False, encoding="utf-8")

#Return reviews for us and canada
google_to_csv(app_name="com.covalent.kippo")


#Apple app store
def app_to_csv(country=None, app_name=None, data_src="apple"):
  app = AppStore(country=country, app_name=app_name)
  app.review()
  df = pd.DataFrame(app.reviews)#All of the reviews
  df.to_csv(DATA_DIR_PATH + data_src + "_reviews_" + country + ".csv", index=False, encoding="utf-8")

#US
#app_to_csv(country="us", app_name="kippo-dating-app-for-gamers")

#CA
#app_to_csv(country="ca", app_name="kippo-dating-app-for-gamers")
