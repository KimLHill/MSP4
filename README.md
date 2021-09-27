# Code Institute: Milestone Project 4 #

## Afan Forest Adventures ##
This project has been created for my Milestone Project 4 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site using HTML, CSS, Javascript, Python, Django, a relational database and Stripe payments.

Afan Forest Adventures is a fictional website for a fictional outdoor activity company. The aim is to provide a website where users can find and buy activities sold by Afan Forest Adventures, with the prupose of increasing the sales for the company. Users will interact with the website through being able to find, book and pay, edit their bookings, view current and past bookings and create reviews of past bookings.

## UX ## 

### Main Aims ### 
* To create a website that allows users to find an outdoor activity, book the quantity required and pay in a simple, easy-to-follow process.
* To create a website that provides a quick and simple way for members to view and edit their upcoming bookings from their member account.
* To create a website that provides a quick and simple way for members to leave reviews on past bookings from their member account, to encourage members to leave reviews which may help to increase sales of the product.
* To make a website that uses Javascript to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### User Stories ###
* I am the owner of the Afan Forest Adventures, I want a website that allows users to quickly book and pay for my products, to increase my sales.
* I am a potential customer, I want to know what activities are offered, so I can decide if I want to buy any.
* I am a customer who will be visiting Afan Forest Adventures, I want to know what facilities are available, so I can plan my day/stay.
* I am a MTB instructor, I want to know what courses Afan Forest Adventures offer, so I can improve my qualifications.
* I am visitor to Afan Forest Adventures, I want to know their contact details, so that I can ask them my questions.


### Technologies Used ###
* HTML5 used for the .html pages
* CSS used to style the html pages.
* Javascript used to make my website interactive with the carousel and collapsible accordian.
* [jQuery](https://api.jquery.com/) javascript library used for my javascript code denoted by $ prefix on script.js.
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) to produce the secure passwords used in my project.
* [AWS Amazon Web Services s3](https://aws.amazon.com/) cloud-based storage service to store my static files.
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
* [Bulma]()


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