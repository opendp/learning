from jinja2 import Environment, FileSystemLoader
import os
from yaml import Loader, load
from pathlib import Path
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')

filename = os.path.join(root, 'index.html')

temp = {'title': '',
        'author': '',
        'description': '',
        'badges': [],
        'link': ''}

all_resources = load(Path('resources.yml').open(), Loader=Loader)

with open(filename, 'w') as fh:
    fh.write(template.render(
        all_resources = all_resources
    ))
