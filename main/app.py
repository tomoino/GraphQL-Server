from flask import Flask
from flask_graphql import GraphQLView
from hello import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # GraphiQLを表示
    )
)

if __name__ == '__main__':
    app.run()