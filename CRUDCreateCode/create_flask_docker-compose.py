import config

def basic_context(config):
    context = f"""
version: '3.8'
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    command: 'python main.py'
    ports:
      - 8001:5000
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
      MYSQL_DATABASE: main
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_ROOT_PASSWORD: root
    volumes:
      - .dbdata:/var/lib/mysql
    ports:
      - 33067:3306
"""
    
    return context