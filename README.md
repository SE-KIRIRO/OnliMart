# OnliMart

**Table of Contents**

- [OnliMart](#onlimart)
- [Installation/Usage locally](#installationusage-locally)
- [Requirements](#requirements)
- [Install Redis](#install-redis)
- [install RabbitMQ](#install-rabbitmq)
- [Usage:](#usage)

## OnliMart

This is a django full web application created to provide the core fuctionalities of an e-commerce website. It includes email notifications and invoices improve customer experience. I have also implemented a recommendation engine with redis

## Installation/Usage locally

### Requirements

- python3.9
- docker installed -(for redis and rabbitmq)
- for windows use `wsl`

### install redis

best options is running redis on docker

```python
sudo docker run -it --rm --name redis -p 6379:6379 redis
```

### install rabbit mq

```python
sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

open the terminal and install python 3.9

```bash
pyenv install 3.9
```

**clone** the project

```bash
git clone https://github.com/SE-KIRIRO/OnliMart
```

open the folder and run the following commands

```bash
python -m venv venv #create virtual environment for the project
source venv/bin/activate # to activate the venv

pip install -r requirements.txt # to install dependencies

cd onlimart
python manage.py createsuperuser # follow the steps shown
python manage.py makemigrations
python manage.py migrate

```

with all migrations made and superuser created to run the appliation follow the following steps

```bash
python manage.py runserver
#open another terminal window activate the venv and run a celery worker
celery -A onlimart worker -l info
# and for webhooks open the stripe cli
stripe listen --forward-to localhost:8000/payment/webhook/
# make sure that redis docker container and rabbitmq containers are running
```