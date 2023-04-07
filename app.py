from flask import Flask , render_template , request , url_for , flash
import urllib.request, json

app = Flask(__name__)

@app.route('/')
def homepage():
    url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=413854a07ca91e30946bd3805915f03c'
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    filmes = jsondata['results'][:3]	 # Obtém os três primeiros filmes
    return render_template('homepage.html', filmes=filmes)




@app.route('/filmes/<propriedade>')
def filmes(propriedade):
	if propriedade == 'populares':
		url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == 'kids':
		url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == '2010':
		url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == 'drama':
		url = 'https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == 'brad_pitt':
		url = 'https://api.themoviedb.org/3/discover/movie?with_people=287,819&sort_by=vote_average.desc&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == 'rank':
		url = 'https://api.themoviedb.org/3/discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == '2023':
		url = 'https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2023&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == 'geral':
		url = 'https://api.themoviedb.org/3/discover/movie?primary_release_date.gte=2014-09-15&primary_release_date.lte=2014-10-22&api_key=413854a07ca91e30946bd3805915f03c'
	elif propriedade == '2022':
		url = 'https://api.themoviedb.org/3/discover/movie?with_genres=18&primary_release_year=2022&api_key=413854a07ca91e30946bd3805915f03c'
		
	resposta = urllib.request.urlopen(url)
	dados = resposta.read()
	jsondata = json.loads(dados)
	return render_template('filmes.html', filmes = jsondata['results'])


if __name__ == "__main__":
    app.run(debug=True)