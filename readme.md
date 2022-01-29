Step to build:

# create virtual environment
python3 -m venv /Users/jk4678/Documents/personal_website/venv

# run virtual enviroment
source venv/bin/activate

# libraries to install
pip install flask, flask-wtf, python-dotenv, Flask-Security 
- wtf for forms
- dotenv for environment variables for the .flaskenv file

# save package dependencies 
pip freeze > requirements.txt
to save package dependencies like the package.json in node.js
reinstall using 'pip install -r requirements.txt'

# SSL handshake error timeout
dont use ssl library use certifi library
'tlsCAFile=certifi.where()' add this to the parameters of mongoClient
ALSO CANNOT BE ON WORK VPN

{% function %}
{{ expression }}
{# comment #}

# git version control
git config --global user.email "you@example.com"
git config --global user.name "Your Name"