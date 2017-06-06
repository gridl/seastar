from flask import Flask
from flask_graphql import GraphQLView

from schema import Query

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = Query,
        graphiql = True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    pass

if __name__ == '__main__':
    app.run()
