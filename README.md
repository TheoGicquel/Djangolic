# Djangolic
# A django beverage crud website


## Installation venv
```
virtualenv venv
```

## Activer le venv
```
source venv/bin/activate
```

## Accéder au bon dossier pour lancer l'application
Se diriger dans le dossier suivant : /djangolic

## Effectuer les installations nécéssaire
Installer django :
```
pip install django
```

Installer django-crispy-forms :
```
pip install django-crispy-forms
```

Installer les librairies nécéssaire :
    - Se déplacer dans le dossier : /djangolic/Gueze/Static
    - Taper la commande :
```
yarnkpg add bootstrap jquery-slim @popperjs/core
```
Et la commande
```
yarnkpg add @fortawesome/fontawesome-free
```

## Effectuer les migrations 
```
./manage.py makemigrations task_and_user
```
```
./manage.py sqlmigrate task_and_user 0001
```
```
./manage.py migrate
```

## Lancer l'application
Se dirigier dans la source du projet : /djangoProject2/
Taper la commande :
```
./manage.py runserver
```
Aller sur votre navigateur et écrire le lien : 127.0.0.1/task_and_user







