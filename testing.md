
#### Potential user's perspective ####
* I am a potential customer, I want to know what activities are offered, so I can decide if I want to buy any.
    * From the home page click the 'Book your adventure now' button or the 'products' button to be taken to the all products page.
    * From the search bar by typing for the activity they want to know whther it is offered.
    * From the 'activities' tap in the secondary navbar and selecting one of the dropdown menu options to explore the activity options.
* I am a customer who will be visiting Afan Forest Adventures, I want to know what facilities are available, so I can plan my day/stay.
    * From the secondary navbar this user can see that Afan Forest Adventures offers a campsite and from the dropdown can see the other ioptions for caravan, glamping etc. They can also see the activities and courses to see the range of offerings.
    * This user could also check out the gallery from the 'gallery' button on the homepage or 'gallery' in navbar.
    * This user could also check out the social media or contact the centre via the details in the footer.
* I am a MTB instructor, I want to know what courses Afan Forest Adventures offer, so I can improve my qualifications.
    * From the search bar by typing in the name of the course they are interested in doing.
    * From the 'courses' tab on the navbar and selecting one of the categories depending on the qualification type or skills course they are after.
* I am visitor to Afan Forest Adventures, I want to know their contact details, so that I can ask them my questions.
    * From the 'Contact Us' section in the footer with options to contact via phone, email (linked to an email platform when clicked), or the social media channels of twitter, facebook and instagram (linked to an corresponding platform when clicked).

#### User's perspective ####
* I am a customer who has booked an activity, I want to view my order history, so I can see what I have booked.
    * This option is reserved for customers with an account: From the navbar select 'My Account', login to the account to see their order history.
    * Guest users wihtout an account are provided with an order confirmation and email confirmation with their order details.
* I am a customer, I want a quick and simple way of making my purchase.
    * From the product details page; add item to bag which causes a toast-success messsage to appear with a link to 'go to secure checkout' taking them to their shopping bag or by clicking the shopping bag navbar tab; checking bag contents and clicking 'secure checkout' button; completing the form and finally clicking 'confirm order'. 
* I am a customer who is booking a course that is paid by my employer, I want a copy of my order, so I can reclaim the cost of the course.
    * This option is reserved for customers with an account: From the navbar select 'My Account', login to the account to see their order history.
    * Guest users without an account are provided with an order confirmation and email confirmation with their order details.

#### Site owner's perspective ####
* I am the admin for Afan Forest Adventures, I want a simple method of managing products, so I can upload, edit and delete what we offer.
* I am the admin for Afan Forest Adventures, I want a simple method of managing the gallery, so  I can upload, edit and delete the images.
* I am the admin for Afan Forest Adventures, I want a simple method of managing the blog, so  I can upload, edit and delete the images.

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

### **Testing toast-success**
* I added an item to my basket to ensure the toast-success appeared to confirm to the user which item had been added, quantity, current bag cost and option to checkout. I chose an item that was under £50 to ensure the prompt to spend more for a free coffee was shown. This worked as planned.

![prompt-to-spend-more](https://user-images.githubusercontent.com/74603013/135245904-93f81cde-c8c6-466b-a272-5aa54c2b9224.png)


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



