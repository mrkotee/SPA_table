
from datetime import datetime as dt
from base.models import create_table, create_session, Base, Resource
from views import app


def fill_base(session):
    import requests
    import random
    words = requests.get("https://www.mit.edu/~ecprice/wordlist.10000").text.splitlines()
    for word in words[:100]:
        session.add(Resource(dt.now().date().replace(day=random.randint(1, 28), month=random.randint(1, 12)),
                             word, random.randint(1, 200), random.randint(1, 100)))
        session.commit()


if __name__ == "__main__":
    from config import user, password, dbname, host, port

    create_table(Base, user, password, dbname, host, port)

    session = create_session(user, password, dbname, host, port)

    fill_base(session)

    app.run()
