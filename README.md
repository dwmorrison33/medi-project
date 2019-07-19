## Medi Weightloss Project

#### Simply clone the project into a directory of your choice

```sh
$ git clone https://github.com/dwmorrison33/medi-project.git
```

#### I added all files, including the default generated sqlite3 file, so that you can run with the data I created on my side. Also, I included the virtualenv that I used, so that you won't have to create a virtualenv manually.

**Change directory to medi-project to access the project**
```sh
$ cd medi-project
```
**Activate virtualenv from base directory**
```sh
$ . venv/bin/activate
```
Your virtual environment should now be activated

#### Usage from base dir
**Change directory again**
```sh
$ cd medi-project
```
**Launch server**
```sh
$ python manage.py runserver
```
**Now launch a browser and go to the http://localhost:8000/products**

#### Final
Thats it, you can now view the website and to add/edit products, login into the admin @**http://localhost:8000/admin**
Username: admin
Password: Password123
