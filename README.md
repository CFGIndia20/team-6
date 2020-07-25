# Awaaz

Project for the NGO Jaanagraha by team 6, for the CODE FOR GOOD Hackathon.

## Aim
The primary aim of our project was to make the complaint entry process for civilians easier. The current process includes a 3-step form. The user first chooses the category 
of the complaint, then they choose the location and write a brief description. They might upload an optional picture. Roughly 85% of all complaints have pictures. 

## Our Approach 
So how do we make an already simple process easier, By pre-filling the form for users. We have used a few different approaches described below. The basic user flow is as follows 

The user can choose to upload a picture, the ML model predict a category. 
If the picture has location metadata extract location from it
This is given as a recommendation to the user. If wrong the user can choose the right one. 
The user then enters the description of the complaint
Similar category prediction happens here
If not selected already the user can enter the category


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
- Identifying sucess stories
- Ask users to give input in specific template

