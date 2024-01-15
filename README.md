# Portfolio Project 4 - Full-Stack Toolkit

## Title

Finding the right consultant is more difficult than ever. That's why we've made it simple.

### This is how easy it works

1. Simply create a request for the consultant you are looking for.
2. Our partners present the best consultants to you.
3. Compare consultants and choose the one that is best for your organization.

![Mockup Image]()

## Live Site

[Go to application]()

## Repository

[View repository]()

---

## Catalouge

<li><a href="#about-the-project">About the Project</a></li>
<li><a href="#planing">Planing</a></li>
<li><a href="#target-group">Target Group</a></li>
<li><a href="#user-experince">UXD - User Experince Design</a></li>
<ul><li><a href="#storytelling">Storytelling</a></li>
<li><a href="#wireframe">Wireframe</a></li>
<li><a href="#flowchart">Flowchart</a></li>
</ul>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#surface-plan">The Surface Plan</a></li>
<ul>
<li><a href="#base">Base</a></li>
<li><a href="#homepage">Homepage</a></li>
<li><a href="#signup">Signup</a></li>
<li><a href="#login">Login</a></li>
<li><a href="#blogger-overview">blogger Overview</a></li>
<li><a href="#new-post">New Post</a></li>
<li><a href="#edit-post">Edit Post</a></li>
<li><a href="#delete-post">Delete Post</a></li>
<li><a href="#reader-overview">Reader Overview</a></li>
</ul>
<li><a href="#database-design">Database Design</a></ul>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#technologies-used">Technologies</a></li>
<li><a href="#credits">Credits</a></li>
<li><a href="#acknowledgements">Acknowledgements</a></li></ul>

---

<h2 id="target-group">Target Group</h2>


### Customers



### Partners



---

<h2 id="user-experince">UXD - User Experince Design</h2>
To better understand the customer journey i made a story about how a customer journey could look.

For base of the project i´ve made wireframes based on the user stories and the flowchart of customer/partner.

<h3 id="storytelling"></h3>


<h3 id="wireframe">Wireframes</h3>

![frontpage]()
![frontpage#2]()

![register account]()
![login]()

### User loged in

![user overview]()
![user request details]()
![user presented candidates]()

<h3 id="flowchart">Flowchart</h3>

![flowchart]()

---

<h2 id="user-stories">User Stories</h2>

* 
* 
* 
* 
* 
* 
*  
*
* 
* 
* 
* 
---

<h2 id="surface-plan">The Surface Plane</h2>

<h3 id="base">Base</h3>
To maintain a consistent layout throughout the application, Django dynamic pages are used for the navbar and footer.

Navbar
![navbar]()

Footer
![footer]()

<h3 id="homepage">Homepage</h3>


![hero]()


![mockup and cta]()


![step-by-step]()

The step-by-step explains in details how the applications work and we want to show that to attract the user who want to understand more before making a decision.

![quote]()

<h3 id="signup">Signup</h3>
The user is using the same signup page and chooses type of account, customer or partner, due to which type of account they will use.

![signup]()

<h3 id="login">Login</h3>
Its easy to login for returning user. Just fill in your username and password and you get logged in.

![login]()

<h3 id="blogger-overview">Blogger Overview</h3>

![user-overview]()

![request-details]()

<h3 id="new-post">New Post</h3>
When the user clicks on the button to make a new request, they get redirected to a form to fill in the details about the request.

![new-request]()

<h3 id="edit-post">Edit Post</h3>
From the overview the user can see the request and click on edit request if they need to make some changes on the request.

![buttons]()

![edit-post]()

<h3 id="delete-post">Delete Post</h3>


![buttons](.)

![delete-post]()

<h3 id="reader-overview">Reader Overview</h3>


![reader-overview](.)

![overview details]()

<h3 id="send-candidates">Send Candidates</h3>
The partner can see information about the request and when they have a candidate that suits the request, they can present the candidate to the customer.

![present-candidate]()

---

<h2 id="database-design">Database Design</h2>
On this project postgresql is used with ElephantSQL

[Database Diagram]()

### Key Models

### Blog

* 
* 
* 

---

<h2 id="testing">Testing</h2>
Link to the testing document.

[TESTING.md](https://github.com/williamtyn/jobin/blob/main/TESTING.md)

---

<h2 id="deployment">Deployment</h2>

The Code Institute student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

* Click the "Use This Template" button.
* Give your repository a name, and description if you wish.
* Click the Create Repository from Template to create your repository.
* Click the Gitpod button to create a gitpod workspace, this can take a few minutes.
* When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
* Use the following commands to commit your work,
git add . - adds all modified files to a staging area.

git commit -m "A short message exlaining your commit" - commits all changes to a local repository.

git push - pushes all your commited changes to your Github repository.

* Before making the first commit:
PLEASE MAKE SURE NEVER TO PUBLISH SECRET KEYS, ADD THE env.py TO A .gitignore TO AVOID PUSHING KEYS TO GITHUB.

### Heroku Deployment

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have dj_database_url and psycopg2 installed.

pip3 install dj_database_url
pip3 install psycopg2

5. Login to the Heroku CLI - heroku login -i
6. Run migrations on Heroku Postgres - heroku run python manage.py migrate
7. Create a superuser - python manage.py createsuperuser
8. Install gunicorn - pip3 install gunicorn
9. Create a requirements.txt file - pip3 freeze > requirements.txt
10. Create a Procfile (note the capital P), and add the following,

web: gunicorn jobin.wsgi

11. Disable Heroku from collecting static files

heroku config:set DISABLE_COLLECTSTATIC=1 --app jobin-compare-consultants

12. Add the hostname to project settings.py file

ALLOWED_HOSTS = []

1.  Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing

connect

14. In Heroku, within settings, under config vars select

Reveal config vars

15. Add the following

DATABASE_URL = URL to the database
CLOUDINARY_URL = URL to cloudinary
SECRET_KEY = The secret key

16. Commit and push in your CLI

git add .
git commit -m "Initial commit"
git push

17. Go back to the Deploy tab and press

Deploy Branch

18. Your deployed site can be launched by clicking Open App from its page within Heroku.

*During production Heroku Postgresql was no longer availible and therefore DATABASE_URL in Heroku Config Vars was changed to the ElephantSQL Postgres url.*

---

<h2 id="technologies-used">Technologies Used</h2>

* [HTML](https://sv.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [ElephantSQL](https://www.elephantsql.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Heroku](https://id.heroku.com/login)
* [Cloudinary](https://cloudinary.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [SimpleImageResizer](https://www.simpleimageresizer.com/)
* [Pagespeed](https://pagespeed.web.dev/)
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)
* [Techsini](https://techsini.com/multi-mockup/index.php)
* [Pexels](https://www.pexels.com)
* [Writer](https://writer.com/grammar-checker/)

---

<h2 id="credits">Credits</h2>

#### Code

* To help me get started with the project and understand the basics, i followed [Code Institute](https://codeinstitute.net/se/) and Matt´s Walktrough on "I Think therefore i Blog", big thanks for getting me started.

* Ed, Ger and Oisin, Tutors at [Code Institute](https://codeinstitute.net/se/) helped me solve some bugs in my code, big thanks.

#### Bootstrap


#### Django


#### Issues with code

<h2 id="acknowledgements">Acknowledgements</h2>
