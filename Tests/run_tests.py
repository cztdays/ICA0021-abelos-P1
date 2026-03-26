import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scr'))

from people_counter import count_people_by_location

SMALL_FILE = os.path.join(os.path.dirname(__file__), '..', 'Testing_data', 'people.json')
BIG_FILE   = os.path.join(os.path.dirname(__file__), '..', 'Testing_data', 'BIGpeople.json')

print("people.json\n")
small = count_people_by_location(SMALL_FILE)
print(small)
sys.stdout.flush()

print("\nBIGpeople.json\n")
big = count_people_by_location(BIG_FILE)
print(big)
sys.stdout.flush()
