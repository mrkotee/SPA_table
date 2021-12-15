
from datetime import datetime as dt
from base.models import create_table, create_session, Base, Resource


user, password, dbname, host, port = 'postgres', 123, 'postgres', 'localhost', 5555

# create_table(Base, user, password, dbname, host, port)

session = create_session(user, password, dbname, host, port)

# import requests
# import random
# words = requests.get("https://www.mit.edu/~ecprice/wordlist.10000").text.splitlines()
# for word in words[:100]:
#     session.add(Resource(dt.now().date().replace(day=random.randint(1, 28), month=random.randint(1, 12)),
#                          word, random.randint(1, 200), random.randint(1, 100)))
#     session.commit()

print([res.name for res in session.query(Resource).all()])
