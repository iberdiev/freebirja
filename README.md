# freebirja

Simple freelance platform website build on Django. 

##### Make sure you have:
1. installed pip3
2. installed git
3. python3.5
4. installed virtualenv

## Installation manual

1. Download the project
```
git clone https://github.com/iberdiev/freebirja
```
2. Open needed directory
```
cd freebirja
```
3. Create a virtual environment with python3.5
```
virtualenv --python=/usr/bin/python3.5 myvenv
```
4. Activate virtual environment (for OS Linux)
```
. myvenv/bin/activate
```
5. Install all required components
```
pip3 install -r requirements.txt
```
6. Run django server
```
python3 manage.py runserver
```
7. Browse http://127.0.0.1:8000/
