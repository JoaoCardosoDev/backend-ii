startproject:
	poetry run django-admin 
	
startapp:
	docker compose run --rm web poetry run python manage.py startapp $(APP)

build:
	docker compose build

down:
	docker compose down

clean:
	docker compose down --volumes

run: build