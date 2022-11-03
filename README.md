# About

This is a test project for my DevOps course.

# Installing required libraries

```shell
pip install pipenv
pipenv install
```

# Running software

```shell
pipenv shell
uvicorn app:app --reload
```

# Running in production

```shell
uvicorn app:app --host 0.0.0.0 --port 80
```