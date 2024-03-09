# Nags With Notions2.0
# Nags With Notions2.0
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


## UX/UI

### STRATEGY

#### Goals 🥅<br> 

[Customer Journey Map](/static/pdfs/nags-with-notions-customer-jouryney-map.pdf)

#### User Stories 📖<br>

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

### SCOPE 🔭<br>



### STRUCTURE☠<br> 

#### Database diagrams

* [Database diagram #1](/static/pdfs/drawSQL-version1.png)
* [Database diagram #2](/static/pdfs/drawSQL-version2.png)


### FLOWCHARTS 📈<br>

Reasoning to flowchart: A flowchart was created to present the entire user story visually. The user is initially presented
with a welcoming landing page. The user is informed they can choose to book the pizza box for 
personal use or see when other events are on that they could attend and try some pizza. The pizza
menu is displayed. If the user wishes to book they are shown the available dates. To book the user
needs to login. If not already registered the user must sign up. Once the user is logged in they 
can select their preferred dates. They then receive a confirmation email regarding their booking. The dates available, personal information and password data is then updated. 

[Full Site Flowchart Sprint1](/static/pdfs/nags-with-notions-flowchart-sprint1.pdf)

#### Sprints

* Sprint 1
[Sprint 1](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/19)

Sprint 1 was overdue by one month as the django lms learning material took much longer than expected. The real project has started now and I expect to work through the issues at a quicker pace. Upon reflection, and advice from slack meeting 110124 I should implement story points to get a better grasp on what can be achieved between sprints and what to prioritise. I will also pivot towards putting crud functionality on bookings rather than comments

* Sprint 2

[Sprint 2](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/20)

Sprint 2 saw the completion of 50% of its tasks. Story points were introduced to get a better grasp on the workload, and this may allow one to gain a better understanding of what can be realistically achieved in Sprint 3. Considerable time was put into automatic testing, which is not a requirement for the pass criteria; so in sprint 3 effort will be directed into other areas. During Sprint 2 much of the functional objectives were achieved. In Sprint 3 I hope to divest more energy into testing. 46 open issues were passed forward from Sprint 2 to Sprint 3. 159 story points were completed in Sprint 2. 147 story points have been passed for to Sprint 3, which makes this workload realistically achievable by the end of Sprint 3.

* Sprint 3 

The last sprint was supposed to prioritise testing but during testing I found several bugs. One bug took several days to fix. This involved ensuring that the registered user could only see their own bookings in the view bookings tab. Connecting the user as a foreign key to my booking model and using the booking id as an argument to track whether the booking belonged to a specific user or not was quite challenging to figure out. Thus during this phase only 6 tasks were completed. For the next two weeks I intend to double down on testing: starting with ensuring all the booking functionality is correct and documenting this in the readme. Still several weeks until the Mar 22 deadline so things appear to be on track.

[Sprint 3](https://github.com/JWalshe86/Nags-With-Notions2.0/milestone/21)

* Sprint 4

The 8 days overdue for sprint 4 was a result of extra work in my internship. However, a lot of manual testing was completed which was quite tedious. This testing also highlighted many errors which took time to fix. The main focus now is to complete the testing and the user stories. 

[Sprint 4](https://github.com/JWalshe86/Nags-With-Notions2.0/milestones?state=closed)

### SURFACE/DESIGN<br>

#### Wireframes

[Initial Landing Page Wireframe](/assets/wireframe/landing-page-wireframe.fig)


[Full Site Wireframe Sprint1](/assets/pdfs/nags-with-notions-wireframe-sprint1.pdf)

Reasoning for Wireframe structure: As a user, I want to be able to see when the Pizza Horsebox is available for private hire. As the owner, I want customers to know they can hire the horse box and when it's available. Also, I want the user of the website to know that Nags with Notions also sells pizzas at events and when these events are on. The wireframe shows websites snippets where such features have been executed successfully. Having shown this wireframe to Nags With Notions they are happy to proceed. 

## FEATURES

### EXISTING FEATURES


### FUTURE FEATURES 🚀

## Technologies used 🧑‍💻

- Snapedit to blur background in hero image 
- Imagor to give pink hue & size images https://github.com/cshum/imagor
- drawSQL to create database diagrams
- tinypng.com to compress images

## Languages used

- Python 🐍

## BUGS OR ERRORS 🐛 😵// Issues which take me more than 2 hours to solve

## Testing

### Feature Testing



### Manual Tests to assess javascript functionality

All tests on functionality were passed. 
[Javascript tests on functionality](/static/pdfs/testing/Manual%20Test%20to%20Assess%20Javascript%20Functionality.pdf)

### Model Testing

Use of pytest-cov to see where tests may be required. I prioritised testing my custom code, as Django would have tested it's own code extensively. I installed factory-boy to insert fake data into the database. [First successful use of Pytest](/static/pdfs/testing/first-successful-use-of-pytest.docx)

### Booking Model tests



#### User Stories Testing<br>



* As a customer interested in hiring a pizzeria horsebox service, I can request to book the horsebox online so that I can use it for a personal event. User Story #3


## MODULES IMPORTED 👽
 

## DEPLOYMENT 🚀

### CREATING THE WEBSITE

[Mentor Meeting 1 Feedback](/assets/pdfs/mentor-meeting1-291123-notes.txt)
  
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

* Code adapted from [SA7MAN](https://youtu.be/KRENd1sv3tE?si=wOYRfPz9qjgKc5w-) for restaurant design using bootstrap
* Websites [littlehotelier.com](littlehotelier.com), [opentable.ie](opentable.ie) and [brolmo](brolmo.com) were used as inspiration
for the confirmation email, logging in to book a table and showing available dates in the wireframe.
* [The Irish HORSEBOX bar hire](https://theirishhorseboxbarhire.com/) was used for inspiration.
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
### Suggested links from Slack Meeting 291123
https://mf-pp4-kerry-surf-school.herokuapp.com/signuporlogin/
https://github.com/IuliiaKonovalova/start-with-django
[for testing](https://github.com/Abibubble/ms4-lead-shot-hazard)

https://www.youtube.com/watch?v=ByGJQzlzxQg
https://www.youtube.com/watch?v=cuEtnrL9-H0

https://www.youtube.com/@ColtSteeleCode
https://www.youtube.com/@KevinPowell

https://wesbos.com/ 

### Slack Meeting Suggestion 100124

- Follow Sprints #TODO
- Add user story points #TODO
- Change comments to reviews #TODO

## TOOLS 🧰

* Icons from [remixicon.com](https://remixicon.com/)
* [Figma](www.figma.com) was used to create the wireframes & user story map
*[tinypng](tinypng.com) was used to compress images


## ACKNOWLEDGEMENTS 👏

