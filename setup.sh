pyenv install 3.7.3
pyenv local 3.7.3
poetry init
mkdir main
touch .gitignore
echo .venv >> .gitignore
echo __pycache__ >> .gitignore
poetry add graphene==2.1.6
poetry add Flask==1.0.3
poetry add Flask-GraphQL==2.0.0