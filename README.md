## Project Structure
```aiignore
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

## Development
To initialize database
```aiignore
flask --app flaskr init-db
```

To start debug mode
```aiignore
flask --app flaskr run --debug
```

To start server
```aiignore
flask --app flaskr run
```

To install the project
```aiignore
pip install -e .
```
verify
```aiignore
pip list
```

To run all the tests
```aiignore
pytest
```

To measure the code coverage of your tests, use the coverage command to run pytest instead of running it directly.
```aiignore
coverage run -m pytest
```
You can either view a simple coverage report in the terminal:
```aiignore
coverage report
```
To generate an HTML file for test report
```aiignore
coverage html
```
This generates files in the `htmlcov` directory. Open `htmlcov/index.html` in your browser to see the report.

## Deploy to Production
To build a wheel (`.whl`) file
```aiignore
python -m build --wheel
```
You can find the file in `dist/flaskr-1.0.0-py3-none-any.whl`. The file name is in the format of `{project name}-{version}-{python tag} -{abi tag}-{platform tag}`.

To install project to another machine
```aiignore
pip install flaskr-1.0.0-py3-none-any.whl
```

and then to initialize database
```aiignore
flask --app flaskr init-db
```