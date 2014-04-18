# Adagio

> *Adagio* - A tempo having slow movement; RESTful at ease (see what I did there? :)

A simple project written as a companion to a presentation given at the 
April 2014 Nashville API Enthusiasts meetup group. It hopefully demonstrates the
simplicity and power of using a fully baked framework for writing and maintaining
your RESTful APIs.

# Requirements

* Python 2.7
* virtualenv-wrapper (use brew or your favorite package manager)
* a handful of python packages

# Quick start

```bash
# Create a virtualenv (requires virtualenv-wrapper)
mkvirtualenv adagio
workon adagio

# Clone the source
git clone https://github.com/abemusic/adagio adagio_root
cd adagio_root

# Install requirements
pip install -r requirements/local.txt

# Move into the Django project's root
cd adagio

# Set up the database
python manage.py syncdb --noinput
python manage.py migrate

# Run the dev server
python manage.py runserver

# Point your web browser to http://localhost:8000
```
