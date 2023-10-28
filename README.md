# Kunstgalerie Wien

![Responsive screenshot](static/images/respon.png)

# The Main Idea

This project is based on a fictious art gallery in Vienna. It allows artists to sign up then post and sell their artwork.
Users sign up create a profile and post their work. I noticed on most gallery websites the gallery doesnt really offer more information on the artists/users previous works or backgrounds .They kind of act like a buffer between artists and art buyer, maybe that is done on prupose, but I wanted to update that model and bring it slighlty into 2023.
()
Required technologies:

- HTML, CSS, JavaScript, Python+Django
- Relational database

The live version url: https://s1-blog-4367ccd1d3ac.herokuapp.com/

# Table of Contents

- [UX / User Experience](#ux "UX")
  - [User Demographic](#user-demographic "User Demographic")
  - [User Goals](#user-goals "User goals")
  - [User Stories](#user-stories "User Stories")
    - [USER](#user "user")
  - [Project Idea](#project-idea "Project Idea")
  - [Site Navigation](#site-navigation "Site Navigation")
  - [Design Inception](#design-inception "Design Inception")
  - [Features](#features "Features")
  - [Existing Features](#existing-features "Existing Features")
    - [Sign In](#sign-in "Sign In")
    - [Home](#Home "Home")
    - [About](#about "About")
    - [Artists](#List-Of-Artists "List Of Artists")
    - [Register](#register "Register")
    - [Login](#login "Login")
    - [Logout](#logout "Logout")
    - [Profile](#profile-page "Profile Page")
    - [Default](#default-images "Default Images")
    - [Create Post](#create-post "Create post")
    - [Edit Post / Delete Post](#edit-post "Edit Post")
    - [Edit Profile / Delete Profile](#edit-profile "Edit Profile")
    - [Comment / Delete Comment](#comment "Comment")
  - [Future Features](#future-features "Future Features")
- [Languages used](#languages-used "Languages used")
  - [Frameworks and libraries and tools](#frameworks-and-libraries-and-tools "Frameworks and libraries and tools")
  - [Installed packages](#installed-packages "Installed packages")
- [Testing](#testing "Testing")
  - [Bugs during development](#bugs-during-development "Bugs during development")
  - [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
  - [Validator Testing](#validator-testing "Validator Testing")
- [Deployment](#deployment "deployment") -[Security notes](#security-notes "security notes")
- [Content](#content "Content")
- [Credits](#credits "Credits")

## UX

### User Demographic

Kunstgalerie Wien

The "Kunstgalerie Wien" is tailored for artists with a connection to Vienna who are seeking a platform to sell, display, and promote their artwork to a global audience while remaining true to Vienna's artistic heritage and culture.

1. Artists:

The local artists we cater to are all from Vienna one way or the other, and want to exhibit their artwork on an international stage while maintaining their roots to the imperial city.

2.  Art Enthusiasts:

Art Buyers and Enthusiasts:

We have two target audiences. Firstly individuals residing in Vienna who are avid art supporters and are enthusiastic about discovering and acquiring artwork created by local artists.

& secondly , Global Art Enthusiasts, people from across the globe who admire Vienna's artistic legacy and would like to add to their art collections contemporary art from Vienna's evolving scene.

### User Goals

The users gets to display thier artwork simply and easily among other like minded contemporary artists and potential buyers in and outside of Vienna.

### User Stories

The following user stories has been implemented in the project. The user storires are based centred around users want to sign up and post, comment and be apart of the gallery.

#### USER

As a **USER** I can **create a profile** so that **I can log in**

As a **USER** I can **upload a profile picture** so that **personalize it**

As a **USER** I can **change or delete my profile picture**

As a **USER** I can **write a short bio** so that **so that other users can read about me**

As a **USER** I can **upoload artwork** so that **my art can be viewed**

As a **USER** I can **can comment on other user posts** so that **so that I can express myself**

As a **USER** I can **delete my comment** so that **if I dont like it later I can remove it**

As a **USER** I can **like other users posts** so that **I encourage others**

As a **USER** I can **edit posts** so that **I can update them and change them if I feel like it**

### Project Goal

Demonstrate CRUD functionailty, database manipulation and an understanding of Django frameworks + HTLM , CSS, JavaScript and Python.

### Design Inception

Initially the project was going to be a runner-instragram like app. So I started the main design ideas with that in mind. The main intresest in a running ap would be to track your speed and distance and performance and so to do what I wanted would require more knowledge than I currently possess and the design was simply ugly. So in the end I opted for something eqaully close to my hear , art , more specifially painting and Vienna.

The idea which at the heart was supposed to be instagram in spirit is actually quite simple and based on modern art gallery sites found in New York city.

The crud fucntionality came pretty simply after I had settled on an idea.
![Runner app example](static/images/runner1.png/)
When I ditched the "Runner app " idea and settled on the art gallery idea everything clicked and I could see the design in my head exactly behinds the scenes.
![Gallery example 1](static/images/wien1.png/)

## Main Features

Kunstgalerie Wien main features:

### - [Login / Register ](#login)

### - [Create Post](#create-post)

### - [Comment, Update, Delete](#edit-post)

### Site navigation

Two version to view to the navigation.
![Site Navigation 1](static/images/nav1.png/)
![Site Naviation 2](static/images/nav2.png/)

#### Sign In

![Sign in](static/images/sign_in.png)

### Home

![Home](static/images/home.png)

### About

![About](static/images/about.png)

### Artists

![Artists](static/images/artists.png)

### Profile

![Artist profile 1](static/images/profile1.png)
![Artist profile 2](static/images/profile2.png)

### Register

## create profile

![Register](static/images/register.png)

### Login

![login](static/images/login.png)

### Logout

![logout](static/images/logout.png)

### Default images

- Of course if the user chooses not to upload a profile image or does not have the image of the artwork they wish to sell default images are provided.
  ![Default image 1](static/images/default1.png)
  ![Default image 2](static/images/default2.png)

### Create Post

-Users can inuitively create posts.
![Create Post](static/images/create%20post.png)

### Post details

![Post Details 1](static/images/postdetails.png)
![Post Details 2](static/images/postdetails2.png)

### Edit post

### Edit & delete post

When the user is logged in they can update and delete their posts.

![Edit post ](static/images/crud1.png)
![Delete post ](static/images/delete1.png)
![Edit post ](static/images/edit_post.png)

### Edit profile

### Edit & Delete Profile

When the user is logged in they can update and delete their profile.

![Edit profile ](static/images/update_delete.png)
![Delete profile ](static/images/delete_profile.png)
![Update profile ](static/images/update_profile.png)

### Comment

### Comment & Delete Comment

Users can comment on other users posts.
![comments ](static/images/comments.png)
![delete comment  ](static/images/delete_comment.png)

### Future Features

These are the features I would like to add in the future.

- Buy and mail artwork functionality, more e-commerce overall
- Artists recent exhibitons, a way to update.
- A bidding system
- Artist commission portal
- More Javascript to the site

[Back to top](#ms-dashboard)

## Languages used

- HTML5
- CSS3
- Javascript
- Python
- Django

### Frameworks and libraries and tools

- GitPod
- GitHub
- Django
- Bootstrap
- Jquery

### Installed packages

- asgiref==3.5.2
  ASGI (Asynchronous Server Gateway Interface) framework for building asynchronous web applications. It's a part of Django.

- cloudinary==1.29.0
  A Python wrapper for the Cloudinary cloud-based image and video management service, allowing you to store, manage, and deliver media assets easily.

- dj-database-url==0.5.0
  A simple utility for using database URLs in Django. Useful for configuring database connections with environment variables.

- dj3-cloudinary-storage==0.0.6
  A Django storage backend for Cloudinary, allows you to integrate Cloudinary with a Django project for media storage.

- Django==3.2.13
  Python web framework for building web applications.

- django-allauth==0.51.0
  An authentication, registration, and account management app for Django. It provides easy user authentication and account management solutions.

- django-crispy-forms==1.14.0
  A Django app that helps manage forms.

- gunicorn==20.1.0
  A popular Python WSGI HTTP server for running web applications.

- oauthlib==3.2.0
  A framework-independent library for implementing OAuth1 and OAuth2 providers.

- psycopg2==2.9.3
  A PostgreSQL adapter for Python. It enables Python applications to connect to PostgreSQL databases.

- pytz==2022.1
  A library for working with time zones in Python. It's particularly useful when dealing with datetime calculations and conversions.

- requests-oauthlib==1.3.1
  A package for providing OAuthlib support to the popular Python requests library. It's used for making OAuth-authenticated requests.

- sqlparse==0.4.2
  A non-validating SQL parser module for Python. It's useful for formatting and parsing SQL statements.

- core.Microsoft
  Custom package related to Microsoft services.

- core.mongo
  Custom package related to MongoDB.

- core.python
  Custom package related to Python.

## Testing

All testing has been done manually.
Testing as much as possible is reflected in the user stories.
Testing has been done constantly throughout all the manifestations of this project.

This is more or less how testing was done:

- Does the code do what I want it to do?
- Are there any bugs ?
- Remove bugs
- Check user stories
- Test for CRUD functionality
- Make code "Pretty"
- Run through validator

### Bugs during development

- There were not so many bugs but the bugs I did have were mostly sytanctial.

- The biggest bug happend to be syntactical. I had used the inccorect boostrap wording and it made viewing another users profile diffiuclt when already logged in. The already logged in user would upon viewing another users profile be logged in as that user but none of the actual functions came along with it.

### Unfixed Bugs

#### Lighthouse score / testing

- The image sizes are bringing down my scores dramatically but since images are uploaded by users, this is beyond my control for now but in a future implementation, I plan on restricting file sizes to 24mb.
  ![Lighthouse score 1](static/images/lighthouse_score_1.png)
  ![Lighthouse score 2](static/images/lighthouse_score_2.png)
  ![Lighthouse score 3](static/images/lighthouse_score_3.png)

- I could not figure out how to rewrite this in way that passes.
  ![Validator testing](static/images/linter_bug.png)

- In an earlier manifestation of the app I tried to include and infinite scroll but I got some strange "glitch" effect where there was anything more to load.

- With the google WAVE tool there are errors about my color choices, but have chosen to keep my choices for asestetic reasons.

#### WAVE

- WAVE contrast errors - I am aware WAVE is highlighting my font colour choice as problematic, but I have made an aesthetic decision to keep it this palette.

[Back to top](#table-of-contents)

### Validator Testing

## Testing

## TESTING ESSENTIAL FUNCTIONS AS A TABLE :

This table does not include every feature , just the essential features.
| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| ------------------------- | -------------------------------------------------- | --------------------------------------------- | ----------------- |
| Home page | Images load , scroll enabled | Everything wroks | Works as expected |
| Home page | Links clickable (including nav bar) and make sense | Links to work | Works as expected |
| Artist page | page loads propwerly and displays all artists | page loads propwerly and displays all artists | Works as expected |
| Artist page | Click artitst @ links | Images load and links lead to profile page | Works as expected |
| About page | click to open up | Displays text, images ad loads properly | Works as expected |
| Footer | Test for responsiveness | Is responsive | Works as expected |
| Create Post -any page | Test for CRUD functionality | CRUD functionality works | Works as expected |
| Create Profile - any page | Test for CRUD functionality | CRUD functionality works | Works as expected |
| Comment | Test for comment functionality | allows user to comment and delete comment | Works as expected |
| Resgister page | Attempt to register | Allows user to sign up | Works as expected |
| Login / Logout | User can login or logout | Allows user to login and logut | Works as expected |

Testing with https://validator.w3.org/ shows no errors on ALL html pages:

![Validator testing](static/images/home_html.png)

Testing and validating using pep8 validations tools passes for ALL python files used in this project.:

Testing with https://jigsaw.w3.org/css-validator/ shown no errors on CSS:

![Validator testing](static/images/w3c.css.png)

## Deployment

The site was deployed to Heroku using these steps:

- First a requirements.txt file is needed to migrate the database before deployment
- I used the usual config vars, Secret key value ,Port value, DATABASE_URL value, these values were stored env.py file
- Set Heroku as an allowed host.
- Create GitHub procfile
- Then after final push , on the Heroku site youu just deploy

## Security notes

- In the commits there is a secret key displayed but I have changed the actual secret key in my proper env file.

## Content

All creative work on this project belongs to the author of this project.

## Credits

The idea for the site layout came from art gelleries in Berlin and New York:

- [Art Galllery New York](https://www.davidzwirner.com/)
- [Art Galllery Berlin ](https://www.kindl-berlin.de/)

The artwork used to populate the site came from the following webistes:

- [Site 1](https://www.thecollector.com/5-rising-black-artists-shaking-the-art-market/)
- [Site 2](https://www.darkyellowdot.com/black-contemporary-artists/)
- [Site 3](https://www.artandobject.com/slideshows/10-contemporary-black-artists-you-should-know-more-about)
- [Site 4](https://www.thecollector.com/5-rising-black-artists-shaking-the-art-market/)
- [ Francis Bacon ](https://www.francis-bacon.com/artworks/paintings/1950s)

The random comments and back stories are a mix of [Wikipedia](https://www.wikipedia.org/) and [ChatGPT](https://chat.openai.com)

The skeleton of the project come from Code Institue project 4 [CI](https://codeinstitute.net/)

The outline for the README doc came from:

- [Readme Doc ](https://github.com/Pelikantapeten/p4-ms-dashboard)

### Acknowledgment

- My Advisor: [Lauren-Nicole Popich](https://www.linkedin.com/in/lauren-nicole-popich-1ab87539/)
