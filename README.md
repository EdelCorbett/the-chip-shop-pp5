# the-chip-shop-pp5
A online ordering site for a fast-food takeaway

 ## LIVE LINK  [The Chip Shop](https://the-chip-shop-pp5-7f84f31ffc3b.herokuapp.com/)
 ## Link to [Github repository](https://github.com/EdelCorbett/the-chip-shop-pp5)

 ## Strategy

This site is developed for a family run fast food take so customer can view the menu, place an oder and select the option to collect or have their order delivered.

---
## Goals
The Goal of this site is to provide the business with a ordering system where customers can order and pay for their order so it save the staff time.For the customer this site will provide a clear menu and a easy way of ordering and paying for their order.


---
## Agile Methodology
Github projects was use to follow agile principles. Using this help me organise my user stories with acceptance criteria and tasks in to EPICS(milestones), once I had created the user stories I then group them in to 9 different Epics 


### [Project Board](https://github.com/users/EdelCorbett/projects/15)

The Project board was divided in to 4 columns todo,In progress, done and bugs 
----
![](documentation/images/projectboard.png)

----
## MoSCoW Prioritization
In this project MoSCoW was use to prioritize the most important features
## Wireframes
| PAGE                  |   Wireframes    |
|-----------------------------|------------|
|  Home          | <details><summary>image</summary><img src="./documentation/wireframes/desktop-home.png"></details> | 
|   Sign up /register        | <details><summary>image</summary><img src="./documentation/wireframes/desktop-signup.png"></details> | 
|  Sign up mobile         | <details><summary>image</summary><img src="./documentation/wireframes/mobile-signup.png"></details> | 
| Menu Mobile         | <details><summary>image</summary><img src="./documentation/wireframes/mobile-menu.png"></details> | 
|  Home Mobile          | <details><summary>image</summary><img src="./documentation/wireframes/mobile-home.png"></details> |

-------
![Entity-Relationship Diagram](documentation/images/erd-image.png)

The Data model user in this project were for
### Menu App
#### Category Model
| Name          | Field Type    |
| ------------- | ------------- | 
|    name  | CharFeild     | 
|    friendly_name |  CharField  |
---
 #### Menuitem Model
| Name          | Field Type    |
| ------------- | ------------- | 
| category  | ForeignKey   | 
|   name| CharField   |
|   description | TextField |
| price | DecimalField |
|   image_url |  URLField    |
|    image |  ImageField   |
----
#### Favorite
| Name          | Field Type    |
| ------------- | ------------- | 
|   user | ForeignKey   | 
|  menuitem| ForeignKey  |
   
----

### Checkout App

#### Order Model
| Name          | Field Type    |
| ------------- | ------------- | 
| order_number  | CharField  | 
|   user_profile | ForeignKey   |
|  full_name| CharField  |
|   email | EmailField|
|    phone_number | CharField    |
|    country |  CountryField  |
| postcode |  CharField |
|       town_or_city |  CharField  |
 |   street_address1 |   CharField  |
|    street_address2 |   CharField  |
|  county|  CharField  |
|     date|  DateField  |
|  delivery |  DecimalField |
| order_total|  DecimalField  |
|     grand_total|  DecimalField  |
|   original_basket|  TextField  |
|    stripe_pid| CharField   |
----
####  OrderLineItem
| Name          | Field Type    |
| ------------- | ------------- | 
| order  | ForeignKey | 
|   menuitem | ForeignKey   |
  quantity|  IntegerField|
|   lineitem_total | DecimalField|
----

### Profiles App

#### UserProfile
| Name          | Field Type    |
| ------------- | ------------- | 
|user  |  OneToOneField | 
|    default_phone_number | CharField    |
|    default_country |  CountryField  |
| default_postcode |  CharField |
|       default_town_or_city |  CharField  |
 |   default_street_address1 |   CharField  |
|    default_street_address2 |   CharField  |
|  default_county|  CharField  |
| default_delivery_option | CharField |
----

### Review App
| Name          | Field Type    |
| ------------- | ------------- | 
| user  | ForeignKey  | 
|  menuitem  |ForeignKey  |
| rating |  IntegerField |
|   message | TextField|
|  created_at | DateTimeField |
|  comment  | TextField |
----



### Inquiry App
| Name          | Field Type    |
| ------------- | ------------- | 
| name  | CharField | 
|   email | EmailField   |
| phone|  CharField |
|   message | TextField|
|  created_at | DateTimeField |
|  contacted | BooleanField |
----
---
# User Experience UX
----
Vistor to this site are here to view menu and make an order. The design is simple with an easy checkout process and a clear menu with images. 
-----

## Deployment
### Heroku
This Project was deployed through [HEROKU](https://www.heroku.com/) using these steps:

1. Create a Heroku account 
2. Then select New
3. [Select Create new app](documentation/heroku/heroku-new.png)
4. Name the App, select region
5. [Select Create app](documentation/heroku/name_region.png)
6. [Then select Settings from the menu bar](documentation/heroku/setting.png)
7. [From here scroll down to Config Vars and the KEY and VALUE to the list](documentation/heroku/config.png)
8. Next add build packs for this project Python was used
9. [Then go to Deploy in the menu bar](documentation/heroku/deploy.png)
10. [Choose GitHub then choose connect to github](documentation/heroku/deploy-method.png)
11. Now enter repository name in search 
12. Then click connect
13. From here scroll down and pick either automatic Deploy or manual deploy
14. [The app is now been built](documentation/heroku/building.png)
15. [Once this has finished click view to go to app](documentation/heroku/deployed_success.png)

### Local deployment

1. Clone the repository.

 - https://github.com/EdelCorbett/the-chip-shop-pp5

 2. Set up a virtual environment.

- Use the command 

        python3 -m venv venv 
        
   to create a new virtual environment named 'venv'.
- Activate the virtual environment with 

        source venv/bin/activate.

3. Install necessary packages.
 Then Run

        pip install -r requirements.txt 
        
        
   to install the dependencies required for the project.

 4. Create a env.py file.

 5.

 - Import the os module with import os.
 - Set your secret key with os.environ["SECRET_KEY"] = 'your secret key'.
 - Provide the database URL with os.environ["DATABASE_URL"] = 'your database url'

6. In settings.py File
 - Specify the debug mode ["DEBUG"] = 'True' or 'False'.
- Define the allowed hosts with os.environ["ALLOWED_HOSTS"] = 'app name.herokuapp.com','localhost'.
- Add  to installed apps
 

6. Set up and configure the database.

- Create the database
- Apply migrations to the Database 

- In terminal first run 

        python manage.py makemigrations

    Then Run
    
        python manage.py migrate

7. Create the superuser.

    In terminal
    
       python manage.py createsuperuser

8. Then you be promted to enter a user name and password once this is done

        python manage.py runserver

### Setting Up a Database with ElephantSQL

1. Go to [ElephantSQL website](https://www.elephantsql.com/) and register for a new account.

2. Once registered, create a new database instance.

3. Assign a unique name to your database and opt for the free tier plan.

4. Proceed by clicking on "Select Region".

5. Choose a region that is close to you 

6. Review your selections by clicking on "Review".

7. Create your new database instance by clicking on "Create Instance".

8. Access your new database by clicking on its name, which will take you to the dashboard.

9. In the dashboard, you'll find the URL for your database. You'll need this URL to connect your Django project to the database.
### Forking a Repository
Forking a repository allow you to make a copy of the repository so you can make changes with out affecting the main repository.

#### Steps to forking 
1. Go to Github account
2. Then choose the repository you wish to copy
3. Now at the right hand coner of the page select the "fork" button
4. Now the copy for the repository is availble




# Technologies And Languages

## Languages 

- [HTML](https://html.com/)
- CSS
- [JavaScript](https://www.javascript.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
---
## Imported 
- [Django-allauth](https://pypi.org/project/django-allauth/) authentication library used to create the user accounts.

- [Gunicorn](https://pypi.org/project/gunicorn/)  web server used to run the website

- [AWS](https://aws.amazon.com/)

- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)

- [Dj-database-url](https://pypi.org/project/dj-database-url/)

- [Psycopg2](https://www.psycopg.org/)


---
## Technologies Used
 - [Techsini.com](https://techsini.com/multi-mockup/index.php)
 - [ElephantSQL website](https://www.elephantsql.com/) 
 - [VS Code](https://code.visualstudio.com/)
 - [Balsamiq](https://balsamiq.com/)
 - [Favicon](https://favicon.io/)
 - [GitHub](https://github.com/) 
 - [dbdiagram.io](https://dbdiagram.io/) was used to create Entity Relationship Diagram
---
## Credits 
* [Code Institute](https://codeinstitute.net/) Boutique Ado walk-through project
* [Very Academy](https://www.youtube.com/@veryacademy) tutorials for understanding of django
* [Codemycom](https://www.youtube.com/@Codemycom) tutorials for understanding of django
* [Pixbay](https://pixabay.com/)  Images
* [Unsplash](https://unsplash.com/) Images

* [Font awesome](https://fontawesome.com/): Icons
* [Coolors](https://coolors.co/) generate color palette

## Acknowledgements 
I would like to acknowledge 
* [Code Institute](https://codeinstitute.net/)
* Juliia Konn My Mentor for her advice and support during the project.
* My Family members who help me test the app 
* This project was built for educational purposes by Edel Corbett  