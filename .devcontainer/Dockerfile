FROM python:3.12

RUN python -m pip install --upgrade pip \


COPY pyproject.toml .
RUN touch README.md \
    && mkdir -p src/python_package \
    && python -m flit install --only-deps --deps develop \
    && rm -r pyproject.toml README.md src
