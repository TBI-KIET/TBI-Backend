# Official TBI-KIET Website

## Setup:

### To run the project locally on your system:

1. Fork the repository.

2. Copy the URL of the Forked Repository.
    
3. To clone the repository:

```sh
$ git clone https://github.com/devyanshiiii21/tbi-kiet-website/
```
4. Change to the repository directory on your computer.

```sh
$ cd tbi-kiet-website
```
5. Create a virtual environment.

```sh
$ python -m venv [name of the virtual env]
```
6. Activate it.

```sh
$ source [name of the virtual env]/bin/activate
```
7. Install the dependencies.

```sh
(env)$ pip install -r requirements.txt
```
#### Note: (env) in the beginning indicates that the terminal session now operates in the activated virtual environment. 

8. Setup the database
```sh
(env)$ python manage.py makemigrations
```
```sh
(env)$ python manage.py migrate
```

9. Run development server.
```sh
(env)$ python manage.py runserver
```
#### Navigate to the url: http://127.0.0.1:8000/
