from flask import Flask, render_template,request
import requests


app = Flask(__name__,static_url_path='/static/css')

@app.route('/')
def index():
    api_key='239cfd24d2aa120c5d4176fbe957ad8d'
    url=f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&sort_by=release_date.desc'
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    return render_template('index.html', movies=movies)
    
@app.route('/trending')
def trending():
    api_key = '239cfd24d2aa120c5d4176fbe957ad8d'
    url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    return render_template('index.html', movies=movies)

@app.route('/search')
def search():
    query = request.args.get('query')
    api_key = '239cfd24d2aa120c5d4176fbe957ad8d'
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    return render_template('index.html', query=query, movies=movies)


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
   app.run(debug=True)