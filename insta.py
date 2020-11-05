from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import datetime


class MattSal:
    # Username and password to the Instagram account
    username = 'XXXXXXX'
    password = 'XXXXXXX'

    # Hashtags desired to be commented on
    hashtags = ['woodworking', 'wood', 'handmade', 'woodwork', 'woodworker', 'diy']

    # First set of comments (20). Has initial engaging comment and comment to invite users to your page
    comments = ['Your posts are amazing! I would love to hear what you think about mine!',
                "Amazing work, keep it up! What do you think of my page?",
                'You have magnificent photos! Reminds me of some I took on my last project!',
                'Your work fascinates me! I hope my page fascinates you!',
                'I like how you put your posts together! Can you give me some feedback on how I put my posts together?',
                'I love your page, great work! How does mine match up?',
                'Really nice photo, great job! Are my photos good?',
                'Well done, I love the work! How do you like my work?',
                'I love the detail of your work! I put so much detail into my work too!',
                'I think your posts are astonishing! What you think about my posts?',
                "Stunning work, keep going! Do you think my last post is cool?",
                'You take breathtaking pictures! Reminds me of my last post!',
                'Everyone thinks your work is great! I hope my work captivates you!',
                'I enjoy looking at how you put your posts together! Can you give me your thoughts on how I put my posts together?',
                'Your page is lovely, great work! How is my page?',
                'Really interesting picture, great job! Is my last post good quality?',
                'Job well finished, I am entranced with the work! Thoughts on my work?',
                'I enjoy the detail of your posts! I put so lots of detail into my work also!', ]

    # Last word commented (50). Positive adjectives to leave a good impression.
    lastWord = ["Fantastic", "Incredible", "Unbelievable", "Wonderful", "Astonishing", "Astounding", "Awesome", "Breathtaking", "Brilliant", "Extraordinary", "Marvelous", "Fabulous", "Unimaginable", "Tremendous", "Stupendous", "Unexpected", "Phenomenal", "Spectacular", "Stunning", "Overwhelming", "Remarkable", "Prodigious", "Shocking", "Stupefying", "Eye-opening", "Surprising", "Mind-blowing", "Striking", "Mind-boggling", "Sensational", "Great", "Miraculous", "Beautiful", "Bewildering", "Portentous", "Wondrous", "Magnificent", "Startling", "Exciting", "Confounding", "Eye-poping", "Ravishing", "Monumental", "Capturing", "Fascinating", "Terrific", "Gorgeous", "Outstanding", "Significant", "Staggering"]

    # Last punctuation commented (6). Creates more combinations of comments
    lastPunctuation = [".", "!", "!!", "!!!", " :)", " (:"]

    # First greeting phrase (3).
    firstWord = ["Hello!", "Hi!", "Howdy!"]

    # Array to store links to top posts in the hashtag categories
    links = []

    # Counter variable to click the correct follow button
    followButtonCount = 0


    def __init__(self):
        self.browser = webdriver.Firefox()  # Opens firefox browser
        self.login()                        # Initiates login function
        self.unfollow()                     # Initiates unfollow function
        self.hustle()                       # Initiates hustle function
        self.finalize()                     # Closes the browser

    def login(self):
        # Goes to login page of Instagram
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)

        # Finds username field, clears text, pastes username variable
        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)

        # Finds password field, clears text, pastes password variable
        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        # Finds and clicks the login/submit button
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(2)
        time.sleep(30)

    def hustle(self):
        self.getTopPosts()      # Initiates getTopPosts function
        self.execute()          # Initiates execute function

    def getTopPosts(self):
        # Traverses through each hashtag in the hashtags array.
        for hashtag in self.hashtags:
            time.sleep(4)

            # Goes to the given hashtag explore page
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(2)

            # Scrapes the links of the top posts on the given hashtag & confirms the links
            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(0, 9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    def execute(self):
        # Counter variable to limit amount of comments
        commentCount = 0
        for link in self.links:
            if commentCount < 40:
                self.browser.get(link)  # Goes to the post desired to be commented on
                time.sleep(2)
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scrolls the browser
                time.sleep(1)
                self.comment()  # Initiates the comment function
                time.sleep(2)
                commentCount += 1   # Increases counter variable
                print("Comment Count: " + str(commentCount))    # Prints the current amount of comments to the terminal
                sleeptime = random.randint(28, 36)
                time.sleep(sleeptime)


    def comment(self):
        try:
            # Finds, clicks, and clears the comment text box
            comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
            comment_input().click()
            comment_input().clear()

            # Concatenates the comment string with a random combination of the choices. 18,000 combinations
            comment = random.choice(self.firstWord) + " " + random.choice(self.comments) + " " + \
                      random.choice(self.lastWord) + random.choice(self.lastPunctuation)

            # Types the comment instead of pasting. Ensures Instagram doesn't detect bot activity
            for letter in comment:
                comment_input().send_keys(letter)
                delay = random.randint(1, 7) / 30
                time.sleep(delay)

            comment_input().send_keys(Keys.RETURN)
        except:
            print("Comments on this post have been limited. 'textarea' not found")



    def like(self):
        # Finds the like button and clicks it
        like_button = lambda: self.browser.find_element_by_xpath('//svg[@class="_8-yf5 "]')
        like_button().click()

    def finalize(self):
        # Closes the firefox browser
        self.browser.close()

    def unfollow(self):
        # Goes to current Instagram account and clicks the following button
        self.browser.get('https://www.instagram.com/woodwose_design/')
        time.sleep(3)
        self.browser.find_element_by_xpath("//a[@href='/woodwose_design/following/']").click()

        for i in range(15):
            for a in range(10):         # Must reiterate after 10 to get most recent following accounts
                 self.clickUnfollow(a)  # Unfollows the next account on list
                 print("unfollow count: " + str((a + 1) + (i*10)))  # Prints the unfollow count to terminal
                 time.sleep(random.randint(4, 20))
                 if a == 9:
                     time.sleep(4)
                     self.browser.get('https://www.instagram.com/woodwose_design/')
                     time.sleep(4)
                     self.browser.find_element_by_xpath("//a[@href='/woodwose_design/following/']").click()

    def clickUnfollow(self, followButtonCount):
        time.sleep(random.randint(5, 7))

        # Finds unfollow buttons and clicks the current one
        unfollowButtons = self.browser.find_elements_by_css_selector('.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl')
        unfollowButtons[followButtonCount].click()
        time.sleep(random.randint(5, 7))
        self.browser.find_element_by_css_selector('.aOOlW.-Cab_').click()

while 0 == 0:       # Makes program always run
    currentTime = datetime.datetime.now()       # Store the current date/time into a variable
    currentHour = currentTime.strftime("%H")    # Converts the current time to the current hour
    currentHour = int(currentHour)              # Converts the hour to an int
    if (currentHour > 7) and (currentHour < 9):     # Executes if its the hour in between
        print("creation started")
        mattsalaway = MattSal()                     # creates the object and starts the __init__
    print("30 minutes passed")
    time.sleep(1800)
