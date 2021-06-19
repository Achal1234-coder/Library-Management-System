# Django Library Management System Project

# How to run the Project

## create virtual environment

```
virtualenv project
```

## Activate virtualenv to run this command

```
source project/bin/activate
```
## Clone the Repository by this command
```
git clone <copied_url>
```
## To install the requirement of this project run this command
```
pip3 install -r requirements.txt
```
## Change the directory to repository run this command for open postgre Sql
```
sudo -u postgres psql
```
## To create a database run this command
```
 \i create.sql
```
## Quit the database
```
exit
```
## Makemigartion command
```
python3 manage.py makemigartions
```
## And run migrate command but it is noted that manage.py should inside in that directory
```
python3 manage.py migrate
```
## Create Super user
```
python3 manage.py createsuperuser
```
## run the project by this command
```
python3 manage.py runserver

```

## Drop the Database
```
\i drop.sql
```
## deactivate virtualenv
```
deactivate
```
