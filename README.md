# PyTesterApi

[![Build](https://github.com/paulocoutinhox/pytester-api/actions/workflows/build.yml/badge.svg)](https://github.com/paulocoutinhox/pytester-api/actions/workflows/build.yml)

This is a simple python project that uses all the power of PyTest to write tests to check local or external API response.

# Structure

The file `tests/api_test.py` has some fixtures to:

- Run before all tests
- Run after all tests
- Run before each tests
- Run after each tests

And have some tests that check the JSON data from a remote API.

# Use case

A simple use case can be start a docker (or docker compose) with database, that need reset their data for each test.

1. When all the tests start the fixture can start the docker or docker compose.
2. When each test start, the fixture can reset the database or anything else.
3. When each test finished, the fixture can cleanup the database.
4. When all the tests finished, the fixture can stop the docker.

Obs: You can simple execute any command with the code:

```python
r.run(["ls", "-lah"])
```

Check the file `tests/api_test.py` for more examples.

# Requirements

- Python 3

# How to use?

Clone the project:

```bash
git clone https://github.com/paulocoutinhox/pytester-api.git
cd pytester-api
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run tests:

```bash
python3 -m pytest
```

or

```bash
./build.sh
```
