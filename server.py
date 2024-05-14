from datetime import datetime
from pprint import pprint

from flask import Flask, render_template
import requests

app = Flask(__name__)

def blog_api():
    """i create the data of the blog  in json format using api.npoint.io website"""
    # API endpoint for the blog data
    blog_url = "https://api.npoint.io/d937dbee332b21507b50"
    
    # Fetch data from the API
    response = requests.get(blog_url)
    response_json = response.json()
    
    return response_json


@app.route("/")
def blog():
    """this method show all the blog post in the main page blog.html"""
    # Retrieve blog data
    data = blog_api()
    
    # Render the template 'blog.html' with the retrieved data
    return render_template('blog.html', post=data)


@app.route("/post_details/<post_id>")
def post_details(post_id):
    
    # print(type(post_id))
    
    """this is the method that will show the blog details"""
    # Retrieve blog data (same as in the 'blog' route)
    data = blog_api()
    # pprint(data)
    
    #We need the post corresponding to the ID sent in the URL
    for post in data:
        
        # We iterate through all JSON data to find the information corresponding to the ID sent in the URL.
        if post["id"] == int(post_id):
            
            post_data={
                "title": post["title"],
                "body": post["body"],
            }
            
            print(type(post_data)) 
 
    # Render the template 'post.html' (you can customize this route as needed) with the retrieved data
    return render_template('post.html', post=post_data)


if __name__ == '__main__':
    app.run(debug=True)
