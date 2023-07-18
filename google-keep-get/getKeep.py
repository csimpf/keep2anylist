import sys
import os
import datetime
from dotenv import load_dotenv

sys.path.append('../lib/gkeepapi')
import gkeepapi

load_dotenv()

keep = gkeepapi.Keep()
success = keep.login(os.environ["GOOGLE_USERNAME"], os.environ["GOOGLE_APP_PASSWORD"])
print("Login success? ", success)

# keep.find returns a generator - use next(gnotes) to get the first in the list
gnotes = keep.find(query=os.environ["KEEP_LIST_NAME"])

shopping_note = next(gnotes)

curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# shopping_note.text = shopping_note.text + "\n Last update:"+ curr_date
print(shopping_note.text)

item_list = shopping_note.text[:shopping_note.text.index("Last update:")].split('\n')[:-1]

# send item_list to lambda to update AnyList
print(item_list)

keep.sync()