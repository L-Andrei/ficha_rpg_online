from modelo_config_bd.config import *

@app.route('/render_cadastro')
def render_cadastro():
    return render_template('cadastro.html')

@app.route('/render_menu')
def render_menu():
    return render_template('menu.html')

@app.route('/render_personagem')
def render_personagem():
    return render_template('personagem.html')

@app.route('/render_mestre')
def render_mestre():
    return render_template('mestre.html')

@app.route('/new_personagem')
def new_personagem():
    return render_template('criar_personagem.html')

@app.route('/render_update')
def render_update():
    return render_template('update_personagem.html')