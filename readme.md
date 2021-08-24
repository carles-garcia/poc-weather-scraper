### Weather API scraper
Author: Carles Garcia Cabot

This proof-of-concept weather API scraper can retrieve the average temperatures
for a given city.

## How to run
- Python 3.9 (probably also works with +3.7)
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=.
python3 eltiempo.py average-min Gavà
python3 eltiempo.py average-max Gavà
pytest --cov . test
```

## Potential improvements
- Add unit tests. Currently, there's only one integration test
due to lack of time. It covers 75% of the code.