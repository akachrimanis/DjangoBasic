import config

def basic_context(config):
    context = f"""
version: '3.11'
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    command: 'python manage.py runserver 0.0.0.0:8000'
    ports:
      - 8000:8000
    volumes:
      - .:/app
    depends_on:
      - db

  queue:
    build:
      context: .
      dockerfile: Dockerfile
    command: 'python -u consumer.py'
    depends_on:
      - db

  db:
    image: mysql:5.7.22
    restart: always
    environment:
      MYSQL_DATABASE: admin
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_ROOT_PASSWORD: root
    volumes:
      - .dbdata:/var/lib/mysql
    ports:
      - 33066:3306
"""
    
    return context