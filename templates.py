'''
Templates for generating Markdown.

I know this isn't the preferred way to handle templates,
but this is the early stages of a pretty small-scale project.
If, down the road, we need to do it the right way with template
directories and stuff then we can modify the code to do it that
way.
'''

index_template ='''
Modcast Index
======================

Hello, this is an index of Primary and Secondary modcast episodes.
There's lots of great information in P&S's modcasts, but since they're
2-5 hour youtube videos, it's hard to access and link to. We're trying
to fix that.

For information on how this was built, why it was built the way it was,
and how to contribute, click [here](info.md).

Episodes
--------------------
{% for episode in episodes %}
  * [{{episode.number}} {{episode.name}}]({{episode.number}}.md)
{% endfor %}
'''

episode_template='''
Episode {{episode.number}}: {{episode.name}}
============================================

This episode is posted at [{{episode.url}}]({{episode.url}}). Special thanks to
{{episode.archivist}} for indexing it.

Episode bookmarks
---------------------
{% for bookmark in episode.bookmarks %}
  * [{{bookmark[1]}}]({{episode.url}}&t={{bookmark[0]|tts}}s)
{% endfor %}
'''
