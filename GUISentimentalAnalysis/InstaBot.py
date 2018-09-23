# Instagram post,comment, and like puller
import requests, urllib                     # Importing Libraries..
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

APP_ACCESS_TOKEN = "***********************"  # Access_Token: Generate your acess token by urself..
BASE_URL = 'https://api.instagram.com/v1/'

#                           Function declaration to get your own info ........
def self_info():                 # defining Function to ascess users information...
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print (colored('Username: %s\n','blue') % (user_info['data']['username']))
            print (colored('No. of followers: %s\n','blue') % (user_info['data']['counts']['followed_by']))
            print (colored('No. of people you are following: %s\n','blue') % (user_info['data']['counts']['follows']))
            print (colored('No. of posts: %s\n','blue') % (user_info['data']['counts']['media']))
        else:
            print (colored('User does not exist!!\n','red'))
    else:
        print(colored('Status code other than 200 received!\n','red'))

#    Function declaration to get the ID of a user by username


def get_user_id(insta_username):                  # Defining function to get User_ID by passing username ..
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print (colored('Status code other than 200 received!\n','red'))
        exit()

#                Function declaration to get the info of a user by username.............................

def get_user_info(insta_username):            #     Defining function to Get user information by passing username ...
    user_id = get_user_id(insta_username)     #     Calling Function of get user_Id  to further proceed..
    if user_id == None:
        print (colored('Instauser Of This Username does not exist!\n','red'))
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print (colored('Username: %s\n','blue') % (user_info['data']['username']))
            print (colored('No. of followers: %s\n','blue') % (user_info['data']['counts']['followed_by']))
            print (colored('No. of people you are following: %s\n','blue') % (user_info['data']['counts']['follows']))
            print (colored('No. of posts: %s\n','blue') % (user_info['data']['counts']['media']))
        else:
            print (colored('There is no data exists for this user!\n','red'))
    else:
        print (colored('Status code other than 200 received!\n','red'))

#                       Function declaration to get your recent post...................

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)    # using urllib library to download the post by passing link of recent media to it ..
            print (colored('Your image From Your Recent Posts has been downloaded Successfully!\n','green'))
        else:
            print (colored('Post does not exist!\n','red'))
    else:
        print (colored('Status code other than 200 received!\n','red'))

#                    Function declaration to get the recent post of a user by username.................

def get_user_post(insta_username):   # Defining function to get recent posts of a user by passing username to function..
    user_id = get_user_id(insta_username)    # Calling get user id function to get user id by passing username ..
    if user_id == None:
        print (colored('Instauser Of This Username does not exist!\n', 'red'))
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)  # Fetching users recent post by passing link to the function as parameter..
            print (colored('The Image From users Recent Posts has been downloaded!\n','green'))
        else:
            print (colored('Post does not exist!\n', 'red'))
    else:
        print (colored('Status code other than 200 received!\n','red'))


#                 Function declaration to get the ID of the recent post of a user by username........

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)               #         Capturing the user id ......
    if user_id == None:                                 #         checking in case post exists or not .......
        print (colored('InstaUser of this Username does not exist!\n','red'))
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    user_media = requests.get(request_url).json()            #      Fetching json data ........

    if user_media['meta']['code'] == 200:                    #    checking the status code .......
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print (colored('There is no recent post of the user!\n','red'))
            exit()
    else:
        print (colored('Status code other than 200 received!\n','red'))
        exit()
#                        Function declaration to like the recent post of a user.........

def like_a_post(insta_username):                              #     Defining the Function ............
    media_id = get_post_id(insta_username)                     # Getting post id by passing the username .......
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}                 #    passing the payloads ........
    print (colored('POST request url : %s\n','blue') % (request_url)     )    #    post request method  to posting the like ......
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:                        #    checking the status code .....
        print (colored('Like was successful!\n','green'))
    else:
        print (colored('Your like was unsuccessful.Please Try again!\n','red'))



#                 Function declaration to Get the like lists on the recent post of a user.........

def get_like_list(insta_username):            # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/likes?access_token=%s' % (media_id, APP_ACCESS_TOKEN)    #    passing the end points and media id along with access token ..
    print (colored('GET request url : %s\n', 'blue') % (request_url))
    like_list = requests.get(request_url).json()

    if like_list['meta']['code'] == 200:  # checking the status code .....
        if len(like_list['data']):
            position = 1
            print (colored("List of people who Liked Your Recent post", 'blue'))
            for users in like_list['data']:
                if users['username']!= None:
                    print (position, colored(users['username'],'green'))
                    position = position + 1
                else:
                    print (colored('No one had liked Your post!\n', 'red'))
        else:
            print (colored("User Does not have any post.\n",'red'))
    else:
        print (colored('Status code other than 200 recieved.\n', 'red'))

#        Function declaration to Get the lists of comments on  the recent post of a user.........

def get_comment_list(insta_username):  # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id, APP_ACCESS_TOKEN)   #    passing the end points and media id along with access token ..
    print (colored('GET request url : %s\n', 'blue') % (request_url))
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:  # checking the status code .....
        if len(comment_list['data']):
            position = 1
            print (colored("List of people who commented on Your Recent post", 'blue'))
            for _ in range(len(comment_list['data'])):
                if comment_list['data'][position-1]['text']:
                    print (colored(comment_list['data'][position-1]['from']['username'],'magenta') +colored( ' said: ','magenta') + colored(comment_list['data'][position-1]['text'],'blue'))      #    Json Parsing ..printing the comments ..
                    position = position+1
                else:
                    print (colored('No one had commented on Your post!\n', 'red'))
        else:
            print (colored("There is no Comments on User's Recent post.\n", 'red'))
    else:
        print (colored('Status code other than 200 recieved.\n', 'red'))

#                  Function declaration to make a comment on the recent post of the user................

def post_a_comment(insta_username):         #     Defining the function ......
    media_id = get_post_id(insta_username)    #   Getting media id by calling the get post id function....
    comment_text = input(colored("Please Write Your comment: ",'blue'))
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print (colored('POST request url : %s\n','blue') % (request_url))

    post_comment = requests.post(request_url, payload).json()    #   Fetching json data ...
    if post_comment['meta']['code'] == 200:             #      checking status code ......
        print (colored("Successfully added a new comment!\n",'green'))
    else:
        print (colored("Unable to add comment.Please Try again!!\n",'red'))


#                      Function declaration to make delete negative comments from the recent post.........................

def delete_negative_comment(insta_username):   #     Defining the function ......
    media_id = get_post_id(insta_username)     #   Getting media id by calling the get post id function....
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print (colored('GET request url : %s\n','blue') % (request_url))
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())       #    Analysing the sentiments and gives the exact figure upto positivity or negativity..
                print (colored(blob.sentiment,'magenta')    )                                              #    Prints the sentiments and gives the exact figure upto positivity or negativity..
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):                  # Checking condition for negative condition..
                    print (colored('Negative comment : %s','green') % (comment_text))
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print (colored('DELETE request url : %s\n','blue') % (delete_url))
                    delete_info = requests.delete(delete_url).json()       #  Fetching Json data after deleting the comment....

                    if delete_info['meta']['code'] == 200:                   # Checking success code .....
                        print (colored('The Negative Comment From the Post has successfully deleted!\n','green'))
                    else:
                        print (colored('Check Network issues , Unable to delete the comment!!\n','red'))
                else:
                    print (colored('The Comment is Positive comment : %s\n','green') % (comment_text))
        else:
            print (colored('There are no existing comments on the post!\n','red'))
    else:
        print (colored('Status code other than 200 received!\n','red'))

#                   Defining the Main function under which above sub-function works by calling ...........

def start_bot():
    while True:
        print (colored("<------ Lets Get Started ------>\n",'magenta'))
        print (colored('Hey! We Welcomes U to instaBot!\n','green'))
        print (colored('Select your menu options Given Below:\n','blue'))
        print (colored("Select Option:'A' : To Get your own details.\n",'green'))
        print (colored("Select Option:'B' : To Get details of a user by Entering username.\n",'green'))
        print (colored("Select Option:'C' : To Get your own recent post.\n",'green'))
        print (colored("Select Option:'D' : To Get the recent post of a user by Entering username.\n",'green'))
        print (colored("Select Option:'E' : To Get a list of people who have liked the recent post.\n",'green'))
        print (colored("Select Option:'F' : To Like the recent post of a user by Entering username.\n",'green'))
        print (colored("Select Option:'G' : To Get the List of comments on the recent post of a user by Entering username.\n",'green'))
        print (colored("Select Option:'H' : To Make a comment on the recent post of a user.\n",'green'))
        print (colored("Select Option:'I' : To Delete negative comments from the recent post of a user.\n",'green'))
        print (colored("Select Option:'J' : To Exit From The Application..\n",'red'))

        choice = input(colored("Please Select youR choice: ",'blue'))
        if choice.upper() == "A":
            self_info()
        elif choice.upper() == "B":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            get_user_info(insta_username)
        elif choice.upper() == "C":
            get_own_post()
        elif choice.upper() == "D":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            get_user_post(insta_username)
        elif choice.upper() == "E":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            get_like_list(insta_username)
        elif choice.upper() == "F":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            like_a_post(insta_username)
        elif choice.upper() == "G":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            get_comment_list(insta_username)
        elif choice.upper() == "H":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            post_a_comment(insta_username)
        elif choice.upper() == "I":
            insta_username = input(colored("Enter the username of the user: ",'blue'))
            delete_negative_comment(insta_username)
        elif choice.upper() == "J":
            exit()
        else:
            print (colored("Wrong Choice Selected By U",'red'))


#                                Calling the main function ..........to start the application....



start_bot()