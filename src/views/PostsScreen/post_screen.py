
import json

from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from utils import load_kv

load_kv(__name__)

class CircularAvatarImage(MDCard):
    avatar = StringProperty()
    name = StringProperty()

class StoryCreator(MDCard):
    avatar = StringProperty()

class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()

class PostScreen(MDScreen):
    profile_picture = 'https://avatars.githubusercontent.com/u/89080192?v=4'

    def on_enter(self):
        self.list_stories()
        self.list_posts()
    
    def on_start(self):
        self.root.dispatch('on_enter')
    
    def list_stories(self):
       ''' with open('assets/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar=data[name]['avatar'],
                    name=name,
                ))
'''
    def list_posts(self):
        with open('assets/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username=username,
                    avatar=data[username]['avatar'],
                    profile_pic=self.profile_picture,
                    post=data[username]['post'],
                    caption=data[username]['caption'],
                    likes=data[username]['likes'],
                    comments=data[username]['comments'],
                    posted_ago=data[username]['posted_ago']
                ))



