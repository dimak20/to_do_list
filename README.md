# TODO list 📝
> Django project 

Custom TODO list


(Optional) Use this credentials to log in:

**Username:** `admin`

**Password:** `admin`
## Getting started

1. Clone repository  
```shell
git clone https://github.com/dimak20/to_do_list.git
```
2. Then, create and activate .venv environment  
```shell
python -m venv env
```
For Unix system
```shell
source venv/bin/activate
```

For Windows system

```shell
venv\Scripts\activate
```

3. Install requirments.txt by the command below  


```shell
pip install -r requirements.txt
```

4. You need to make migrations
```shell
python manage.py makemigrations
python manage.py migrate
```
5. (Optional) Also you can load fixture data
```shell
python manage.py loaddata auction_data.json
```


6. And finally, create superuser and run server

```shell
python manage.py createsuperuser
python manage.py runserver # http://127.0.0.1:8000/
```


### Project configuration

Your project needs to have this structure


```plaintext
Project
├── to_do_list
│   ├── __init__.py
│   ├── models.py
│   └── views.py
│   ├── settings.py
│   └── urls.py
│
├── manage.py
│
├── templates 
|
|
├── README.md
│   
├── static
│
├── to_do_management
│   ├── __init__.py
│   └── admin.py
│   ├── apps.py
└   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── requirements.txt
```


## Features

* Creation tasks
* Creation tags
* Cheange task status
* Delete and update tasks/tags
* Sort by content, id, status, dates
