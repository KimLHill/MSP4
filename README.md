# **Code Institute: Milestone Project 4** #

## **Afan Forest Adventures** ##
This project has been created for my Milestone Project 4 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site using HTML, CSS, Javascript, Python, Django, a relational database and Stripe payments.

Afan Forest Adventures is a fictional website for a fictional outdoor activity company. The aim is to provide a website where users can find and buy activities sold by Afan Forest Adventures, with the prupose of increasing the sales for the company. Users will interact with the website through being able to find, book and pay, edit their bookings, view current and past bookings and create reviews of past bookings.

#### **My deployed project can be viewed live [here](https://afan-forest-adventures.herokuapp.com/).**

## **UX** 

### **Main Aims** 
* To create a website that allows users to find a product, book the quantity required and pay in a simple, easy-to-follow process.
* To create a full stack website where the siteowner/admin can satisfy all CRUD functions, allowing them to Create, Read, Update and Delete products, blog posts and gallery images.
* To create a full stack website where the site users can Create, Update and Delete their shopping basket and Read the blog and gallery.
* To implement Stripe to take payments.
* To create a website that provides a quick and simple way for members to view and their order from their member account.
* To make a website that uses Javascript to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### **User Stories**
#### Potential user's perspective
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

### **The 5 Planes of UX**
Having created the user stories so that I knew who I was designing my website for, I then followed the user centred design process to create a website that would answer the above user stories.
1.	#### **Strategy Plane:**
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
    * Create a blog to further promote the products sold by Afan Forest Adventures; to increase the interest for users and to give the users a reason to keep re-visiting the website to increase the chances of them making purchases and repeat purchases.
    * Create a gallery to promote the Afan Forest and the products sold by Afan Forest Adventures, again with the purpose of giving something extra to website users and promoting more of the products to increase the chances of the users making a purchase.
    * To provide an easy way of searching for the product the user is after.
    * To provide a simple checkout process to increase the chance of the user completing the purchase and not just adding it to their bag.
    * To provide contact details for Afan Forest Adventures such as phone and email, but also social media links to appeal to the wide age range of users and user contact preferences.
    * To provide a clean website layout that appeals to the wide range of users but targeting the outdoor/active key user groups identified above.
    * To provide a consistent website layout and experience across the site to keep familiarity and be suitable for use by people of all computer competency levels.
    * To provide a user account area to store past order history and profile information such as shipping/billing address.

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

3. **Structure Plane:**
    * When addressing the structure plane, I focused on the journey the website would take the users on. I kept in mind the question: What is an intuitive way to navigate through the content and features?
        * How to get there? I knew that my website should include a main navbar with tabs to enable users to easily navigate through the website content and a sub-navbar to easily navigate through the product categories. 
        * There would also be a products/blogs/gallery page to display a limited amount of information on the products/blogs/images but that links to a page with greater information detail if the user clicks on them. This allows the user to easily access more detail on the items they want to know more about, without being overloaded with information at first or having to search through lots of information to find what they want. 
        * I wanted some of the website like the home, products, gallery and blog pages to be open to all users, but for some pages like order history or the ability to manage products to only be displayed to the alloed users. I decided to have different tabs displaying, depending on whether or not a user was logged in. For example, a user who is already logged in doesn’t want to see ‘Register’ or ‘Login’ options, so instead can see 'My profile' and ‘Logout’ or 'Product Management' for superusers.
        * How will they move through the website?
            * Guest (not logged in). This user firstly views the home page, they can see the main navbar with a search bar to quickly find products and with links to the create an account, view their shopping bag, view blogs, view the gallery. The secondary navbar displays the product categories for ease of searching for products and showing the range of categories avaiable in the shop.
            * Customer and Superuser (logged in) This user can see the same as the guest, however the dropdown menu options provide different options for them. This provides the same flow through the website which is:
                * home page with contact details
                * search bar to quickly and easily find products to increase sales which is the main purpose of the website
                * access their account and view their shopping bag which are what the suer will be wanting and expecting to see
                * view blogs and gallery to further promote th products and to provide inspiration if the user is not sure what they want to purchase or to persuade them to purchase more.
                * The secondary navbar provides another prompt to search through the products.

4. **Skeleton Plane:**
    * When addressing the skeleton plane, I focused on keeping the layout design of the website familiar to the users by using a standard layout the users would be use to seeing. I kept in mind the question: What conventions will the user be familiar with? This led to the choices of:
        * a navbar at the top of the page
        * a main body
        * a footer at the bottom of the page
    * How to style the page? I knew that my website pages should be consistent in style and that they should use a standard page layout. I chose to use features the user would expect to see including:
        * logo linked to home page
        * social media links open new window to the relevant page
        * email icon opens new window to email provider
        * navbar dropdowns
        * navbar toggle on smaller screen sizes
        * contact details, social media details and copyright info in the footer

5. **Surface Plane:**
    * When addressing the surface plane, I focused on the website branding and details like the colour, fonts and images. I kept in mind the question: What will be appeal to my users?
        * Images – promoting the forest, being outdoors, outdoor activities and camping activities to appeal to the website’s users.
        * Colour scheme – I chose to use the colours of green, black and white as these are gender neutral colours that will appeal to people of all ages. Green is also associated with the outdoors so fits well with the business and will appeal to the website's users. They are also strong colours that will stand out from the potentially large number of colours in product, blog and gallery photos.
        * Icons – I chose to use font awesome icons across the pages where it could aid the user’s understanding and for greater visual appeal.
        * Logo – I chose to position the logo in the top left-hand corner of the website (within the navbar) as this is a convention of websites that users have to come to expect.
        * Call to action buttons - I chose to colour the call-to-action buttons in bright colours to attract the user and make them more likely to click them.
        * Fonts - I kep the fonts as common fonts that are clean and easy to read.

### **Features**
Features consistent across all the different pages of my project include:
1. **Navbar**
    * The navbar has the Afan Forest Adventures logo which, when clicked, returns the user to the home page. In the centre is a search bar with a visual search icon and 'search' placeholder text to make it really obvious what this feature is for. On the right-hand side are the navigation tabs linking to account, shopping bag, blog and gallery. These have visual icons relating to the tab to aid the user's understanding and for better visual appeal. The black (#000) fits with the colour scheme and provides a good contrast from the white background. A text-shadow effect, further enhances readability. When the user hovers over a navbar tab, the background colour of the tab changes to provide visual feedback as to which tab they are about to click. The navbar collapses to a toggle button on tablet and mobile devices for an improved user experience on smaller screen sizes. The navbar tabs have dropdown menus to further aid the user in navigating the website, these change depending on whether or not the user is logged in, to provide a better user experience by showing them only what they need.

### **Additional Features Implemented**
* I liked the idea of having the prompt to encourage users to spend more as this fits with the purpose of the website. The website was designed with a free next-day delivery bonus if the user spent £50 and added a percentage delivery charge if the grand total of the shopping bag was under this value. However, as the products sold by Afan Forest Adventures would not be shipped, no delivery charge was required at the moment. However this functionality may be required in the future for example if they decide to sell clothing or other phycial merchandise that needs to be shipped to the customer. So I set the free delivery cutoff to 0 so no charge was incurred, but so that the functionality remained in place to be easily added in the future. I Then added the incentive of a free coffee to be redeemed in the shop onsite, so nothing physical needed to be sent to the user, but provided a nice bonus to user's to spend more money! This prompt was in the toast-success when a user added an item to their basket that was under £50, with a further prompt in the shopping bag totals to further promote spending more money on the site!
* Added delay to order creation if not found in database to ensure an order isn’t added twice if the view is just slow. Done in webhook_handler.
* Added a stripe_pid field as a required field to order, to ensure each order is assigned a unique number and therefore prevents a second-order not being placed if a user orders the same items on two separate occasions, as the first order will have the different  stripe_pid to ensure the second order will be added to the database.
* Provided visual feedback in forms – text form inputs are greyed out when empty and the text changes to black as the input field is completed. Placeholders are used to prompt the user to submit the correct information for that form field. Furthermore, an asterix provides a visual indication that the form is a required field as a convention the user will be use to.
* Added a country dropdown menu to aid the user in selecting the correct two-digit code used by Stripe to identify each country.
* Footer icons turn bold when user hovers over them to help prompt user to click them and show which they are selecting.
* When hovering over links (e.g. navbar and buttons) the mouse cursor changes from an arrow to a pointed finger cursor to provide a visual indication to the user that they can click on this item and to encourage them to click it.
* Added overlays behind text on the home page to make this text easier to read and less distracting for th user, as it is positioned over the background image.
* Added a border and lightgreen background colour to dropdown navbar menu options to make them standout from the white background of the rest of the website to be more obvious to users. Each link within the dropdown menu bar changes to white when hovered over to make it obvious to users which one they are about to select.
#### **Javascript Features**
* Back to top arrows provide a simple way to return user to top of page, whilst this isn’t needed at the moment it would be useful in the future as more content is added to the website.
* To get the current year in the copyright information in the footer of the page.
* Toasts to provide helpful messages to the suer to confirm their actions have been either successfully completed or as an error message to alert the user to a problem.
* For the quantity change buttons to allow the user to simply click up or down buttons to change the quantity without needing to type in a number.
* For the loading spinning cirle when submitting the checkout form to provide visual feedback to the user that the form is submitting before they reach the checkout success page, to prevent the user from trying to re-submit the form.
* For the product search bar to enable users to quickly and easily search for the products they want.
* For the product sort options to choose and display products in the order of the users preference e.g. price low to high.
* To update or remove items from shopping bag to allow the user to easily adjust their order.


### **Technologies Used**
* HTML5 used for the .html pages
* CSS used to style the html pages.
* Javascript used to make my website interactive.
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

### **Credits**
* I used this [Stackoverflow post](https://stackoverflow.com/questions/40853952/bootstrap-footer-at-the-bottom-of-the-page) to find the mt-auto Bootstrap flexbox class to fix the footer to the bottom of the page.

### **Acknowledgements**
* My Code Institute mentor Seun Owonikoko whose feedback throughout the project influenced my website design, content and features.
* The Code Institute tutorial videos, especially from the 'Boutique Ado project'.
* My family and friends who tested my website on their devices and provided feedback for improvements.


### **Media**
The images used on my wireframes and website are from:
* [home hero image](https://images.pexels.com/photos/117843/pexels-photo-117843.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
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