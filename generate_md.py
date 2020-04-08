#!/usr/bin/env python
'''
generate_md.py: generate modcast markdown from json input.
'''

from jinja2 import Template, Environment, DictLoader
from templates import episode_template, index_template
from utils import timestamp_to_seconds
import json
import os

def render_stuff():
    #TODO: write autoescape functionality for markdown
    env = Environment(autoescape=False,
                      loader=DictLoader(
                          {
                              'README.md': index_template,
                              'EPISODE.md': episode_template
                          }
                      ))

    env.filters['tts'] = timestamp_to_seconds

    #OK this is where I do the programming equivalent of breaking out the duct
    #tape and JB Weld

    episodes = []
    basedir = 'modcasts'
    files = sorted(
        [os.path.join(basedir, fname)\
         for fname in os.listdir(basedir)\
         if fname.endswith('json')]
    )

    #read json files from basedir ('modcasts')
    for fn in files:
        try:
            with open(fn) as f:
                ep_info = json.load(f)
        except Exception as e:
            print("Error loading {}: {}".format(fn,e))
            continue
        else:
            episodes.append(ep_info)

    #generate episode files
    for episode in episodes:
        t = env.get_template('EPISODE.md')
        output = t.render(episode=episode)
        with open('{}.md'.format(episode['number']), 'w') as f:
            f.write(output)

    #generate index file
    t = env.get_template('README.md')
    output = t.render(episodes=episodes)

    with open('README.md', 'w') as f:
        f.write(output)
    
    








if __name__ == '__main__':
    render_stuff()

