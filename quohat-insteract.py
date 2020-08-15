import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint, choice

browser = webdriver.Chrome(executable_path='./chromedriver')
sleep(2)

my_username = "quohat"
my_password = "quohatteam"
hashtag_list = ['quohat', 'quohatinscard', 'quohatteam']
n = 3  #post per hashtag

# - - - - - - - - - - - - - - - - - - - - - - - - -

def click_follow():
    follow = browser.find_elements_by_class_name('sqdOP.yWX7d.y3zKF')[0]
    if follow.text == 'Follow':   # in case you haven't yet
        follow.click()

def click_like():
    like = browser.find_elements_by_class_name('wpO6b')[1]
    like.click()

def go_next():
    nextphoto = browser.find_elements_by_class_name('_65Bje.coreSpriteRightPaginationArrow')[0]
    nextphoto.click()

def get_description(order):
    description = browser.find_elements_by_class_name('KL4Bh')
    if description == []: return ''
    else:
        description = description[order]
    description = description.get_attribute('innerHTML')
    if 'Image may contain' not in description: return ''
    delimiters = '<img alt="', ' Image may contain: ', '" class="'
    regexPattern = '|'.join(map(re.escape, delimiters))
    description = re.split(regexPattern, description)[2]
    return description

def create_comment(descr):
    # Your time is now. Return whatever you want!
    if (descr == '') or ('possible text that says' in descr):
        return ''
    temp = ['']
    if 'drawing' in descr:
        temp = ['Beautiful :o', 'How long have you been doin this?']
    if 'food' in descr:
        temp = ['Delicious food!',  'This food is out of this world!', 'Tastyyy']
    if 'drink' in descr:
        temp = ['Delicious drink!',  'This drink is out of this world!', 'Tastyyyy']
    if 'nature' in descr:
        temp = ['Nature is something beautiful & mysterious.', 'More of this :D', 'Happy to see yours <3. More of this!', 'What a beautiful sighttt.']
    if 'night' in descr:
        temp = ['Nighttttt', 'Love to see this!']
    if 'shoes' in descr:
        temp = ['Beautiful shoooes! <3', 'Nice shoooes!', 'Coool shoes! <3 Love to see more.']
    if 'dog' in descr:
        temp = ['How lovely this dog is', 'Cutenessssss']
    if 'cat' in descr:
        temp = ['How lovely this cat is', 'Cutenessss']
    if 'car' in descr:
        temp = ['Nice car ^ ^', 'Wooow', 'Car timeee']
    if 'closeup' in descr:
        temp = ['Beautiful ^ ^!', 'More of thisssss', 'Wowwww']
    return choice(temp) # Randomly

def comment(content):
    try:  # identify comment box, sometimes it not interactable
        inp = browser.find_elements_by_class_name('Ypffh')[0]
        inp.send_keys('')
    except:
        sleep(1)
        try: inp = browser.find_elements_by_class_name('Ypffh')[0]
        except: pass
    #inp = browser.find_elements_by_class_name('Ypffh')[0]
    inp.send_keys(content)
    sleep(len(content.split()) // 2 + 2) # The more the words, the longer you need to wait :D
    inp.send_keys(Keys.ENTER)

# - - - - - - - L O G I N - - - - - - -

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(5)

username = browser.find_element_by_name('username')
username.send_keys(my_username)
password = browser.find_element_by_name('password')
password.send_keys(my_password)
sleep(randint(2, 4))

try:
    button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div:nth-child(4) > button')
except:
    button_login = browser.find_elements_by_class_name('sqdOP.L3NKy.y3zKF')[0]

button_login.click()
sleep(3)

# - - - - - - - - - - - - - - - - - - - - - - - - -

for hashtag in hashtag_list:
    count = n
    browser.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
    sleep(randint(3, 4))

    # Recently updated
    first_thumbnail = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div[1]/a/div')
    first_thumbnail.click()
    sleep(randint(4, 5))

    while count > 0:
        count -= 1
        description = get_description(9) # You don't need to know that nine, honestly
        text = create_comment(description)
        if text != '': comment(text); sleep(2)
        click_follow(); sleep(2)
        click_like(); sleep(1)
        go_next()
        sleep(randint(3, 5))
