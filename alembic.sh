# 1. Initialize alembic database migration flow

alembic init alembic

# 2. This will scan the models and generate upgrade & downgrade scripts
alembic revision --autogenerate -m “Initial tables”

### 3. RUNNING DB MIGRATIONS ###

# following command will run all migration script and bring it to latest version
alembic upgrade head
# If we like to incrementally upgrade and check for some errors
alembic upgrade +1
# To undo last migration
alembic downgrade -1
# To get more information
alembic current
alembic history - verbose
# generate SQL for upgrade
alembic upgrade start_version:end_version --sql >migration.sql
