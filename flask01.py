from flask import Flask, render_template,request,jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
posts = [{
    "Name":"Rohan",
    "Version":'0.0.1',
    'content':'init' 
    },  
    {    
    "Name":"Shen",
    "Version":'0.0.2',
    'content':'Mid' 
    },{
    "Name":"Para",
    "Version":'0.0.3',
    'content':'killer' 
    }]
@app.template_filter('newline')
def newline(n):
    return f'{n} \n'
def scrape_wikipedia(page_title):
    """
    Scrapes the introduction section of a Wikipedia page.
    :param page_title: Title of the Wikipedia page
    :return: Introduction text or an error message
    """
    url = f"https://en.wikipedia.org/wiki/{page_title}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Page not found or unable to fetch data."}

    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    intro_text = ""

    for paragraph in paragraphs:
        if paragraph.text.strip():
            intro_text += paragraph.text.strip()
            break  # Only fetch the first non-empty paragraph

    return {"title": page_title, "intro": intro_text}

@app.route('/scrape', methods=['GET'])
def scrape():
    """
    Endpoint to scrape data from Wikipedia.
    Example usage: /scrape?title=Python_(programming_language)
    """
    page_title = request.args.get('title')
    if not page_title:
        return "Error: Please provide a title parameter.", 400
    result = scrape_wikipedia(page_title)
    print(f"Results: {result}")
    if "error" in result:
        return f"Error: {result['error']}", 404
    # Return the result as plain text
    return render_template('scrape.html',value=result)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return "The requested method id GET \n"
    elif request.method == 'POST':
        return "The requested method id POST \n"


@app.route("/about")
def about():
    return render_template("about.html",posts=posts)