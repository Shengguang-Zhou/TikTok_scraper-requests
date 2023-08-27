import random
import requests
from bs4 import BeautifulSoup
import time
import streamlit as st

def get_tiktok_userinfo(username):
    user_info = {}
    userNotFoundMessage = "User ID已改变"
    #target website
    url_tiktok = 'https://www.tiktok.com'   # -> check on inspector from chrome
    combined_url = url_tiktok+'/@'+username
    # response get
    response = requests.get(combined_url)
    if response.status_code == requests.codes.ok:
        html= response.content
        # bs4
        soup = BeautifulSoup(html, 'html.parser')
        user_subtitle = soup.find('h2',class_='tiktok-1d3qdok-H2ShareSubTitle ekmpd5l7')
        if user_subtitle:
            user_info['user_subtitle'] = user_subtitle.text.strip()
        followers_num = soup.find('strong',attrs={'data-e2e': 'followers-count'})
        if followers_num:
            user_info['followers_num'] = followers_num.text.strip()
        user_bio = soup.find('h2',class_="tiktok-vdfu13-H2ShareDesc e1457k4r3")
        if user_bio:
            user_info['user_bio'] = user_bio.text.strip()
    elif response.status_code == 404:
        user_info = {"user_subtitle": userNotFoundMessage, "followers_num": userNotFoundMessage, "user_bio": userNotFoundMessage}
    else:
        raise ValueError('访问被拒绝或其他错误',response.status_code)
    return user_info

@st.cache_data()
def getUsersInfoThru(userlist):
    info = []
    for i in range(len(userlist)):
        try:
            user_info = get_tiktok_userinfo(userlist[i])
            info.append(user_info)
        except Exception as e:
            print(f"Error for user {i}: {e}")
        random_sleep = 1 + 3 * random.random()
        time.sleep(random_sleep)
    return info



##############################################################################################################################
##############################################################################################################################
######################################################  TEST CASES     #######################################################
##############################################################################################################################
##############################################################################################################################

# info = []
# username = ['shanleysings','alexanderinvicta','TENFLOW','ShiemB7','big_luke_official','tesi.mae']
#
# for i in range(len(username)):
#     user_info = get_tiktok_userinfo(username[i])
#     random_sleep = 1 + 4 * random.random()
#     time.sleep(random_sleep)
#     info.append(user_info)
#
# print(info)