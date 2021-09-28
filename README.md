# Code Institute: Milestone Project 4 #

## Afan Forest Adventures ##
This project has been created for my Milestone Project 4 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site using HTML, CSS, Javascript, Python, Django, a relational database and Stripe payments.

Afan Forest Adventures is a fictional website for a fictional outdoor activity company. The aim is to provide a website where users can find and buy activities sold by Afan Forest Adventures, with the prupose of increasing the sales for the company. Users will interact with the website through being able to find, book and pay, edit their bookings, view current and past bookings and create reviews of past bookings.

My deployed project can be viewed live [here](https://afan-forest-adventures.herokuapp.com/).

## UX ## 

### Main Aims ### 
* To create a website that allows users to find a product, book the quantity required and pay in a simple, easy-to-follow process.
* To create a full stack website where the siteowner/admin can satisfy all CRUD functions, allowing them to Create, Read, Update and Delete products, blog posts and gallery images.
* To create a full stack website where the site users can Create, Update and Delete their shopping basket and Read the blog and gallery.
* To implement Stripe to take payments.
* To create a website that provides a quick and simple way for members to view and their order from their member account.
* To make a website that uses Javascript to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### User Stories ###
#### Potential user's perspective ####
* I am a potential customer, I want to know what activities are offered, so I can decide if I want to buy any.
* I am a customer who will be visiting Afan Forest Adventures, I want to know what facilities are available, so I can plan my day/stay.
* I am a MTB instructor, I want to know what courses Afan Forest Adventures offer, so I can improve my qualifications.
* I am visitor to Afan Forest Adventures, I want to know their contact details, so that I can ask them my questions.

#### User's perspective ####
* I am a customer who has booked an activity, I want to view my order history, so I can see what I have booked.
* I am a customer, I want a quick and simple way of making my purchase.
* I am a customer who is booking a course that is paid by my employer, I want a copy of my order, so I can reclaim the cost of the course.

#### Site owner's perspective ####
* I am the admin for Afan Forest Adventures, I want a simple method of managing products, so I can upload, edit and delete what we offer.
* I am the admin for Afan Forest Adventures, I want a simple method of managing the gallery, so  I can upload, edit and delete the images.
* I am the admin for Afan Forest Adventures, I want a simple method of managing the blog, so  I can upload, edit and delete the images.

### The 5 Planes of UX ###
Having created the user stories so that I knew who I was designing my website for, I then followed the user centred design process to create a website that would answer the above user stories.
1.	**Strategy Plane:**
    * When addressing the strategy plane, I focused on who the website users were likely to be and the objectives the website needed to meet to attract these users. I kept in mind the question: Why is the Afan Forest Adventures website so special?
        * Reason for the website’s existence – To promote Afan Forest Adventures' business and to allow their customers to purchase their products online.
        * Culture of the audience – people wanting to visit the Afan Forest which may include:
            1.	People wanting to stay the night/holiday.
            2.	People wanting to take one of the courses offered by Afan Forest Adventures.
            3.	People who enjoy the outdoors.
            4.	People who want to relax and unwind.
            5.	People looking to try an activity for the first time.
            6.  People who enjoy outdoor activities.
        * User demographic – the website is open to everyone and Afan Forest Adventures is likely to have a large user audience with a variation in understanding of the Afan Forest, outdoor activities etc.  The website branding therefore needs to appeal visually to all ages and genders. It must also be able to be navigated easily as the users could have a wide range of computer competency levels.
    * I researched existing websites that promote the Afan Forest as well as outdoor activity websites including:
        * [Afan Forest Park](https://dramaticheart.wales/home/discover-our-area/attractions/afanforestpark/
        * [Bryn Teg House](https://brynteghouse.com/mountain-biking-afan-forest-park/)
        * [SUP Cardiff](https://www.supcardiff.co.uk/sup-rental/)
        * [Monmouth Canoe](https://www.monmouthcanoe.co.uk/canoe-kayak/canoe-kayak-guided-river-trips/)

    This helped me to gather information on what these websites offer their users; the pros and cons that I liked as a user of their website and to identify the features and information they provided. This gave me ideas of how to address my user’s needs but also how I could further improve my user’s experience to add value to the Afan Forest Adventures website. 
    
    This gave me the following ideas:
    * Create an online shop with the products sold by Afan Forest Adventures.
    * Create a blog 

2.	**Scope Plane:**
    * When addressing the scope plane, I focused on what features were to be included on the website and its key functionality to meet the all the user’s needs. I also needed to combine these with Stripe and Django as per the requirements for my Code Institute MSP4. I kept in mind the question of: Why would a user want this?
	    * Requirements: there would be 3 types of user categories - guest (anonymous users of the site who aren't logged to a profile), customers (who have created an account) and superusers (admin for Afan Forest Adventures).
            * All users (guest, customers and superuser): Learn about the business, search for product, read the products (campsite, activity, courses), read product details on product if selected, update quanitity of product qanted, add product to bag, update shopping bag by adjusting product quantity, delete item from shopping bag, make purchase through checkout, view order summary, read blog, read blog details on blog if selected, read (view) gallery, read image details if gallery image selected and create an account.
            * Customers and superusers: have the additional requirments of beind able to login to their account and view past orders.
            * Superusers: have the additional requirments of managing the site which includes being able to edit (for example to adjust the price), delete products and add new products; edit, delete and add blog posts; edit, delete and add gallery images.
        * From the above requirements, I identified the following Key features: 
            * All users: a simple and easy method to search for products, to navigate around the site and select categories of products, to sort the products on the page (e.g. by lowest price first), to create an account, to view the blog and gallery, to view more product details, to adjust quantity of a product, to ad to shopping bag, to adjust items in the shopping bag and to checkout.
            * Customers and superusers: to login to account and view order history.
            * Superusers: to manage products, blog and gallery.
        * CRUD functions: To achieve the above requirements and key features I needed to implement the Create, Read, Update & Delete (CRUD) functions for my database. I decided to use them in the following ways:
            1. Create: 
                * Create a new user (account)
                * Allow superuser to create (add) a product
            2. Read:
                * To search, find and read products in the database
                * To read blogs in the database
                * To view gallery images in the database
            3. Update:
                * Update quantity of a product on product details page
                * Update quantity of a product in shopping bag
                * Update user profile information from checkout form
                * Allow superuser to edit products
                * Allow superuser to edit blogs
                * Allow superuser to edit gallery inmages
            4. Delete: 
                * Delete a product from shopping bag
                * Allow superuser to delete a product
                * Allow superuser to delete a blog post
                * Allow superuser to delete a gallery image


### Technologies Used ###
* HTML5 used for the .html pages
* CSS used to style the html pages.
* Javascript used to make my website interactive with the carousel and collapsible accordian.
* [jQuery](https://api.jquery.com/) javascript library used for my javascript code denoted by $ prefix on script.js.
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) to produce the secure passwords used in my project.
* [AWS Amazon Web Services](https://aws.amazon.com/) cloud-based storage service to store my static and media files.
* [Balsamiq](https://balsamiq.com/) used to create my wireframes.
* Jinja - templating language for some of my Python code denoted by {% %}.
* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) used to check the validity of my html code for all .html pages.
* [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input) used to check the validity of my css code for the style.css file.
* [JSHint](https://jshint.com/) used to check the validity of my javascript code for the script.js files.
* [PEP8 Online](http://pep8online.com/) used to check the PEP8 compliance of my Python code.
* [Am I responsive](http://ami.responsivedesign.is/#) used to check the responsiveness of my design on different screen sizes and for creating the first image in this README file.
* [Paint 3D](https://microsoft-paint-3d.en.softonic.com/) used to crop the screenshots of images added to this README.md file and testing.md file.
* [Google Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) used to generate Lighthouse reports on the performance of all my web pages once the project was deployed.
* [Heroku](https://www.heroku.com/what) to deploy my website.
* [Gitpod](https://www.gitpod.io/) to write my project code.
* [GitHub](https://github.com/) remote repository where my project is stored.
* [Font Awesome](https://fontawesome.com/) for the icons used throughout the website.
* [Bootstrap](https://getbootstrap.com/) to create a responsive website across mobile, tablet, desltop and large screen devices.
* [Bulma](https://bulma.io/) css framework for styling font awesome icons.
* [Stripe](https://stripe.com/) to handle secure payments.
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for user authentication, registration and account management.
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to produce and style the forms.
* [Django Countries](https://pypi.org/project/django-countries/) for the country codes to ensure they were in an acceptable format for Stripe.
* [Pillow](https://pillow.readthedocs.io/en/stable/) to allow images to work in the database.
* [SQLite](https://www.sqlite.org/index.html) database.
* [Heruko PostgresSQL](https://www.heroku.com/postgres) database.
* [Gunicorn](https://gunicorn.org/) used in the deployment to Heroku.
* [Gmail](https://www.google.com/intl/sv/gmail/about/#) to to send order confirmation emails to users.

### **Testing**
The testing that I undertook on my project is detailed in the [testing.md](testing.md) file. 

### **Using My Project**
If you would like to use or further develop this project, you can make a clone by completing the following steps. 
#### Prerequisites ####
You will need to have the following setup:
* An IDE (such as Gitpod)
* Python - programming language for the backened
* PIP - package installer for Python
* Git for project version control
* AWS account with a set up S3 Bucket
* Stripe Account for payment functionality
* Gmail Account for emails

#### Fork the repository ####
To make a copy of my project to your GitHub account, you can fork a copy of my project, with the following steps:
* Log in to your GitHub account (or create a new account).
* Search for my repository called KimLHill/MSP4.
* In the far right-hand corner of the screen at the top of the repository, click the ‘fork’ button next to the fork icon.
Further information about forking a repository can be found [here](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

#### Clone My Project ####
To run my project locally you can clone the project, with the following steps:
* Open GitHub.
* Select my project repository called KimLHill/MSP4.
* Click on the green ‘Code’ button.
* Click the clipboard icon next to the url to copy the url link.
* Open your IDE.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the url link you copied in step 4.
* Press enter to create your local clone.
Alternative methods of cloning my project can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

#### Local Deployment ####
Follow these steps to deploy locally:
* Install the required dependencies with command "pip3 install -r requirements.txt".
* In your [Gitpod account](https://gitpod.io/variables) select the variables tab and enter the following Environment Variables:
    * Name "SECRET_KEY"  Value <your key> Scope "*/*"
    * Name "STRIPE_SECRET_KEY"  Value <your key> Scope "*/*"
    * Name "STRIPE_PUBLIC_KEY"  Value <your key> Scope "*/*"
    * Name "STRIPE_WH_SECRET"  Value <your key> Scope "*/*"
* Make migrations to create the local database with command "python3 manage.py makemigrations" then "python3 manage.py migrate".
* Import the fixture folders with command "python3 manage.py loaddata categories" then "python3 manage.py loaddata products" then "python3 manage.py loaddata blog" then python3 manage.py loaddata gallery".
* Create a superuser with command "python3 manage.py createsuperuser" and follow the terminal instructions.
* Run the server with command "python3 manage.py runserver" and the project is now deployed locally.



### Media ###
The images used on my wireframes and website are from:
* [home hero image](https://images.pexels.com/photos/397096/pexels-photo-397096.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)
* [camping image](https://images.pexels.com/photos/6324131/pexels-photo-6324131.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)
* [glamping image](https://images.pexels.com/photos/5359324/pexels-photo-5359324.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [caravan image](https://images.unsplash.com/photo-1626680114529-3f6ffa002b80?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=632&q=80)
* [bbq image](https://images.pexels.com/photos/8522790/pexels-photo-8522790.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [dog image](https://images.pexels.com/photos/3680896/pexels-photo-3680896.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [segway image](https://images.unsplash.com/photo-1492558647888-45b0d471e2c3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1120&q=80)
* [Mountain biking image](https://images.unsplash.com/photo-1594942940158-af338884ac6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80)
* [walking image](https://images.unsplash.com/photo-1597120590849-a1d5a743d155?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80)
* [hiking image](https://images.unsplash.com/photo-1606262482703-496941e54337?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=685&q=80)
* [paddle boarding image](https://images.unsplash.com/photo-1472745942893-4b9f730c7668?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1169&q=80)
* [tombstoning image](https://images.unsplash.com/photo-1606330287762-9851d5dc6f16?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1032&q=80)
* [swimming image](https://images.unsplash.com/photo-1578253734010-32bb761af7e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1176&q=80)
* [mtb leader level 2 image](https://images.unsplash.com/photo-1621427259734-2c1167c9860d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80)
* [mtb leader level 3 image](https://images.pexels.com/photos/163491/bike-mountain-mountain-biking-trail-163491.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [bike maintenance image](https://images.pexels.com/photos/1154089/pexels-photo-1154089.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260)
* [Emergency outdoor first aid image](https://images.pexels.com/photos/5125748/pexels-photo-5125748.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [specialist outdoor first aid image](https://images.pexels.com/photos/5125690/pexels-photo-5125690.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [watersports first aid image](https://images.unsplash.com/photo-1582645502666-6727e63a027b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1119&q=80)
* [MTB benefits blog image](https://images.pexels.com/photos/2270328/pexels-photo-2270328.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [why afan forest blog image](https://images.pexels.com/photos/1112186/pexels-photo-1112186.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [picnic gallery image](https://images.pexels.com/photos/8208715/pexels-photo-8208715.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260)
* [squirrel gallery image](https://images.pexels.com/photos/5643876/pexels-photo-5643876.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [autumn walk gallery image](https://images.pexels.com/photos/3107873/pexels-photo-3107873.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [spring gallery image](https://images.pexels.com/photos/8355200/pexels-photo-8355200.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [winter gallery image](https://images.pexels.com/photos/163756/park-winter-russia-city-park-163756.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
* [deer gallery image](https://images.pexels.com/photos/1035367/pexels-photo-1035367.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)