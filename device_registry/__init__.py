import os
import markdown

# import the framework
from flask import Flask
# create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index():
    # open readme file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

      # read the content of the file
      content = markdown_file.read()

      # convert to HTML
      return markdown.Markdown(content)
