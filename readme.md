# Flask - Geocoder
-----
![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a) ![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)

A Flask Blueprint to find the distance from the Moscow Ring Road to the specified address. Yandex-geocoder was used to determine the coordinates.

## Installation

Install with pip:

```
$ git clone https://github.com/mtnylnky/Geocoder.git
$ cd Geocoder
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
geocoder
├── geocoder
│   ├── home
│   │    ├── static
│   │    │    └── css
│   │    │         └── style.css
│   │    ├── templates
│   │    │    └── index.html
│   │    ├── __init__.py
│   │    └── index.py
│   ├── static
│   │    └── css
│   │         └── main.css
│   ├── templates
│   │    └── base.html
│   ├── tests
│   │    └── test_basic.py
│   ├── __init__.py
│   └── get_data.py
├── config.py
├── tests.py
├── requirements.txt
├── readme.md
├── geocoder.log
└── run.py
```

## Flask Configuration
For queries, api key must be entered in `config.py`
```python
class Config:
    # Yandex-Geocoder Api Key
    API_KEY = "YOUR_API_KEY"
```
## Run Flask

```
$ python run.py
```
In flask, Default port is `5000`
Navigate to:  `http://127.0.0.1:5000/`

### How do queries happen?

Queries are made with both textbox in the app and http.

#### Textbox Request
After entering the `http://127.0.0.1:5000/` address, it is enough to write the address or coordinates in the textbox.

#### HTTP Request
Searching by adding `/?distance=` after localhost

With Place Name

```
http://127.0.0.1:5000/?distance=adress+name
http://127.0.0.1:5000/?distance=Moscow
http://127.0.0.1:5000/?distance=Beyoglu+Istanbul
```

With Coordinate
```
http://127.0.0.1:5000/?distance=lon,lat
http://127.0.0.1:5000/?distance=37.617635,55.755821
http://127.0.0.1:5000/?distance=37.617635+55.755821
```

* -lon : Longitude
* -lat : Latitude

## Unittest
```
$ python test.py
```

## Reference

Offical Website [Flask](http://flask.pocoo.org/)
