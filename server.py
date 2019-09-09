from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index_form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submitInfo():
    # In order to retrieve information from html page
    # make sure that the form has action='/<some_route>' and method='POST'
    # each input field will have a 'name = '' ' so by that field
    # we can retrieve the information in backend using request.form[' ']
    name = request.form['username']
    dojo_location = request.form['location']
    lang = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', username = name, dojo = dojo_location, prog_lang = lang, user_com = comment)


if __name__ == '__main__':
    app.run(debug = True)