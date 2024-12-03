FROM python:3.12

WORKDIR /code
COPY --link --chown=1000 . .


RUN pip install --upgrade pip
RUN pip install pytest pytest-cov pre-commit
RUN pip install --no-cache-dir -e .
RUN pre-commit install-hooks
