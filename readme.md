Step to build:

# create virtual environment
python3 -m venv /Users/jk4678/Documents/personal_website/venv

# run virtual enviroment
source venv/bin/activate
I think I have to run this each time: $ export PASSWORD='password'

# libraries to install
pip install flask, flask-wtf, python-dotenv
- wtf for forms
- dotenv for environment variables for the .flaskenv file

# save package dependencies 
'$ pip freeze > requirements.txt'
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
git clone <repo url>

# heroku deployment to <appname>.herokuapp.com
1. make heroku account
2. add credit card if you want to add custom domain
3. in app 'Settings' add ENV VAR like password to mongodb or other api passowrds ($ EXPORT CAP_VAR=abc in terminal for local os.enviorn)
4. need pip packages: gunicorn (Python Web Server Gateway Interface (WSGI) HTTP server)
5. needed to create Procfile with 'web: gunicorn app:<appname> (appname from FLASK env)'
6. install heroku cli and run '$ git push heroku HEAD:master' (AFTER you have pushed your code to the repo you created)

# custom domain with heroku google-domains cloudflare
*disclaimer: if you get heroku hobby $7/mo. or higher dyno you don't need this 
because you can enable ACM for ssl certs
1. goto google domains and buy a domain name
2. heroku domains:add <www.yourdomain.com> and/or <yourdomain.com> (without www) or use web interface
3. (IF YOU HAVE >= HOBBY TIER) get domain target with '$ heroku domains' then copy that into google domains dns tab under custom records with hostname www, CNAME type, data is domain target you copied
3. if on free tier register for cloudflare account
4. add custom domain to websites tab
5. get the cloudflare nameservers and add them to google domain website under dns -> custom name servers 
6. go back to cloudflare dns -> add record -> CNAME, root, DNS TARGET from heroku from website or using '$ heroku domains' 
7. goto ssl/tls tab in cloudfare and change full to flexible 
8. wait a couple mins should get email confirmation from cloudflare that your website is 'secured'
(both manual and automatic ssl from heroku needs paid dyno, cloudflare is free but only half secure)

# Login / Register
1. pip install Flask-Security 
2. 

# edit biography
1. can pre populate data with form.<field>.data = var or you can do it in the html with {%set var = var%} and {{form.<field>(value = var)}}