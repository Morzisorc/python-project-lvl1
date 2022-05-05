#Makefile

install: #установка poetry
	poetry install

brain-games: #запуск
	poetry run brain-games

.PHONY: brain-games

build: #собрать пакет и убедиться, что вы его правильно настроили
	poetry build
	
publish:  #публикация пакета, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run

package-install: #установка пакета из операционной системы
	python3 -m pip install --user  --upgrade --force-reinstall dist/*.whl

lint: #запуск линтера
	poetry run flake8 brain_games