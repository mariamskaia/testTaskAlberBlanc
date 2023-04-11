docker-compose up app -d
docker-compose run tests /root/py/bin/pytest -v
docker-compose down