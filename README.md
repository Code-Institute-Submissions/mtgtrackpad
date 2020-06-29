# Data Centric Development Milestone Project - MTG Trackpad

In this project I have created a web application that allows Magic: The Gathering players to record their own league results. This provides them with a way to keep a track of their game history and in future developments will provide insightful statistics on their game results.

## UX

### Strategy

The reasons for this project include providing an open space for players to record their game data, as Wizard of the Coast (the creators of Magic: The Gathering) do not release all game data from their online software. This will allow players to have a better understanding of their level of play as well as access to game insights that are withheld from them. Another reason for the introduction of this app is the recent closure of the DCI registration process for Magic: The Gathering players. DCI numbers were how players signed up for tournements in paper magic. All games against your DCI number would be recorded and be easily viewable online and as this is no longer the case, this app provides a simple way to replicate this recording of games. Albiet, manually.

The key demographic for this web application is Magic: The Gathering Players who are interested in game statistics and data with the end result being to improve their knowledge and make the correct choices to improve their results at the game.

#### User Stories

I Identified two users for this site. Players who keep records of their data, and Players who use this data to empower their knowledge

##### Players who keep records

1. As a record keeping player, I am able to record my progress within certain formats and with certain decks, allowing me to build a players record and learn from it.
2. As a record keeping player, I am able to go backwards in time and review events that I was previously a part of.

##### Players who use the data

1. As a player who uses the data, I am able to review what players are doing well with what decks and use this information to improve my own game play and choices.

### Scope

Using the user the above user stories and he project brief I identified the follwoing requirements:

#### Functional Requirements

1. The Project must be able to use the CRUD methodology on a mongodb database for user data management.
2. The webpage must be responsive to a range of devices, so you can play magic and record the event via this application on a portable device.
3. The output of data must be valuable to the user.

#### Non-Functional Requirements

1. Data entry should be intuitive and flexible
2. The site design should be simple and stylish. Easy on the eye but with the focus being on ease of use.

#### Content Requirements

1. The project will need to flask forms.
2. The project will need to contain adverts for potential revenue.
3. Clear and precise information.
4. A mongodb database to store all of the recorded information.

### Structure

For the structure of this project I began with a python application using the following imports:

1. flask
2. pymongo
3. wtforms

I created a template structure of how I envisioned the project working here: [**MTG Trackpad Template**](https://github.com/JPMurdie/mtgtrackpad/blob/f9078a93ba3eef55a438bc98c40094a531e69e9a/MtG%20Trackpad%20Template.pdf)

It quickly became apparent that one of the features I wanted to include involving the addition and removal of games per record would be too difficult and time consuming for my current level of knowledge. I scrapped this feature and went with a standard 5 round form as a minimum viable product.

#### The app routes I included are:

**/hompage** - The home page displays a brief overview of the application as well as a call to action. An advert is placed above a table of the most recently added events. This table is limited to 5 events.

**/player_history/<player_name>** - This route is accessed by a search function in the navigation bar. The search button triggers onclick JQuery to run code against the input value. If the value is empty a modal box will trigger, if not the route will be accessed.

**/new_record** - This route loads a new_event_form() into a page or submits a current form from the page based on the Request Method. The form is built within flask and contains validators both within the form and within the route.

**/edit_record** - Again, this page is dependant on the GET Request Method. With a GET Request the page will load a selected event based on that events ID into a form page that allows the user to edit the data. With a POST Request the updated data will be changed on the database and the user will review to the homepage and relevent flash messages will be displayed.

\*The forms for both new_record & edit_record include custom error message displays below the input field, advising the user on incorrect completion.

**/error.handler(404)** - This route was created as a custom 404 error handler. It displays an image of the malfunction magic: the gathering card and an achor tag directing the user back to the home page. This was introduced as a catch all for routes that do not exist in the application.

### Surface

#### Colours

I wanted the website to be as decluttered as possible. This resulted in going with a clean and simple look. The colours I used were Golden, Bootstrap Warning, Bootstrap Dark and an off yellow for the footer anchor tags and data displays. The pages blend well and look professional in these colours.

## Features

#### All Page Features:

- **Semantic HTML**: All pages have been written with semantic HTML in mind.
- **Responsive Design**: Site pages are designed to work on all sizes of device.

#### Specific Features:

- **Dropdown selector**: The form includes a dropdown selected for the Format field that is fed by another data collection from my database in mongodb.
- **Calculated Insight**: Part of the event calculation is created using data input and added to the form, this allows to user to easily view if their event has been completed, what their record was and how good or bad their game win percentage score was.

### Features Left to Implement

- **Format Insight**: Format insight will be more valuable after players begin to use the site. A format page, displaying the decks and players that are posting the best results within that format would be useful to all who would like to improve their game. That decks weaknesses and strengths as well are more technical insight such as match up percentage wins could be included within this page.

- **Custom events**: I still believe that the ability to add and remove rounds from the form dynamically while using and saving the data will be a great addition to the site. This is something that I will investigate and add when possible.

## Technologies Used

In this project the following technologies have been used.

- **Bootstrap 4**
  - The **Bootstrap 4** framework was used to help layout the webpage

- **JQuery**
  - **JQuery** was used as a part of the **Bootstrap 4** and **Fancybox**

- **Flask**
  - **Flask** was used as the basic model structure for this application
  - **Flask-wtf & wtforms** was use to create the form class. Providing an easy to to create and manipulate the form into the project

- **Python**
  - **PyMongo** helped me to communicate with my mongodb database through prebuild functions and useability.

- **Gitpod**
    -**Gitpod** The application was constructed in Gitpod, since switching to gitpod for my projects I am finding myself learning more that I did via AWS & Cloud9

## Testing

Through this testing I have completed a number of full reviews of the website.

I also gained feedback from local players through our discord channel. Some of this feedback included removing the requirement for number of draws, length restrictions to certain inputs such as player names and deck names (A friend demonstrated this by posting a starwars story as a player's name), and a dropdown box for useability.

The testing I carried out follows:

Anchor tag tests - To make sure links were opening correctly, external anchor were testing for blank targets.

Route tests - I debugged my routes by forcing errors into the site to see how the website would respond. This resulted in more detailed python including if statements and try/exception blocks.

Form tests - I continually tested the form submits to make sure the data was being present correctly to the database. Throughout my testing I also introduced validation into the flask form, these include InputRequired, AnyOf, Optional & length.

Data tests - By building dummy data manually in mongodb and retreiving it to display on the homepage I was able to test the form requests by the homepage display. If the data schema of the request matched my dummy data within mongodb, the html would display it all in the same way. This took a number of itteration to get the python code correct.

It currently looks like this:

event_rounds = []
for i, num in enumerate(['first', 'second', 'third', 'fourth', 'fifth']):
event_rounds.append(
{
'round': i+1,
'opp_name': request.form.get(f'{num}\_oppname'),
'opp_deck': request.form.get(f'{num}\_oppdeck'),
'games_won': request.form.get(f'{num}\_w'),
'games_drawn': request.form.get(f'{num}\_d'),
'games_lost': request.form.get(f'{num}\_l')
},
)
{
'player_name': request.form.get('player_name'),
'mtgformat': request.form.get('mtgformat'),
'deck_name': request.form.get('deck_name'),
'event_date': request.form.get('event_date'),
'event_rounds': event_rounds, # Jquery function calcs these inputs as uneditable fields
'final_record': request.form.get('eventrecordinput'),
'gamewin_perc': request.form.get('eventgamewin'),
'event_status': request.form.get('eventstatusinput')}})

Browers and Device Testing - I tested the application on andriod phone, windows OS and Mac OS through explorer, edge, chrome and safari.
There were no obvious errors and the website remained responsive thanks to the Bootstrap framework. I believe more testing should be done here.

## Deployment

I have hosted my application on heroku and the code is stored in Github.

[**GitHub Repo**](https://github.com/JPMurdie/mtgtrackpad)<br>
[**MTG Trackpad Heroku Deployment**](http://mtgtrackpad.herokuapp.com/homepage)


## Credits

My mentor Reuben Ferrante helped a lot with my understanding of PyMongo and convinced me to stay the course and not switch to sql. I'm glad I did because it was helpful to struggle with the structure of JSON/NoSQL data and learn from it.

Magic: The Gathering - Wizards of the Coast open most of their copyright images and content to allow content creators throughout the world to express themselves. They don't hold content creation back and actively encourage it.

### Media

- Advert Banner was taken from the Magic: The Gathering release page for the new Coreset, Core 2021.
- The card art for the Magic: The Gathering Card, Malfunction, was taken from Magic: The Gathering's card database called The Gatherer.

### Acknowledgements

- A number of Codepen items inspired me throughout the build of this application, but I only took one style line for line. This was golden text by Megan McKinnon as stated in the style.css file within the static folder.
- The style and design of this website, along with the functionality of the data within was insipired by [**MTG Goldfish**](https://www.mtggoldfish.com/)
