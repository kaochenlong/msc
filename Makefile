server:
	uv run manage.py runserver

migration:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

shell:
	uv run manage.py shell
