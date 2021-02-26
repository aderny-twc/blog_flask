# Simple blog on Flask 
### Download 

```
$ git clone https://github.com/aderny-twc/blog_flask.git
$ cd blog_flask
```

### Setting up a virtual environment 

```
$ python -m venv venv
$ source venv/bin/activate
(venv) pip install -r requirements.txt 
```

### Launching the project 

```
(venv) python app/main.py
```

## Project structure

```
blog_flask/
├── app
│   ├── app.py
│   ├── config.py
│   ├── main.py
│   ├── posts
│   │   ├── blueprint.py
│   │   └── templates
│   │       └── posts
│   │           └── index.html
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   └── view.py
├── LICENSE
├── README.md
└── requirements.txt
```

### urls

| url                         | description |
| --------------------------- | ----------- |
| http://localhost:5000/      | Home page   |
| http://localhost:5000/blog/ | Posts       |

