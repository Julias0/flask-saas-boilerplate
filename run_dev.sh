bash ./wait_for.sh db:5432 -- flask db upgrade
gunicorn --bind 0.0.0.0:$PORT --reload --log-level=debug main:app
