FROM python:3.11.4-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONBUFFERED 1


# Install system dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev


RUN pip install --upgrade pip

COPY requirements.txt /code

COPY requirements-noversion.txt /code
#COPY requirements.txt /code
#RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -r requirements-noversion.txt

#COPY ./entrypoint.sh /usr/scr/app/entrypoint.sh

# Copy the current directory contents into the container at /code/
COPY . /usr/src/app/entrypoint.sh


# Expose port 8000 to allow communication to/from server
EXPOSE 8000


# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


ENTRYPOINT ["/usr/src/app/entrypoint.sh"]