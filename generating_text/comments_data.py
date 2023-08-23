import streamlit as st
import random


def random_text_generator(yourName):
    hello_list = ['''Hey, this is {} from Meme agency. '''.format(yourName),
                  '''Hello, this is {} from Meme agency. '''.format(yourName),
                  '''Hi there, this is {} from Meme agency. '''.format(yourName),
                  '''Hi, this is {} from Meme agency. '''.format(yourName),
                  '''Greetings, this is {} from Meme agency. '''.format(yourName)
                  ]

    talking_great = ['''We're truly captivated by your content! ''',
                     '''Honestly, your videos are on 🔥! ''',
                     '''Your content is a breath of fresh air! ''',
                     '''We're blown away by your unique voice! ''',
                     '''Your stellar streams are exactly what we love! ''']

    who_we = ['''At Meme Agency, as an officially certified Tiktok agency, 
                we see a bright collaboration ahead with talents exactly like you. 
                ''',

              '''We are an officially certified Tiktok agency focusing on helping 
              streamers perform better and earn better with our 0-fee policy.
              ''',

              '''We are an officially certified Tiktok agency focusing on 
              helping streamers perform better. 
              ''',

              '''We are an officially certified Tiktok agency focusing on 
              helping streamers perform better and earn better.
              ''']

    why_join = ['''How about we magnify that creativity? 
    With Meme Agency, you'll find zero fees and unwavering support.''',

                '''At Meme Agency, 
                we charge 0 fees and offer unparalleled backing for your daily support.
                ''',

                '''We are focusing on helping streamers 
                perform better and earn better with our 0-fee policy.
                ''',

                '''With Meme Agency, you'll find zero fees and unwavering support. 
                ''',

                '''With Meme, we will provide one-on-one dedicated operational support, 
                such as Discord operation and live guides. 
                We will also help on bossting your traffic. ''']

    ending = ['''Interested in diving deeper?
                ''',
              '''Any interest in further talk?''',
              '''Any chance for a further talk?''',
              '''Fancy a chat to discuss the possibilities?''',
              '''Any chance for a further talk?''']

    hello_random = random.choice(hello_list)
    talking_great_random = random.choice(talking_great)
    who_we_random = random.choice(who_we)
    why_join_random = random.choice(why_join)
    ending_random = random.choice(ending)

    output = hello_random + talking_great_random + \
             who_we_random + why_join_random + ending_random

    return output
