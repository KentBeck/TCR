import sublime
import sublime_plugin
import os

# This is the Sublime Text 3 plugin to run tcr.sh on save.
#
# Put this file here: ~/Library/Application Support/Sublime Text 3/Packages/User

class TcrOnSave(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        filename = view.file_name()
        view.window().run_command('exec', {
            'cmd': ['./tcr.sh'],
            'working_dir': '/Users/kelly.sutton/workspace/plain-david',
        })
