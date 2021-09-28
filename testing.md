## **Problems Resolved During Testing**
* Having run the “loaddata” commands and “runserver”, the image for “emergency outdoor first aid” and “bike maintenance” weren’t showing on the website. I found that both of these errors were due to having accidentally used different names in the products.json file and the corresponding image in the media file. I found that I had put “first-aid.jpg” and “mtb-maintenance.jpg” as my images in products.json but had called them “first_aid.jpg” and “bike-maintenance.jpg” in the media file. I changed the names to match and re-ran the “loaddata products” command to fix these errors.
* The pricing for the products and shopping bag was displaying in USD currency. This was because I had followed the Code Institute Boutique Ado tutorial to write my code and they had used $ currency. However, as my project was aimed at British users, I changed the currency to display in GBP £. 
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
* A major problem I encountered was with deploying to Heroku. I could run the project locally through Gitpod and that worked fine but I was getting build error when trying to deploy to Heroku so my project wouldn't build and wouldn't deploy. I spent a day trying to resolve my error by rechecking procfile, Afan settings, checking views, models and config variables. I then saught help from the Code Institute Tutor Support Team. The build log detailed the error.
![build-error-message](https://user-images.githubusercontent.com/74603013/135090269-ddb99065-207e-41c6-ae52-59eb783d8c1e.png)
The error isn't very clear and researching the error didn't find any solutions. I had also checked the Code Institute Slack channel but couldn't find a solution there. Three tutors from Code Institute helped to check my code and confirmed that my code seemed to be correct and nothing was missing. This made us think it was a problem with the AWS, I re-entered the ACCESS_KEY_ID and SECRET_ACCESS_KEY but still the error remained. I then decided to recreate my AWS bucket, policy, user and group. I followed the Code Institute Boutique Ado tutorials very closely! This gave me a new ACCESS_KEY_ID and SECRET_ACCESS_KEY to access the new bucket. I replaced the old config variables in heroku with these new ones and did a rebuild. This time the build was successful and my app deployed. 
![build-success](https://user-images.githubusercontent.com/74603013/135091176-65cb88e5-a227-4d9f-9211-50a1a96a9260.png)
