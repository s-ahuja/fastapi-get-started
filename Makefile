alembic-init:
	alembic init alembic

alembic-initial-migration:
	rm -f ./alembic/versions/*.py
	alembic revision --autogenerate -m "001_initial_migration"

alembic-generate-migration:
	alembic revision --autogenerate -m "00x_comment"

alembic-upgrade-latest:
	alembic upgrade head

alembic-upgrade:
	alembic upgrade +1

alembic-downgrade:
	alembic downgrade -1

alembic-offline:
	alembic upgrade --sql > "00x_comment.sql"
	# alembic upgrade start_version:end_version --sql >migration.sql

docker-app-up:
	docker-compose build && docker-compose up

docker-app-down:
	docker-compose down

pytest:
	find . -name "*,cover" -type f -delete
	pytest -v --html=report.html --self-contained-html --cov=bookstore main_test.py tests/
	open -n -a /Applications/Google\ Chrome.app  "./report.html"
	coverage html --skip-empty
	open -a /Applications/Google\ Chrome.app  "./htmlcov/index.html"
