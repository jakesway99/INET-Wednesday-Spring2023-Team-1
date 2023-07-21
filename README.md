# NYU Beat Buddies

NYU Beat Buddies is a platform designed to connect music lovers that operates similarly to a dating app. 

## Project Overview

Upon signing up, users create a profile listing their favorite songs, artists, albums, and answer prompts about their music tastes. To enhance the matching experience, users can also share that they are interested or attending music events happening in New York City.

Once a user profile is set up, users can explore other profiles. Users can browse through other profiles, and if interested, match with them. Matches unlock a chat feature where users can discuss their shared love for music and plan event attendances, among other topics. 

One of the key features of NYU Beat Buddies is its integration with Spotify. Users can play snippets of songs directly from their profile, and also hear other user's songs. This allows for an immersive and interactive user experience as profiles can literally resonate with the musical tastes of the user.

## Technical Details

- The platform was built using Django for the backend, providing a robust and scalable framework. 
- The frontend was designed with HTML5. NYU Beat Buddies integrates with the Spotify API to allow users to play song snippets directly from their profiles and the Ticketmaster API to fetch information about music events in New York City.
- For deployment and data management, we used Amazon Web Services (AWS). Our application is hosted on AWS and we use Amazon RDS for our SQL database needs.


[Develop](http://dev.nyubeatbuddies.com/):
[![Build Status](https://travis-ci.com/gcivil-nyu-org/INET-Wednesday-Spring2023-Team-1.svg?branch=develop)](https://travis-ci.com/gcivil-nyu-org/INET-Wednesday-Spring2023-Team-1)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/INET-Wednesday-Spring2023-Team-1/badge.svg?branch=develop)](https://coveralls.io/github/gcivil-nyu-org/INET-Wednesday-Spring2023-Team-1?branch=develop)

