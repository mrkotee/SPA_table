import flask
from base.models import Resource, create_session
from config import user, password, dbname, host, port

app = flask.Flask(__name__, static_folder='static/')


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return flask.render_template("index.html")


@app.route('/', methods=['POST'])
def get_table():
    page = int(flask.request.get_json()['page'])
    per_page = int(flask.request.get_json()['per_page'])
    session = create_session(user, password, dbname, host, port)
    resources = session.query(Resource).all()
    pages = len(resources)/per_page
    pages = round(pages + (0.5 if pages % 1 > 0 else 0))
    resources = resources[(page-1)*per_page:page*per_page]
    res_dict = {'pages': pages, 'resources': [{'date': res.date.strftime("%Y-%m-%d"),
                 'name': res.name,
                 'amount': res.amount,
                 'distance': res.distance} for res in resources]}
    session.close()
    return flask.jsonify(res_dict)


@app.route('/table', methods=['POST'])
def update_table():
    print(flask.request.get_json())
    request = flask.request.get_json()['request']

    session = create_session(user, password, dbname, host, port)

    page = int(flask.request.get_json()['page'])
    per_page = int(flask.request.get_json()['per_page'])

    resources = session.query(Resource)
    if request == "sort":
        sort_field = flask.request.get_json()['sort_field']
        reverse = flask.request.get_json()['reverse']

        if sort_field == 'name':
            resources = set_query_order(resources, Resource.name, reverse)
        elif sort_field == 'amount':
            resources = set_query_order(resources, Resource.amount, reverse)
        elif sort_field == 'distance':
            resources = set_query_order(resources, Resource.distance, reverse)

    elif request == "search":
        page = 1
        search_field = flask.request.get_json()['search_field']
        search = flask.request.get_json()['search']

        if search_field == 'name':
            resources = resources.filter(Resource.name == search)
        elif search_field == 'amount':
            resources = resources.filter(Resource.amount == search)
        elif search_field == 'distance':
            resources = resources.filter(Resource.distance == search)
        elif search_field == 'date':
            resources = resources.filter(Resource.date == search)

    resources = resources.all()
    pages = len(resources)/per_page
    pages = round(pages + (0.5 if pages % 1 > 0 else 0))
    resources = resources[(page-1)*per_page:page*per_page]
    res_dict = {'pages': pages, 'resources': [{'date': res.date.strftime("%Y-%m-%d"),
                                               'name': res.name,
                                               'amount': res.amount,
                                               'distance': res.distance} for res in resources]}
    session.close()
    return flask.jsonify(res_dict)


def set_query_order(query, instance, reverse):
    if reverse:
        return query.order_by(instance.desc())
    else:
        return query.order_by(instance.asc())


if __name__ == "__main__":
    app.run(debug=True)
