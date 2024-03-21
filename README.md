# Nags With Notions2.0

![Responsiveness](/static/images/readme-responsiveness-image.png)

  - [OVERVIEW](#overview)
  - [UX/UI](#uxui)
    - [STRATEGY](#strategy)
      - [Goals<br>](#goals)
      - [User Stories<br>](#user-stories)
    - [SCOPE<br>](#scope)
    - [STRUCTURE<br>](#structure)
    - [FLOWCHARTS<br>](#flowcharts)
    - [SURFACE/DESIGN<br>](#surfacedesign)
    - [EXISTING FEATURES<br>](#existing-features)
    - [FUTURE FEATURES<br>](#future-features)
  - [BUGS OR ERRORS](#bugs-or-errors)
  - [TESTING](#testing)
  - [MODULES IMPORTED](#modules-imported)
  - [DEPLOYMENT](#deployment)
    - [CREATING THE WEBSITE](#creating-the-website)
    - [DEPLOYING ON HEROKU](#deploying-on-heroku)
    - [FORK THE REPOSITORY](#fork-the-repository)
    - [CLONE THE REPOSITORY](#clone-the-repository)
  - [CREDITS](#credits)
  - [TOOLS](#tools)
  - [ACKNOWLEDGEMENTS](#acknowledgements)


## OVERVIEW 🚠
This site was created to allow users book a portable pizza service. Users should be able to access the site and book the service for their event. Users can also view other events. The site mainly uses Django, Python, SASS, CSS, Javascript and python. CRUD functionality is found on both events and bookings. Only superusers can configure events. However, registered users can view their bookings and update/delete them as required.

## UX/UI

### STRATEGY

#### Goals 🥅<br>

The UX was explored using a customer journey map. The site then acted successfully on the insights taken from the map. The customer journey map detailed the journey and expected emotions of 3 standard users of the website. Goals and expectations are taken into account. This gave a general view of how to proceed with the project. User stories were then used to break these needs into tasks. The UI involved good use of navigation through anchor links and appropriate sizing for different devices. A toggle dropdown menu was used for smaller screens.

[Customer Journey Map](/static/pdfs/nags-with-notions-customer-jouryney-map.pdf)

#### User Stories 📖<br>

**The number references here proceeded by the hash key refer to the issue number in the github projects.

* As a customer interested in hiring a pizzeria horsebox service, I can request to book the horsebox online so that I can use it for a personal event #3
* As a website user I can see what events have occurred or will be occurring, so I can keep informed.
* As a user I want to be able to see my current bookings displayed on the site.
* As a user I want to only see my own bookings, so my booking information is kept private #171 #154
* As a user I want to quickly see a 'book now' button which brings me to the booking form #163
* As a user I want to be able to create bookings on the site #157
* As a user I want to be able to update bookings on the site #159
* As a user I want to be able to delete bookings on the site #156
* As a user I want to be able to see the prices of all the food items #131 #45
* As a user I want to see the name of each food item underneath its image #44
* As a user I want to be able to see if I'm logged in #99
* As a user I want to access my information once logged in #100
* As a user I want to be able to register an account using a username and password
* As a user I want feedback when my form completion has been successful #93 #94
* As a user I want a dropdown toggle menu for mobile screen sizes #52
* As a user I want a responsive header with interactive links for ease of site navigation #51 #4
* As a user I want to be able to access social media sites from the footer #5


* As an admin I want to be able to upload images related to events #170 #168
* As admin I want to be able to create events but users cannot create events #168
* As admin I want to be able to update events so new information can be added or subtracted #167
* As admin I want to be able to delete events #167
* As admin I want to have my passwords safe #113


### SCOPE 🔭<br>



### STRUCTURE☠<br>

#### Database diagrams

* [Database diagram #1](/static/pdfs/drawSQL-version1.png)

The comments model was removed as it wasn't seen as essential, and other work took priority, such as testing.
* [Database diagram #2](/static/pdfs/drawSQL-version2.png)


### FLOWCHARTS 📈<br>

Reasoning to flowchart: A flowchart was created to present the entire user story visually. The user is initially presented
with a welcoming landing page. The user is informed they can choose to book the pizza box for
personal use or see when other events are on that they could attend and try some pizza. The pizza
menu is displayed. If the user wishes to book they are shown the available dates. To book the user
needs to login. If not already registered the user must sign up. Once the user is logged in they
can select their preferred dates. They then receive a confirmation email regarding their booking. The dates available, personal information and password data is then updated.

[Full Site Flowchart](/static/pdfs/nags-with-notions-flowchart-sprint1.pdf)

#### Sprints

[Sprint 1](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/19) * This will be closed but closed issues can be viewed.

Sprint 1 was overdue by one month as the django lms learning material took much longer than expected. The real project has started now and I expect to work through the issues at a quicker pace. Upon reflection, and advice from slack meeting 110124 I should implement story points to get a better grasp on what can be achieved between sprints and what to prioritise. I will also pivot towards putting crud functionality on bookings rather than comments

* Sprint 2

[Sprint 2](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/20) * This will be closed but closed issues can be viewed.


Sprint 2 saw the completion of 50% of its tasks. Story points were introduced to get a better grasp on the workload, and this may allow one to gain a better understanding of what can be realistically achieved in Sprint 3. Considerable time was put into automatic testing, which is not a requirement for the pass criteria; so in sprint 3 effort will be directed into other areas. During Sprint 2 much of the functional objectives were achieved. In Sprint 3 I hope to divest more energy into testing. 46 open issues were passed forward from Sprint 2 to Sprint 3. 159 story points were completed in Sprint 2. 147 story points have been passed for to Sprint 3, which makes this workload realistically achievable by the end of Sprint 3.

* [Sprint 3](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/21) * This will be closed but closed issues can be viewed.

The previous sprint was supposed to prioritise testing but during testing I found several bugs. One bug took several days to fix. This involved ensuring that the registered user could only see their own bookings in the view bookings tab. Connecting the user as a foreign key to my booking model and using the booking id as an argument to track whether the booking belonged to a specific user or not was quite challenging to figure out. Thus during this phase only 6 tasks were completed. For the next two weeks I intend to double down on testing: starting with ensuring all the booking functionality is correct and documenting this in the readme. Still several weeks until the Mar 22 deadline so things appear to be on track.


[Sprint 4](https://github.com/JWalshe86/Nags-With-Notions2.0/milestones?state=closed) * This will be closed but closed issues can be viewed.

The 8 days overdue for sprint 4 was a result of extra work in my internship. However, a lot of manual testing was completed which was quite tedious. This testing also highlighted many errors which took time to fix. The main focus now is to complete the testing and the user stories.

[Sprint 5](https://github.com/JWalshe86/Nags-With-Notions2.0/issues)

The final sprint involved doubling down on testing. Python testing was completed. The readme was updated. My site was also tested by friends and work colleagues.

Everything onn Kanban board was completed.

[Kanban Board](/static/images/KanbanBoard.png)

### SURFACE/DESIGN<br>

I chose the 'square' color harmony using Adobe's color wheel. The base color was the color associated with Nags with Notions Logo. However I swapped out #C4C9F5 for aliceblue as I felt #C4C9F5 was a bit too harsh.

![Color Palette](/static/images/colorpalette.png)

#### Wireframes

[Initial Landing Page Wireframe](/static/pdfs/Nags-With-Notions-Wireframe.pdf)


Reasoning for Wireframe structure: As a user, I want to be able to see when the Pizza Horsebox is available for private hire. As the owner, I want customers to know they can hire the horse box and when it's available. Also, I want the user of the website to know that Nags with Notions also sells pizzas at events and when these events are on. The wireframe shows websites snippets where such features have been executed successfully. Having shown this wireframe to Nags With Notions they are happy to proceed.

## FEATURES

### EXISTING FEATURES


### FUTURE FEATURES 🚀

## Technologies used 🧑‍💻


- Django was used as the framework for both the backend and frontend of the website.
- HTML & CSS for the templates and styling
- Snapedit to blur background in hero image
- Imagor to give pink hue & size images https://github.com/cshum/imagor
- drawSQL to create database diagrams
- tinypng.com to compress images
- Bootstrap
- Sass
- Jquery

### Django Packages

- [Requirements.txt1](./static/images/requirements.txt1.png)
- [Requirements.txt2](./static/images/requirements.txt2.png)

Many of the packages here are dependencies of core packages. The main packages used were:
- Django as the framework
- django-allauth for user permissions
- django-crispy forms to make forms look and perform better
- factory-boy to create fake data for automated tests
- pillow to manage images
- python-dotenv to create a virtual python environment and keep dependencies local
- waitress as a subtitute for gunicorn as I was using windows
- whitenoise for static support when deploying to a server




### Infastructural Technologies

- PosterSQL - used as the database
- Heroku - where site was deployed

## Languages used

- Python, Javascript 🐍

## BUGS OR ERRORS 🐛 😵// Issues which take me more than 2 hours to solve

1. Getting the site deployed to Heroku from windows was very challenging. It probably took me 3 days and I almost gave up. Gunicorn doesn't
work well with Windows. I was also using vscode which meant Code Institue support was compromised as they used codeanywhere. Eventually I came across waitress server. Using a combination of both stackoverflow and youtube I figured out how to get the procfile correct. Adding 'web: waitress-serve --port=$PORT nags_with_notions.wsgi:application' worked. The '--port=$PORT" was the biggest factor in getting the site deployed. I found this on an obscure youtube video. I was very grateful for the person who created that content.

2. I was unable to get users content to stay specific to their logins. For example, if one user added a booking, this new booking could be seen by all users. The solution involved changing all my functions in views, to classes. I was then able to import django views, which did alot of the work behind then scenes and enabled me to compartmentalize user data. It also allowed me to import success messages.

3. Getting images to upload when creating an event was challenging. It involved using whitenoise. It also involved figuring out how to get the path to correct correctly. A default path from the root had to be configured in settings.py. This took alot of trial and error but eventually it worked.

4. During lighthouse testing I couldn't get the hero image to load under 5 seconds. However, in reality the image appears to load straight away. That said after alot of trial and error I was able to get the image to render in under a second on lighthouse but then it would increase again. I think it may be due to internet connection. I still haven't figured this out fully.

## Testing

### Feature Testing

*If in Markdown: PDF's open in github https://github.com/JWalshe86/Nags-With-Notions2.0?tab=readme-ov-file

[Manual Testing](/static/pdfs/testing/manual-testing.pdf)

### Manual Tests to assess javascript functionality

All tests on functionality were passed.
[Javascript tests on functionality](/static/pdfs/testing/Manual%20Test%20to%20Assess%20Javascript%20Functionality.pdf)

### Model Testing

Use of pytest-cov to see where tests may be required. I prioritised testing my custom code, as Django would have tested it's own code extensively. I installed factory-boy to insert fake data into the database. [First successful use of Pytest](/static/pdfs/testing/first-successful-use-of-pytest.docx). Due to the complexity of this testing, and time constraints I moved onto manual tests.

#### User Stories Testing<br>

* As a customer interested in hiring a pizzeria horsebox service, I can request to book the horsebox online so that I can use it for a personal event #3
Achieved. See feature testing for more detail.
[New booking created](/static/images/userstorytesting/newbookingcreated.png)

* As a website user I can see what events have occurred or will be occurring, so I can keep informed.
Achieved. See feature testing for more detail.
[Events list](/static/images/userstorytesting/canseeevents.png)

* As a user I want to be able to see my current bookings displayed on the site.
Achieved. See feature testing for more detail.
[Bookings list](/static/images/userstorytesting/canseebookings.png)

* As a user I want to only see my own bookings, so my booking information is kept private #171 #154
Achieved. See feature testing for more detail.
[See own bookings](/static/images/userstorytesting/canseebookings.png)

* As a user I want to quickly see a 'book now' button which brings me to the booking form #163
Achieved. See feature testing for more detail.
[Book Now 1](/static/images/userstorytesting/booknow1.png)
[Book Now 2](/static/images/userstorytesting/booknow2.png)

* As a user I want to be able to create bookings on the site #157
Achieved. See feature testing for more detail.
[Create booking](/static/images/userstorytesting/newbookingcreated.png)

* As a user I want to be able to update bookings on the site #159
Achieved. See feature testing for more detail.
[Update booking 1](/static/images/userstorytesting/update1.png)
[Update booking 2](/static/images/userstorytesting/update2.png)
[Update booking 3](/static/images/userstorytesting/update3.png)

* As a user I want to be able to delete bookings on the site #156
Achieved. See feature testing for more detail.
[Delete booking 1](/static/images/userstorytesting/delete1.png)
[Delete booking 2](/static/images/userstorytesting/delete2.png)
[Delete booking 3](/static/images/userstorytesting/delete3.png)

* As a user I want to be able to see the prices of all the food items #131 #45
Client asked for prices to be removed and ratings used instead.
[See ratings](/static/images/userstorytesting/pizzaratings.png)

* As a user I want to see the name of each food item underneath its image #44
Achieved. See feature testing for more detail.
[Item description](/static/images/userstorytesting/pizzaratings.png)

* As a user I want to be able to see if I'm logged in #99
Achieved username presents in header.
[Logged in](/static/images/userstorytesting/userloggedin.png)


* As a user I want to access my information once logged in #100
Achieved. Restricted info for users not logged in.
[Limited info](/static/images/userstorytesting/‫limitedinfonotloggedin.png)

* As a user I want to be able to register an account using a username and password
Achieved. See feature testing for more detail.
[Register 1](/static/images/userstorytesting/Register1.png)
[Register 2](/static/images/userstorytesting/Register2.png)
[Register 3](/static/images/userstorytesting/Register3.png)

* As a user I want feedback when my form completion has been successful #93 #94
Achieved. See feature testing for more detail.
[success message](/static/images/userstorytesting/newbookingcreated.png)

* As a user I want a dropdown toggle menu for mobile screen sizes #52
Achieved. See feature testing for more detail.
[Toggle Dropdown](/static/images/userstorytesting/toggledropdown.png)

* As a user I want a responsive header with interactive links for ease of site navigation #51 #4
Achieved. See feature testing for more detail.

* As a user I want to be able to access social media sites from the footer #5
Achieved. See feature testing for more detail.


## MODULES IMPORTED 👽


## DEPLOYMENT 🚀

### CREATING THE WEBSITE

[Mentor Meeting 1 Feedback](/static/pdfs/mentor-meeting1-291123-notes.txt)

### DEPLOYING ON HEROKU

- Install Gspread using pip install Gspread in the terminal
- Ensure the requirement.txt file in the virtual working environment contains Gspread
- Enter [Heroku](https://id.heroku.com/login) and click 'Create new App'.
- Store sensitive data contained in the creds.json file in the config/Environment Vars
- Add both Python and node.js buildpacksClick Deploy and then connect to GitHub
- Search and connect to the GitHub repository name
- Click deploy branch
- When the project has been successfully deployed, click view.

### FORK THE REPOSITORY 🍴

If you would like to contribute to the project. You can:
1. Open the pizza ordering system repository on my account and
press the fork button on the top right of the screen.
2. Click create a new fork.
3. Navigate to your fork of the original repository.
4. Copy the URL for the repository.
5. Type git clone into your terminal and paste the repository.
6. You can then create a pull request which I will review.

### CLONE THE REPOSITORY ©

You can clone the repository to use locally by following these steps:
1. Navigate to the GitHub Repository you want to clone
2. Click on the code drop-down button
3. Click on HTTPS
4. Copy the repository link to the clipboard
5. Open your IDE of choice (git must be installed for the next steps)
6. Type git clone copied-git-URL into the IDE terminal

The project will now be cloned locally for you to use.


## CREDITS 💛

* [Learn SASS and SCSS](https://www.udemy.com/course/learn-sass-and-scss/?couponCode=ST14MT32124)
* Code adapted from [SA7MAN](https://youtu.be/KRENd1sv3tE?si=wOYRfPz9qjgKc5w-) for restaurant design using bootstrap
* Websites [littlehotelier.com](littlehotelier.com), [opentable.ie](opentable.ie) and [brolmo](brolmo.com) were used as inspiration
for the confirmation email, logging in to book a table and showing available dates in the wireframe.
* [flyUX-pp4](https://github.com/CarlMurray/flyUX-pp4) for inspiration on readme.
* [The Irish HORSEBOX bar hire](https://theirishhorseboxbarhire.com/) was used for inspiration.
* [Django Python Environment Variables](https://youtu.be/0nFizjeNJl4?si=2nMinofCWIV-y_A7)
* [Display data from database on browser - Codemy](https://youtu.be/H3joYTIRqKk?si=qAek5PaXluQp_lLa)
* [Upload images with django - Codemy](https://youtu.be/bNXmU-941iY?si=3EYbBp2vkRvsg1hC)
* [Style Django forms with Bootstrap - Codemy](https://youtu.be/6-XXvUENY_8?si=7Q3HWX7ivY8DhTAX)
* [Django Permissions - Very Academy](https://youtu.be/AR5hjQ8nla0?si=L6d7-AdgmsIMR8rg)
* [Dennis Ivy CRUD with Model Forms](https://youtu.be/EX6Tt-ZW0so?si=j9mncTFJLuVmly83)
* [How to build a javascript password strength meter with regex - Web Dev Simplified](https://youtu.be/7-1VZ2wF8pw?si=c7_yong1oqQD4naz)
* [Style login page bootstrap - Codemy](https://youtu.be/0Z_3APyKwQ4?si=HcRplqpnrJF9BBps)
* [User Login, Logout and Flash Messages](https://youtu.be/naIgdcxUT_w?si=7doNH4wgCOqfm42N)
* [Writing your first Django test using pytest-django Pybites](https://youtu.be/L5jWFU2sVXQ?si=7jORatCMS2P8wz1o)
* [Make your Django Project Live on internet Fix Error While Deploying to Heroku Servers](https://youtu.be/lKijcNqLL7A?si=ezxh8rGUcP3PQ9pB)
* [Bootstrap alert](https://youtu.be/UTZjhCH80Zg?si=w3inHIFfo3BFuTs5)
* [How to set up tests and testing urls](https://youtu.be/0MrgsYswT1c?si=z0kcjuW3C6eQnEa6)

## TOOLS 🧰

* Icons from [remixicon.com](https://remixicon.com/)
* [Figma](www.figma.com) was used to create the wireframes & user story map
*[tinypng](tinypng.com) was used to compress images


## ACKNOWLEDGEMENTS 👏

* I'd like to thank Code Institute Tutors Iris and Marco who supported and listend to myself, Abdul and Aongus every Wednesday.
* To my mentor who gave great advice on the project
* To everyone on youtube and stackoverflow who created content
* To my friends, family and colleagues at 2Toucons (Chandeep) for reviewing the site
* To Nags with Notions for giving me images and ideas and reviewing the site
* Code Institute