# Quickstart

1. Make sure port `8888` is open
2. Run `docker compose up` to start the app
3. Apply migrations `docker compose run --rm web python manage.py migrate`
4. Copy staticfiles `docker compose run --rm web python manage.py collectstatic --no-input`
5. Go to http://localhost:8888/api/v1/shrt/ or use curl
```
curl -v --location --request POST 'http://localhost:8888/api/v1/shrt/' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://news.ycombinator.com/"
}'
```
# Code style

See `.pre-commit-config.yaml`

# Docs

Go to http://localhost:8888/api/docs/

