# playwrights = can help u scrape things. if u have search quieries, stuff to put in a box

import pandas as pd
# The following get ran in the terminal
# pip install playwright
# python3 -m playwright install
from playwright.sync_api import sync_playwright, Playwright
import re
# 1st need to start a playwright server

# The following lines will activate a playwright
# browser, open a new page, and then go to the
# desired page.

pw = sync_playwright().start()

chrome = pw.chromium.launch(headless=False) # getting the chrome browser. headless=false means that
#when it goes, it will open an actual browser u can play and click. =true wont open a browser
# u want a browser to come up os u can see what it's doing. 
#but doing this will take a bit more time and cant pararelize it

page = chrome.new_page() # will actually open the browser

page.goto('https://www.imdb.com/title/tt0290988/reviews/?ref_=tt_ov_ql_2')

# page.locator('css=.ipc-see-more__text').click()

# Display all reviews

page.get_by_test_id("tturv-pagination").get_by_role("button", name="All").click() 
# opens many other functions we can use to access on the page
# get by test id = help by testinit out. creating a test id allowing u to access it directly
# if it has a test id this is what u always want to target
# inspect, click all button .... 
#once it find the tturv pagination, it will find it, will find a button names All and click it. 

# The class below will grab the entire review block
# and the class can change on a whim. You'l have to
# inspect the page to find the correct class.

reviews = page.locator('css=.sc-d59f276d-1') # this =.sc ---- is dynamic, it wont work tmr or nxt wk

# You'l always count your objects, for the sake
# of iterating over them.

reviews_count = reviews.count() # we always need to know how many thigns we have

# You'll make constant use of the nth() function!

reviews.nth(0).hover() # going to reviews, the nth 0 (first thing) and hover over it. will automatically 
reviews.nth(3).click() # clicking on the fourth one
reviews.nth(0).locator('css=.ipc-rating-star--rating').inner_text() # go back to 1st, use locator and get the inner text of that

# The is_visible function is very useful when you have 
# include something condition (i.e., if no star is visible,
# then return None in your DataFrame).

reviews.locator('css=.ipc-list-card--border-speech').nth(3).locator('css=.ipc-rating-star').is_visible()
# is visible = not everything has what we want and if we iterte over it, we have to account for it not being there
#like not every review has a star rating, and itwill be looking for it for 30sec and if doesnt find it will stop and get an error
#we dont want it to stop. . this helps with this situation

# Lots of flexibility with how you find elements!
# Most of the time you are looking for the inner text.

review = reviews.nth(0).get_by_test_id('review-overflow').inner_text()

# You'll always have to create a list to your data!
review_list = []

# if blocked bc of a 'spoiler' button, we need to clikc on it to access the review.  = if statement - 
# if the nth has button called spoiler, if its visible, get this same thing and click it

for i in range(0, reviews_count): # loop over entire review count
    # A fun surprise! Some reviews have a spoiler button!
    if reviews.nth(i).get_by_role("button", name="Spoiler").is_visible():
        reviews.nth(i).get_by_role("button", name="Spoiler").click()
    # This pulls out the information from every individual review   
    review_text = reviews.locator('css=.ipc-list-card__content').nth(i).locator('css=.ipc-html-content').inner_text() # find car content, fet locator and get inner text for each review
    #review_text = reviews.nth(i).locator('css=.ipc-list-card__content').inner_text()
    # Hitting some cleanup!
    review_text = re.sub(r'\n', ' ', review_text) # fixing some line breaks
    # You'll usually have to create a DataFrame for each review
    review_df = pd.DataFrame({'review': [review_text]})
    review_list.append(review_df)
    
pd.concat(review_list)

page.get_by_placeholder('Search IMDb').fill('Barbie') # get by palceholder = any search bar that 
#got text already there, the text is a playholder, u can search by that text ('search imdb') can search by barbie

page.locator('css=#suggestion-search-button').click() #this brings up the search for the barbie stuff

page.locator('css=.ipc-metadata-list-summary-item__t').nth(0).click() # selected the first one that appeared in the search

page.get_by_text('User reviews').nth(0).click() # went to barbie user reviews

page.close()

chrome.close()

pw.stop()