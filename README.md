# freebirja

Simple freelance platform website build on Django. (no styles/pure backend)

##### Make sure you have:
1. installed pip3
2. installed git
3. python3.5
4. installed virtualenv
5. Django==2.0.1
## Running via Docker container
1. Go to root directory and build an image
```
docker build -t freebirja_image . 
```
2. Run docker container
```
docker run --name webapp -p 8000:8000 freebirja_image
```
3. Browse http://127.0.0.1:8000/
## Installation manual

1. Download the project
```
git clone https://github.com/iberdiev/freebirja
```
2. Open needed directory
```
cd freebirja
```
3. Create a virtual environment
```
virtualenv myvenv
```
4. Activate virtual environment (for OS Linux)
```
. myvenv/bin/activate
```
5. Run django server
```
python3 manage.py runserver
```
6. Browse http://127.0.0.1:8000/
