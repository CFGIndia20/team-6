# Awaaz

Project for the NGO Jaanagraha by team 6, for the CODE FOR GOOD Hackathon.

## Aim
The primary aim of our project was to make the complaint entry process for civilians easier. The current process includes a 3-step form. The user first chooses the category 
of the complaint, then they choose the location and write a brief description. They might upload an optional picture. Roughly 85% of all complaints have pictures. 

## Our Approach 
So how do we make an already simple process easier, By pre-filling the form for users. We have used a few different approaches described below. The basic user flow is as follows 

Improvement to current process
1. All inputs can be given through voice
1. The user can choose to upload a picture, the ML model predicts a category. 
   1. If the picture has location metadata extract location from it
   1. This is given as a recommendation to the user. If wrong the user can choose the right one. 
1. The user then enters the description of the complaint
   1. Similar category prediction happens here if not done already
1. User selects category if not done
1. If location is extracted from photo, initialize the map pin on that location
1. User enters location
1. User verifies all fields and registers complaint

Extracting complaints from a Social media post
We extract as much information from a social media post(Any platform) and then create half filled form with public urls
We add these public url as a comment on the post of the user. The user can fill these URLs and add a complaint
data we extract
- User details from the username
- Image from post and use it predict category and location
- Address from the post (The location field starts from this position)
- Description from the post


### Features

DATA EXTRACTION
Extract description and location from a social media post
- Extract location from Google map URL if provided
- Extract PIN Code from post 
- Extract Address from post 
Extract category from the input picture if provided
Extract category from the description 
Adding voice to text functionality to make it easier to enter data
Extract geo-data from the picture metadata

AUTO FILLING
- Filling a half filled form with the data extracted from social media 
- Creating a URL for the half-filled form and adding it as an comment on the social media platform

SENTIMENT ANALYSIS
- Analyzing feedback from social media. If negative feedback follow up

Future Ideas
- Gamification by creating a leaderboard
- Creating user badges to promote the platform
- Rating the citizens to help the NGO detect genuine complaints

### More detailed Explanation of features

##### Extract location from google map URL
Using a regex parser. Given a body of text get the URL. Using the URL get latitude and longitude and use it to initialize the map. The functions can be found in '/app/extract-url-from-para'

##### Extract location from post
Using an RNN ML model get the address features from text. found in '/app/extract-field-from-text'

##### Extract category from input image 
Using a CNN ML model we predict the category given the image. We have implemented it for 5 classes to demo. State-of-the-art models can predict upto 1000 classes very well, so the solution will be able to detect most of the 241 classes. found in '/app/get-category-from-image'

##### Extract category from description
Using a LSTM ML model we predict the category given the image. We have implemented it for 20 classes to demo.

##### Extract location from image metadata
JPG images taken from a smartphone with GPS on have location metadata stored with the picture. If available we use this to predict location. 

#### voice to text 
All text input can be provided through voice input. 

#### Sentiment analysis
Given feedback text a NLP model predicts whether the review is positive or negative. If it is negative we ask for extra details. found in '/app/sentiment-analysis'

### Description of Future features
#### Gamification by using a leaderboard
We keep a track of the number of resolved requests for each user. Based on which we create two leaderboards. One for the current month and the other an all-time leaderboard

#### Rating the citizens 
We could keep a rating system where the rating of an individual is the weighted sum of the following attributes. Number of genuine complaints, percentage of resolved complaints, no of comments etc.


## Project Structure
Our project follows an MVC structure, which is modular with with modules for differeent functionalitites.
All individual features can be found in the `/app` folder.

To run the project install django, keras, and tensorflow

move to the main directory and run `python manage.py runserver`. This will start the server 

