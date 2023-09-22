import sys
import os
import datetime
print(sys.path)
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
print(dir(shopping_note.items[0]))

# item_list = shopping_note.text[:shopping_note.text.index("Last update:")].split('\n')[:-1]

# send item_list to lambda to update AnyList
list_to_send = []

for item in shopping_note.items:
    list_to_send.append(item.text)

print("Going to send this to AnyList:")
print(','.join(list_to_send))


# Once sent and HTTP 200, delete from this list
# keep.sync()