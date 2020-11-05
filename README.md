# Instagram-Engagement-Bot
insta.py - Python code for program

geckodriver.log - Selenium Module

Demo Video - https://drive.google.com/file/d/1wgAWHN4gYWcV29HhUM-8YqAZ51q_hmPF/view?usp=sharing
# Purpose
After managing my business Instagram account to reach more clients, I realized I was wasting my time becasue I would spend a few hours each day just engageing with other accounts. About a month after being inefficient with my time, I realized that I was trapped in the algorithm and wasn’t doing what I loved. I looked at management services, but they were too expensive. And then it hit me: all I was doing was tapping on certain buttons and scrolling. Why not program a computer to do that. I researched a module that could find buttons by their HTML/CSS attributes and click on them. From then on, Python and the selenium module did the work for me.
# The Selenium Module
The Selenium module allows the program to open and control a browser. From there, it is able to find and click on objects in the browser based on thier HTML/CSS attributes. In order for the module to work, you have to copy the geckodriver.log life into the project folder. Here is more information if it doesn't work: https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path.
# The Plan
First I need the program to log into the instagram account. I utlized Selenium to open a firefox browser, get instagram, and the fill in the login form with my account's credentials. From there, I created a function to go to the accounts I follow, and then unfollow the desired numbers of accounts. The other function I made was to comment on the most popular Instagram posts with the hashtags I wanted. To do this, I made the program go to the hashtags, scrape the links of the posts off the webpage and store them, and then go to each link and comment on the post. Lastly, I made the program always running, but only initiate the bot when I wanted. Working within the Instagram restriction limits, I developed the program to comment with a caption that has 18,000 combinations and run during time intervals to ensure it did not surpass limits.
# Results/Demo Video
https://drive.google.com/file/d/1wgAWHN4gYWcV29HhUM-8YqAZ51q_hmPF/view?usp=sharing. 

This demo video shows the program running while I am away from the computer. The program first unfollows 120 people, and then comments on 40 different posts.
