import flask
from base.models import Resource, create_session
from config import user, password, dbname, host, port
default_per_page = 20

app = flask.Flask(__name__, static_folder='static/')


@app.route('/', methods=['GET', 'HEAD'])
def index():
    session = create_session(user, password, dbname, host, port)
    resources = session.query(Resource).all()
    pages = range(1, int(len(resources)/default_per_page)+1)
    session.close()
    return flask.render_template("index.html", resources=resources, pages=pages)


@app.route('/', methods=['POST'])
def update_table():
    print(flask.request.get_json())
    # page = int(flask.request.args.get('page'))
    # per_page = int(flask.request.args.get('per_page'))
    # session = create_session(user, password, dbname, host, port)
    # resources = session.query(Resource).all()[:page*per_page]
    # return flask.render_template('table.html', resources=resources)
    return ''


if __name__ == "__main__":
    app.run(debug=True)
