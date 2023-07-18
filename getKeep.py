import sys
import os
import datetime
from dotenv import load_dotenv

sys.path.append('lib/gkeepapi')
import gkeepapi

load_dotenv()

keep = gkeepapi.Keep()
success = keep.login(os.environ["GOOGLE_USERNAME"], os.environ["GOOGLE_APP_PASSWORD"])
print("Login success? ", success)

# keep.find returns a generator - use next(gnotes) to get the first in the list
gnotes = keep.find(query='Shopping')

shopping_note = next(gnotes)

curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

shopping_note.text = shopping_note.text + "\n Last edit:"+ curr_date

keep.sync()
print("sync success?")