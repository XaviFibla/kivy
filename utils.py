from kivy.lang import Builder
import os

def load_kv(module_name):
    Builder.load_file(f"{os.path.join(*module_name.split('.'))}.kv")