# Mock Overflow- Simple Stack Overflow Clone

Mock Overflow is a Stack Overflow-like forum for users to ask and answer questiosn related to programming.

# Prerequisites:

## Dependencies

This app requires the <a href="https://pillow.readthedocs.io/en/stable/index.html">Pillow</a>, <a href="https://django-taggit.readthedocs.io/en/latest/">django-taggit</a>, and <a href="https://django-crispy-forms.readthedocs.io/en/latest/install.html">django-crispy-forms</a> external libraries to run. You should install them by the running the commmands below:

~~~
pip install django-taggit
pip install Pillow
pip install django-crispy-forms
~~~

## Installation

Before installing, make sure:

* All dependencies are installed
* Django is installed
* Python virtual environment (venv) is installed

1) Clone this repository 
~~~
git clone git@github.com:julianfssen/mockoverflow.git
~~~
2) Activate your virtual environment 
~~~
source your_env_name/bin/activate
~~~
3) Navigate to the project folder 
~~~
cd mockoverflow/mockoverflow
~~~
4) Start the server 
~~~
python manage-py runserver
~~~
5) Navigate to the localhost URL in your browser 
~~~
http://localhost:8000
~~~

## Usage

Go to https://mockoverflow.herokuapp.com/ to use the app.

Use the test account to try out the features:

~~~
Email: herokutest@gmail.com
Password: testing321
~~~

If the account does not work, register for a new account and you'll be able to use the app nornmally.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Released under MIT License

## Author
<strong>Julian Foo Siang Sen</strong> (julianfssen@gmail.com)
