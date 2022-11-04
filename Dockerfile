# Another text
# Tuleeko konfliktia?
FROM python:3.8
WORKDIR /app
COPY . /app/
RUN pip install pipenv
RUN pipenv install --system
EXPOE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
