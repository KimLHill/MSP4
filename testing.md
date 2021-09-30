# **Testing**

## **User Stories**

### **Potential user's perspective**
* **I am a potential customer, I want to know what activities are offered, so I can decide if I want to buy any.**
    * From the home page click the 'Book your adventure now' button or the 'products' button to be taken to the all products page.
    * From the search bar by typing for the activity they want to know whther it is offered.
    * From the 'activities' tap in the secondary navbar and selecting one of the dropdown menu options to explore the activity options.
* **I am a customer who will be visiting Afan Forest Adventures, I want to know what facilities are available, so I can plan my day/stay.**
    * From the secondary navbar this user can see that Afan Forest Adventures offers a campsite and from the dropdown can see the other ioptions for caravan, glamping etc. They can also see the activities and courses to see the range of offerings.
    * This user could also check out the gallery from the 'gallery' button on the homepage or 'gallery' in navbar.
    * This user could also check out the social media or contact the centre via the details in the footer.
* **I am a MTB instructor, I want to know what courses Afan Forest Adventures offer, so I can improve my qualifications.**
    * From the search bar by typing in the name of the course they are interested in doing.
    * From the 'courses' tab on the navbar and selecting one of the categories depending on the qualification type or skills course they are after.
* **I am visitor to Afan Forest Adventures, I want to know their contact details, so that I can ask them my questions.**
    * From the 'Contact Us' section in the footer with options to contact via phone, email (linked to an email platform when clicked), or the social media channels of twitter, facebook and instagram (linked to an corresponding platform when clicked).

### **User's perspective**
* **I am a customer who has booked an activity, I want to view my order history, so I can see what I have booked.**
    * This option is reserved for customers with an account: From the navbar select 'My Account', login to the account to see their order history.
    * Guest users wihtout an account are provided with an order confirmation and email confirmation with their order details.
* **I am a customer, I want a quick and simple way of making my purchase.**
    * From the product details page; add item to bag which causes a toast-success messsage to appear with a link to 'go to secure checkout' taking them to their shopping bag or by clicking the shopping bag navbar tab; checking bag contents and clicking 'secure checkout' button; completing the form and finally clicking 'confirm order'. 
* **I am a customer who is booking a course that is paid by my employer, I want a copy of my order, so I can reclaim the cost of the course.**
    * This option is reserved for customers with an account: From the navbar select 'My Account', login to the account to see their order history.
    * Guest users without an account are provided with an order confirmation and email confirmation with their order details.

### **Site owner's perspective**
* **I am the admin for Afan Forest Adventures, I want a simple method of managing products, so I can upload, edit and delete what we offer.**
    * Once logged in, the superuser can acccess 'product management' from the dropdown menu on the 'my account' tab on the navbar to take them to the form to add a product. When viewing any of the products either from the all products page, products page or products details pages this user will have the option to edit or delete the products.
* **I am the admin for Afan Forest Adventures, I want a simple method of managing the gallery, so  I can upload, edit and delete the images.**
    * Once logged in, the superuser will have the option to edit or delete the gallery images either from the gallery page or image details pages. 
* **I am the admin for Afan Forest Adventures, I want a simple method of managing blogs, so  I can upload, edit and delete the images.**
    * Once logged in, the superuser will have the option to edit or delete blogs either from the blogs page or blog details pages.


## **HTML Validation**
I passed all my html code through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

**Note: Following errors ignored in W3CValidation testing (ignored in my error reporting below):**
* On most .html pages I had validation errors of: "Bad value" relating to my use of {{ url_for}} internal links for Python. These errors were to be expected as the html validator was not expecting to find these in html code. I therefore left the code the same and these errors still exist.
* I also had errors of: "Text not allowed in element ul in this context." This error related to the use of Jinja templating and is needed to determine which navbar tabs are displayed according to whether or not the user is logged into their account. This same error also relates to the use of Jinja for the url links in buttons which is required. I therefore chose to keep the code the same and these errors still exist. 
* On all .html pages except for the base.html page I had errors relating to the lack of declaring the lang, doctype and header elements. This is because these pages were extending from the base.html template. I therefore chose not to change my code and these errors still exist, but are to be expected.
* A "Warning: The type attribute is unnecessary for JavaScript resources" on all pages with a back to top arrow button. This related to the javascript code for the functionality of the back to top arrow button. As this was code I had created whilst following the Code Institute tutorial and because it was a warning not an error, I left this code unchanged and this warning is still present.  
  
### **Bag app**
1. #### **bag.html**
    * **W3C Validation:** No errors found.  

### **Blog app**
1. ### **add_blog.html**
    * **W3C Validation:** No errors found.  

2. ### **blog_detail.html** 
    * **W3C Validation:** No errors found.  

3. ### **blog.html**
    * **W3C Validation:** No errors found.  

4. ### **edit_blog.html**
    * **W3C Validation:** No errors found.  

### **Checkout app**
1. ### **checkout_success.html**
    * **W3C Validation:** "Error: Stray end tag div." This was caused by an additional div tag at the end of my code. I removed this unnecessary element and my code passed through the validator.

2. ### **checkout.html** 
    * **W3C Validation:** No errors found.  

### **Gallery app**
1. ### **add_gallery.html**
    * **W3C Validation:** No errors found.  

2. ### **edit_gallery.html**
    * **W3C Validation:** No errors found.  

3. ### **gallery_detail.html**
    * **W3C Validation:** No errors found.  

4. ### **gallery.html**
    * **W3C Validation:** No errors found.  

### **Home app**
1. ### **index.html**
    * **W3C Validation:** No errors found.  

### **Products app**
1. ### **add_product.html**
    * **W3C Validation:** No errors found.  

2. ### **edit_product.html**
    * **W3C Validation:** No errors found.  

3. ### **product_detail.html**
    * **W3C Validation:** No errors found.  

4. ### **products.html**
    * **W3C Validation:** Errors relating to the product sort selector code. As this was code that I had created by following the Code Institute Boutique Ado tutorial, I left this code unchanged. The errors related to the use of '==', 'not serializable as XML 1.0.' and 'none_none'.

### **Profiles app**
1. ### **add_product.html**
    * **W3C Validation:** Error relating to the use of tr tags used to create the rows in the form. I chose to ignore this error as it was used for the table formatting and I checked against the Code Institute tutorial example code which matched mine. 

### **Templates app**
1. ### **base.html**
    * **W3C Validation:** No errors found.  

2. ### **footer.html**
    * **W3C Validation:** No errors found.  

3. ### **main-nav.html**
    * **W3C Validation:** No errors found.  

## **CSS Validation**
I passed my css code through the [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input). 

### **Checkout app**
1. ### **checkout.css**
    * **CSS Validation:** No errors found..

### **Static folder**
1. ### **base.css**
    * **CSS Validation:** No errors found.

## **Javascript Validation**
I passed my javascript code from script.js through [JSHint](https://jshint.com/).

### **Checkout app**
1. ### **stripe_elements.js**
    * **JSHint:** 2 warnings and 1 error found.
        * Both warnings related to 'Eversion 6'. I researched this and found this [post](https://stackoverflow.com/questions/37247474/es6-in-jshint-jshintrc-has-esversion-but-still-getting-warning-using-atom) giving this comment /*jshint esversion: 6 */ to add to the top of the javascript code to resolve the warnings. I added this comment at the top of my js code and the warnings disappeared.
        * The error related to a missing semicolon on line 125. Adding a ';' corrected this issue and re-validating the code found no further errors.

### **Profiles app**
1. ### **countryfield.js**
    * **JSHint:** 1 warnings found.
        * The warning related to an "unnecessary semicolon" on line 5. Removing the ';' corrected this issue and re-validating the code found no further errors.
    


## **PEP8 Validation**
I passed my Python code through [PEP8 Online](http://pep8online.com/) and also used the 'Problems' feature in the Gitpod terminal to identify any problems in my code.

**Note: Following errors commonly found in PEP8 test (ignored in my error reporting below):**
Common errors identified in my Python code included:
* An error relating to expecting to find blank lines, this was because I had inserted my comments into the blank spaces, so the validator was reading 1 blank line not two. I added the extra blank lines where required to resolve these errors.
* A warning of "No newline at end of file". I addded the extra line where required to resolve these errors.
* Flake 8 errors for lines too long. I fix the line lenght errors where I could using '()' to split imports and '\' for other code. I didn't correct the errorn if breaking the line risked breaking the code such as in validators.

### **Afan app**
No errors were found in:
* urls.py
* wsgi.py

1. ### **settings.py**
    * **PEP8 Validation:** 4 errors and 1 warning
        * 4 x flake8 errors for "line too long". I chose to ignore these erros because they relate to the AUTH_PASSWORD_VALIDATORS.
        * The warning related to a trailing space, I removed the space to fix this error.

### **Bag app**
No errors were found in:
* apps.py
* bag_tools.py
* contexts.py
* urls.py
* views.py

### **Blog app**
No errors were found in:
* admin.py
* forms.py
* models.py
* views.py

### **Checkout app**
No errors were found in:
* init.py
* admin.py
* apps.py
* forms.py
* models.py
* signals.py
* urls.py
* views.py
* webhook_handlers.py
* webhooks.py

### **Gallery app**
* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py

### **Home app**
* apps.py
* urls.py
* views.py

### **Products app**
* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py

### **Profiles app**
* apps.py
* forms.py
* models.py
* urls.py
* views.py

## **Manual Testing of features**
The following manual tests were carried out on Microsoft Edge, Google Chrome and Mozilla Firefox:
* Social media links were hovered over to makesure they changed to their hover feature of bold to make them look bigger and then clicked on to make sure that they open in a new tab at the correct corresponding landing page.
* Navbar items were clicked on from each page to make sure that they navigate to the correct page.
* All buttons and links were clicked on to check that they take the user to the correct page.
* Clicking on the Afan Forest Adventures logo in the navbar returns the user back to the home page.
* Checked the mouse cursor changed from an arrow to a pointed finger when the user could click/swipe on an item they could select like navbar buttons, products items, blog items and gallery items etc.

### **Styling of navbar**
* I clicked on the secondary navbar tabs and ensured that the correct dropdown menu appeared with the corresponding category options, had the lightgreen background colour styling and the links changed to a white background when hovered over. The navbar worked as expected.

![dropdown-navbar-styling](https://user-images.githubusercontent.com/74603013/135285484-e3c27d54-5be2-4925-8504-32100c20c4b4.png)

### **Testing product page**
* I checked that I could view the product image, product name, product description, rating and price as intended.
* I checked that the qty + and - buttons worked as intended to change the qty with visual change in hover colour; that I could manually type in a qty and that an error was shown if the qty was not equal to or greater than 1.

![product-qty-check](https://user-images.githubusercontent.com/74603013/135369642-d1cf7427-d6ec-402e-855c-38a3847dd856.png)

### **Testing toast-success**
* I added an item to my bag to ensure the toast-success appeared to confirm to the user which item had been added, quantity, current bag cost and option to checkout. I chose an item that was under £50 to ensure the prompt to spend more for a free coffee was shown. This worked as planned.

![toast-success-2](https://user-images.githubusercontent.com/74603013/135371022-a518773d-6c5c-43aa-8f3b-5bc7a4c4f39a.png)

* I then added an item to my basket that was more than £50 to ensure the prompt wasn't shown in the success-toast.

![toast-success-no-prompt](https://user-images.githubusercontent.com/74603013/135371228-8e69705b-86c8-4fd7-af55-821226e7a523.png)

### **Testing shopping bag**
 
* I added an item to my bag, then viewed the bag. I made sure the shopping bag contained the product image, name, SKU, quantity, subtotal for the item the user had selected and checked that the bag total was correct. I chose an item that was under £50 to ensure the prompt to spend more for a free coffee was shown. I also made sure that once an item was in the bag that the bag icon in the navbar displayed teh current bag total price. This worked as planned.

![bag-prompt](https://user-images.githubusercontent.com/74603013/135372102-1a4dead7-ada3-44f8-86b6-f38b2a782cf9.png)

* I checked that if I added different items to my bag, that they displayed on their own row


![bag-rows](https://user-images.githubusercontent.com/74603013/135372460-3022ed97-75c7-416e-ab4d-707e1c324f43.png)

* I checked that the bag totals were calculated correctly with multiple items in the bag and that the prompt to spend more was removed if the bag was over £50 in total. I checked the user has the option to checkout or keep shopping.

![bag-total-correct](https://user-images.githubusercontent.com/74603013/135372674-beef5bb5-cb13-40a9-8f6c-060a48ceff08.png)

* I checked that I could update the qty from the bag page and that the success-toast with updated qty appeared.
![bag-update](https://user-images.githubusercontent.com/74603013/135373480-d36cf1a8-a1da-4fdc-bd6c-5c3789ca4f11.png)

* I then removed an item from the bag to confirm that the 'remove' button also worked and that the toast-success for removal displayed with the correct message. Along with the bag and total updating.

![remove-item](https://user-images.githubusercontent.com/74603013/135373765-b32e07bf-1ea7-45ba-b4d2-cf94d52b9fd1.png)


### **Testing search bar**
* I tested the search bar by first doing a search with no criteria and checking that it took me to the all products page and showed the toast  error message.

![no-search-criteria](https://user-images.githubusercontent.com/74603013/135384647-0f624eab-06f1-40d3-b5f2-fafef65d3c8f.png)

* I confirmed that searching for a product by name or category worked but typing water.

![Screenshot 2021-09-30 at 04-58-07 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135384822-3ec3fade-01fa-4cf7-8904-77d6c3039973.png)

* Then confirmed that the search functionality was also incorporating the description by searching for food which i knew wasn't in a product name or category but was in a product description. The correct product was returned.

![Screenshot 2021-09-30 at 05-00-47 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135385027-84243d11-ee15-4bac-a976-8f9286da4b3c.png)


### **Testing sort products**
* I navigated to the all products page and then went through each of the sort product options ensuring that the correct order then displayed. 

### **Testing Sign up form**
* I tested the link to login page if user already had account worked.
* I checked placeholder text and mandatory form fields were denoted.
* I tested the field validation messages by entering an unsuitable password.

![sign-up-error](https://user-images.githubusercontent.com/74603013/135375986-5ecbf75d-d712-48a5-abe0-8ce3c2821805.png)

* I then entered correct, viable information and submitted the form and confirmed that the page showed the 'verify email message' and the toast-alert message also displayed.

![verify-email-office](https://user-images.githubusercontent.com/74603013/135379433-2934225d-076a-43fd-a875-ceacc2c0f660.png)

* I tried to login without verifying my email and confirmed that I was taken to the 'Verify your email address' page again, couldn't access my account and toast alert confirmed where the verification email had been sent.

![confirm-verify](https://user-images.githubusercontent.com/74603013/135378503-1416565f-7a6e-43f8-bffa-c5e0d42e9d9d.png)

* I then checked my email account to confirm receipt of the email.

![email-inbox](https://user-images.githubusercontent.com/74603013/135379592-edc16930-cca7-44ac-b3cc-5b4ddde800d0.png)

* I also tested using a gmail address to confirm that the email were working for different email platforms that users might use.

![gmail-verify-email](https://user-images.githubusercontent.com/74603013/135379885-60bda79c-d175-4c02-ba53-60061d036e6a.png)

* I checked the email contained the verification process and followed the instructions to register my account.
* I clicked the verification link in the email and confirmed that I was taken to the website confirm email page.

![confirm](https://user-images.githubusercontent.com/74603013/135380106-a04819e8-199c-4885-beb1-f89588f7d280.png)

* I clicked the confirm button to makesure that the toast success for confirmed email verifcation appeared along with the contents of my bag that I had added before registering for an account and I was taken to the sign in page.

![confirm-success](https://user-images.githubusercontent.com/74603013/135380427-69d8d69c-496a-4000-a526-563269a34585.png)

* Using the same login details as I registered with, I successfully signed in

![sign-in-success](https://user-images.githubusercontent.com/74603013/135380707-351e4f72-d46a-4dab-88db-f6d56477e1a1.png)

* I then went to my profile to confirm that it was empty

![empty-profile](https://user-images.githubusercontent.com/74603013/135380935-a478ddf9-da2f-4d9c-ab92-b9310a8dd708.png)

* I then tried to resubmit the sign up form with the same details to make sure that I was in the database and that it wouldn't allow another user to register with the same details or for someone with an account to re-register.

![already-exists-error](https://user-images.githubusercontent.com/74603013/135377536-ad25c20d-895d-4514-9d24-d3e21124ee00.png)


### **Testing checkout form**
* Whilst still logged into my account, I went to the bag then checkout page. I made sure that the page displayed as intended with the form and order summary displayed. I checked that the placeholder text was in the form fields, that the user had to submit the mandatory fields and in the specified format and that the country fields menu worked. I also checked that the 'Keep Shopping' button worked as expected.
* I then completed the checkout form with the correct, valid details and Stripe test payment card details. I confirmed that I could tick the box to save details to my profile, which I selected. I also checked the warning message next to checkout confirms to the user that they are about to submit a payment and that it was for the correct value as in my bag.

![checkout](https://user-images.githubusercontent.com/74603013/135382450-268ce603-d3c1-459f-9ab3-99c75dda966b.png)

* I then submitted the form using the 'Secure Checkout' button and confirmed that I could see the overlay with the circular spinner as visual feedback to confirm the form was being submitted and that the overlay covered the page so that I couldn't re-submit or trying editing the form.
* I confirmed that I was taken to the checkout success page where I could see an order summary and the toast-success to confirm my order had been placed.

![order-success-summary](https://user-images.githubusercontent.com/74603013/135382876-d1027383-db97-4034-ba9c-d297a813c112.png)

* I confirmed that I received an order confirmation email.

![inbox-order-confirm](https://user-images.githubusercontent.com/74603013/135383071-c8f2ae80-4f7b-4919-a2df-e06765776d71.png)

* Confirmed the email was populated with the information I had put into the checkout form.

![Screenshot 2021-09-30 at 04-38-40 Webmail Afan Forest Adventures Confirmation for Order Number 12FC9957F3A541A7AC4CCFAF6BDF](https://user-images.githubusercontent.com/74603013/135383238-1d69b6ea-bdd5-4185-86d9-295dbd377ca3.png)

* I then went to my profile and confirmed that it showed my order history and that it had populated my details in the profile form from the checkout form.

![populated-profile](https://user-images.githubusercontent.com/74603013/135383455-3d14719d-9ec0-4ccc-a872-8511691c44ec.png)


### **Testing update profile info form**
* I edited the phone number and country in my profile and clicked the 'Update Information' button. I then confirmed that I was still in my own account that was showing the same order history but now correctly showed my updated details.

![update-profile](https://user-images.githubusercontent.com/74603013/135383951-f1828544-a50d-41b8-822e-4bb16e4a5c11.png)

### **Testing logout**
* I clicked the logout button from the dorpdown menu from the 'My Account' navbar tab. I confirmed that I got the screen to confirm that I wanted to sign out. 

![Screenshot 2021-09-30 at 07-05-46 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135396828-ff3e23b3-992e-42da-acec-1d6031299267.png)

* I clicked 'Sign Out' to confirm and made sure that I saw the toast success message to confirm successful sign out and that I was returned to the homepage.

![Screenshot 2021-09-30 at 07-10-14 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135396992-333ab1ba-5092-41f7-836b-72cb55c4d43c.png)


### **Testing signin**
* I entered a false username and password to ensure that it wouldn't let me log in and confirmed that I got an error message that gave a bit extra security by saying "username and/or password incorrect".

![Screenshot 2021-09-30 at 07-12-16 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135397230-c50c1ae1-1a94-4d36-9b83-40de5f8c5f25.png)

* I then entered the correct username and password to prove that I could successfully log in.

### **Testing superuser project management**
* I logged into my superuser account. I then confirmed that 'Project Management' was an option in the dropdown menu of the 'My Account' navbar.

![account-dropdown](https://user-images.githubusercontent.com/74603013/135407423-419c345d-6f8e-4cdd-b538-33afb7a266e8.png)

* I then selected 'Product Management' and confirmed that I was taken to the 'Add a product' form.

![Screenshot 2021-09-30 at 08-24-34 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135407135-e0524ab6-0b24-4a06-ae81-e9c7644a29c9.png)

* I then completed the form fields, ensuring all the category options were available in the dropdwon selection menu and that the form wouldn't allow me to submit without the required fields being completed. I then completed the form with valid information.

![Screenshot 2021-09-30 at 08-40-24 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135408957-ac69a9ef-2995-44e6-b389-02d4d0813720.png)

* I clicked the 'Add product' button. I then confirmed that I had the toast success message to confirm the product was successfully added and that I was taken to the product details page for the kayak product I had just added. I also ensured that as a superuser, I had the option to edit or delete the product.

![Screenshot 2021-09-30 at 08-41-12 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135409126-501fedc7-0722-4a97-a7da-42a2a5061ce1.png)

* I confirmed that I had the option to edit or delete on all products.

![Screenshot 2021-09-30 at 08-46-13 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135409859-5307d81f-8416-4972-a6c7-86de483a8263.png)

* I confirmed that I also had the option to edit or delete blogs

![Screenshot 2021-09-30 at 08-48-20 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135410206-75937a49-f61c-4a0c-9b31-902907976cce.png)

* I confirmed that I also had the option to edit or delete gallery images

![Screenshot 2021-09-30 at 08-49-53 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135410617-3fbc142e-4c62-45b1-a66d-fc33c87e84ef.png)

* I confirmed the 'Edit product' form was working by clikcing edit on the squirrel image and changing the name to hedgehog.

![Screenshot 2021-09-30 at 08-52-47 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135410881-24983328-4914-4ac0-9062-6f6748a93ff2.png)

* On clicking 'Update gallery', I confirmed that I had the toast success to confirm the edit had taken effect and I was returned to the image details for the image I had just editted.

![Screenshot 2021-09-30 at 08-54-47 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135411154-4c287cda-7e4a-4e3c-b98a-aebbdba75fe8.png)

* I then re-edited this image to return the name to squirrel, and confirmed that I got the toast alert message to confirm that I was editing the image.

![Screenshot 2021-09-30 at 08-56-21 Afan Forest Adventures](https://user-images.githubusercontent.com/74603013/135411429-b5e82636-7f60-4ff1-9071-376b118b1cc7.png)

* I then confirmed that the image name had correctly returned to squirrel.
* I then did the same test for editing a blog.





### **Testing blogs and gallery (not superuser)**
* I clicked on the blog icon in the navbar and ensured that I was taken to the blogs page and could view the blogs.

![blogs](https://user-images.githubusercontent.com/74603013/135373954-4a5c6130-35be-434b-a001-b3f8f8c97224.png)

* I then clicked on a blog to confirm that I was taken to the corresponding blog details page to read the blog contents.

![blog-detail](https://user-images.githubusercontent.com/74603013/135374157-02a3b7e7-89af-4d69-91e3-e4963817da61.png)

* I then repeated this process but for the gallery navbar icon checking I went to the gallery page 

![gallery](https://user-images.githubusercontent.com/74603013/135375258-d78c45a9-ec36-4849-8bfd-c98431bc4499.png)

* I then clicked on an image to make sure I could view more detail about it.

![image](https://user-images.githubusercontent.com/74603013/135375416-3a237557-cb48-47ac-b001-176a63fb12c1.png)










## **Problems Resolved During Manual Testing**
* Having run the “loaddata” commands and “runserver”, the image for “emergency outdoor first aid” and “bike maintenance” weren’t showing on the website. I found that both of these errors were due to having accidentally used different names in the products.json file and the corresponding image in the media file. I found that I had put “first-aid.jpg” and “mtb-maintenance.jpg” as my images in products.json but had called them “first_aid.jpg” and “bike-maintenance.jpg” in the media file. I changed the names to match and re-ran the “loaddata products” command to fix these errors.
* The pricing for the products and shopping bag was displaying in USD currency. This was because I had followed the Code Institute Boutique Ado tutorial to write my code and they had used $ currency. However, as my project was aimed at British users, I changed the currency to display in GBP £. I later foubnd the same error in my toast_success message when a user added something to their basket that was under a grand total of £50, as a prompt to get them to spend more. I updated the toast text to correct this.
* The blog page title on the Blogs page read ‘Products’ instead of ‘Blogs’ from where I had copied the products template to create the blog.html template. I fixed this by correcting the h2 title in blog.html.
* On clicking the gallery navbar icon, the gallery page failed to load giving the following error:
![gallery-error-message](https://user-images.githubusercontent.com/74603013/135091799-bebfa10b-23a1-467d-ab8e-cdeba0bbc6fe.png)
I used the error message to find the problem.

![incorrect-gallery-view-code](https://user-images.githubusercontent.com/74603013/135092465-8162831b-97bf-40bf-830f-1099012060f0.png)

I then corrected my code by adding the necessary 's' to 'gallery' in the function and context.

![correct-gallery-view-code](https://user-images.githubusercontent.com/74603013/135092841-30ee1444-319f-4b27-b161-7e639cd95e4c.png)

This corrected that error and allowed my to view the Gallery page, however there was another error in that the gallery images weren't showing.

![gallery-no-images](https://user-images.githubusercontent.com/74603013/135093063-f61c1f81-5393-4840-b13c-b4ff616fe836.png)

Again, I inspected the code to find the error.

![gallery-faulty-code](https://user-images.githubusercontent.com/74603013/135093191-562204b5-94fa-4c2b-a3d8-1533d97cf15c.png)

This time the error was having changed the 'edit' and 'delete' instead of the 'blog' parts of the two button links allowing a superuser to edit or delete gallery images. This was because I had re-used the code from the blog app and incorrectly changed the wrong part of the code.

![gallery-good-code](https://user-images.githubusercontent.com/74603013/135093880-5788e2a9-37a0-4ea2-98e7-8ee939191c6e.png)

This fixed the error and the Gallery page displayed correctly.
* The 'Book your adventure here' button on the home page didn't work. I found that I had not attached a url to this button. I added the all products page url and this fixed the problem.
* When I added a footer to the website, it had a very large top padding. I found the problem to be that I had used the same class name in my footer as for my block content which had a top-padding of 200px. I resolved this error by changing the class name of the footer to apply different css styling and reduce the footer height for a better appearance. I also added the mt-auto Bootstrap flexbox class to fix the footer to the bottom of the page.
* The website was designed with a free next-day delivery bonus if the user spent £50 and added a percentage delivery charge if the grand total of the shopping bag was under this value. I kept this functionality in place as detailed in my README under 'Additional Features Implemented' but set the delivery cost 0 and updated both the toast-success message and shopping bag message to the new free coffee offer and redeem instructions.
* Whilst not a true problem, I felt the home page image didn't conjure up the feel I waqnted the website to create as it showed a misty photo creating an almost sad feel. So I changed the hero image to fit better with the happy, adventurous image I wanted it to promote and that would better appeal to the website users. This did require, redownloading the media file from my GitHub repo and reuploading the images to the media file in the AWS S3 bucket.
* When manually testing the footer icons, the email icon and email address were not clickable as I had intended. I found that I had failed to put the closing href anchor tage after the icon and paragraph containing the email address. Once I correctly positioned the closing tag, this email icon and email address worked as expected by opening the website for Microsoft Outlook email in a new tab.
* On a mobile device som of the features weren't displaying nicely so I set media queries to overcome these issues. Using a screen size of 320px wide, I added media queries to sort the following problems:
    * Reduce size of main callout. This initially didn't change anything as I had set the earlier css for this class as !important, so I removed that to allow the media query changes to take effect.
    * Reduce padding of nav links.
    * Reduce size of navbar font awesome icons.
    * Reduce size and padding of toggler.
    * Reduce padding on product, blog, gallery detail buttons.
    * Reduce size and padding of shopping bag buttons.
    * Set qty increment to ignore media query changes.
* I changed the col-width and css styling for the main callout and 'book your adventure here' button as having the two alongside each other looked bad on smaller screens. I also changed the overlay so that it was just behind the main 'The outdoors awaits...' text and not behind the whole div with button so that it looked smarter and cleaner on the screen. I left the large overlay on the second callout as I didn't think this looked odd. In changing the col widths the callout was much more responsive for mobile devices.


## **Problems Resolved During Deployment**
* A major problem I encountered was with deploying to Heroku. I could run the project locally through Gitpod and that worked fine but I was getting build error when trying to deploy to Heroku so my project wouldn't build and wouldn't deploy. I spent a day trying to resolve my error by rechecking procfile, Afan settings, checking views, models and config variables. I then saught help from the Code Institute Tutor Support Team. The build log detailed the error.
![build-error-message](https://user-images.githubusercontent.com/74603013/135090269-ddb99065-207e-41c6-ae52-59eb783d8c1e.png)
The error isn't very clear and researching the error didn't find any solutions. I had also checked the Code Institute Slack channel but couldn't find a solution there. Three tutors from Code Institute helped to check my code and confirmed that my code seemed to be correct and nothing was missing. This made us think it was a problem with the AWS, I re-entered the ACCESS_KEY_ID and SECRET_ACCESS_KEY but still the error remained. I then decided to recreate my AWS bucket, policy, user and group. I followed the Code Institute Boutique Ado tutorials very closely! This gave me a new ACCESS_KEY_ID and SECRET_ACCESS_KEY to access the new bucket. I replaced the old config variables in heroku with these new ones and did a rebuild. This time the build was successful and my app deployed. 
![build-success](https://user-images.githubusercontent.com/74603013/135091176-65cb88e5-a227-4d9f-9211-50a1a96a9260.png)
* Having deployed my project to Heroku, when testing the features I found that both the blog and gallery failed to display and instead showed the folloing error:

![heroku-blog-error](https://user-images.githubusercontent.com/74603013/135150668-57073777-1fba-4224-b529-40fbfabc8460.png)

but the gallery and blog pages were fine in the localhost run from Gitpod:

![gitpod-blogs-success](https://user-images.githubusercontent.com/74603013/135150841-0c5980ac-f4ff-4e17-b132-4b39cacc49fb.png)

As the project worked locally, this helped me to identify the source of the problem. I had forgotten to do the make migrations to Heroku Postgress. I made these migrations and the loaddata commands for the categories, products, blog and fixtures and the deployed app worked correctly.

