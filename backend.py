from modelo_config_bd.config import *
from modelo_config_bd.modelo import *
from rotas_render import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cadastrar_mestre",methods=["POST"]) # curl -X POST localhost:5000/cadastrar_mestre -d '{"userid":"Spadez","senha":"123456789"}' -H "Content-Type: application/json"
def cadastrar_mestre():
    """Rota responsável por cadastrar um mestre.
    Returns:
        respostra(json): mensagem de sucesso caso tudo ocorre certo.
    """
    try:
        resposta = jsonify({"resultado":"ok"})
        dados = request.get_json(force=True)
        mestre = Mestre(**dados)
        if len(mestre.userid.replace(" ","")) < 3: # Verifica se o usuário possui caracteres válidos.
            resposta = jsonify({"resultado":"user invalid"})
            return resposta
        db.session.add(mestre)
        db.session.commit()
        resposta = jsonify({"resultado":"sucesso"})
    except Exception as e:
        resposta = jsonify({"resposta":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/cadastrar_jogador",methods=["POST"])# curl -X POST localhost:5000/cadastrar_jogador -d '{"userid":"Spades","senha":"123456789"}' -H "Content-Type: application/json"
def cadastrar_jogador():
    """Rota responsável por cadastrar um jogador.

    Returns:
        resposta(json): mensagem de sucesso caso tudo ocorra bem.
    """
    try:
        resposta = jsonify({"resultado":"ok"})
        dados = request.get_json(force=True)
        jogador = Jogador(**dados)
        if len(jogador.userid.replace(" ","")) < 3:
            resposta = jsonify({"resultado":"user invalid"})
            return resposta
        db.session.add(jogador)
        db.session.commit()
        resposta = jsonify({"resultado":"sucesso"})
    except Exception as e:
        resposta = jsonify({"resposta":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/login_jogador",methods=["POST"])# curl -X POST localhost:5000/login_jogador -d '{"userid":"Spades","senha":"123456789"}' -H "Content-Type: application/json"
def logar_jogador():
    """Realiza login de um jogador.

    Returns:
        resposta(json): Retorna sucesso e um jsonweb token caso tudo ocorra certo.
    """
    try:
        dados = request.get_json(force=True)
        user = db.session.query(Jogador).filter_by(userid=dados["userid"],senha=dados["senha"]).first()
        if user == None:
            resposta = jsonify({"resultado":"not user"})
        if user!=None:
            resposta = jsonify({"resultado":"sucesso"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    return resposta

@app.route("/login_mestre",methods=["POST"])# curl -X POST localhost:5000/login_mestre -d '{"userid":"Spades","senha":"123456789"}' -H "Content-Type: application/json"
def logar_mestre():
    """Realiza um login de mestre.

    Returns:
        resposta(json): Retorna um sucesso e um jsonweb token caso tudo ocorra bem.
    """
    try:
        dados = request.get_json(force=True)
        print(dados)
        user = db.session.query(Mestre).filter_by(userid=dados["userid"],senha=dados["senha"]).first()
        if user == None:
            resposta = jsonify({"resultado":"not user"})
        if user!=None:
            resposta = jsonify({"resultado":"sucesso"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/criar_personagem",methods=["POST"]) 
def criar_personagem():
#  curl -X POST localhost:5000/criar_personagem -d '{"mestreid":"Spades","jogadorid":"Spades","nome_do_personagem":"Ricardo","nex":"5%","forca":1,"agi":1,"int":1,"pre":1,"vig":1,"vd_max":20,"san_max":20,"pe_max":10}' -H "Content-Type: application/json"
    """Realiza o cadastro de um personagem de rpg.

    Returns:
        resposta(json): Retona sucesso caso o personagem seja criado.
    """
    try:
        resposta = jsonify({"resultado":"ok"})
        dados = request.get_json(force=True)
        personagem = Personagem(**dados)
        if db.session.query(Personagem).filter_by(jogadorid=dados['jogadorid'],mestreid=dados['mestreid']).first() is not None:
            print('entrou1')
            # Este condição impede a criação de vários por uma mesma pessoa.
            # Uma pessoa só pode criar um personagem para cada mesa que estiver jogando, sendo assim 1 personagem para a relação de 1 jogador e 1 mestre.
            resposta = jsonify({'resultado':'personagem já cadastrado'})
            return resposta
        db.session.add(personagem)
        personagem = db.session.query(Personagem.id).filter_by(jogadorid=personagem.jogadorid).first()
        db.session.commit()
        resposta = jsonify({"resultado":"sucesso","detalhes":personagem.id})
    except Exception as e :
        print(e)
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/listar/<string:identificador>",methods = ["POST"]) #curl -X POST localhost:5000/listar/player -d '{"id":"2"}' -H "Content-Type: application/json" -i
def listar(identificador):
    """Realiza a listagem de alguns registros.

    Args:
        identificador (string): Identifica qual é a tebela de listagem.

    Returns:
        resposta(json): Uma lista erm json com os registros.
    """
    try:
        resposta = jsonify({"resultado":"ok"})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        dados = request.get_json(force=True)
        if identificador == "jogador": # Caso seja um jogador chamando a função ela retornará o seu personagem.
            person = db.session.query(Personagem).filter_by(jogadorid = dados["id"]).first()
            personagem = person.retorna_personagem()
            resposta = personagem
        elif identificador == "mestre": # Caso seja um mestre a função retornará todos os jogadores da sessão.
            # curl -X POST localhost:5000/listar/mestre -d '{"id":"Spadez"}' -H "Content-Type: application/json" -i
            personagem =  db.session.query(Personagem).filter_by(mestreid = dados["id"]).all()
            person_json =[ x.retorna_personagem() for x in personagem]
            resposta = jsonify(person_json)
    except Exception as e:
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    return resposta

# curl -X PUT localhost:5000/update_personagem/simples --data '{"id":"2","dano_sofrido":6,"cura":null,"san_regen":null,"dano_mental":5,"pe_gasto":null}' -H "Content-Type:application/json"
@app.route("/update_personagem/<string:identificador>",methods=["PUT"]) 
def update_personagem_simples(identificador):
    """Realiza o update dos dados de um personagem.

    Args:
        identificador (string): Indica o tipo de update do personagem.

    Returns:
        resposta: Retorna sucesso caso tudo ocorra certo.
    """
    resposta = jsonify({'resultado':'ok'})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    if identificador == "simples":
    # O update simples será utilizado durante as sessões, principalmente durante cenas de combate.
    # Realiza a atualização de poucos atribuitos como vida, sanidade e pontos de esforço.
        try:
            dados = request.get_json(force=True)
            personagem = db.session.query(Personagem).filter_by(jogadorid = dados["id"]).first()# Encontra o registro que sera modificado.
            if dados["dano_sofrido"] !='':
                personagem.vd_atual = personagem.vd_atual - int(dados["dano_sofrido"])
            if dados["cura"] !='':
                personagem.vd_atual = personagem.vd_atual + int(dados["cura"])
            if dados["dano_mental"] !='':
                personagem.san_atual = personagem.san_atual - int(dados["dano_mental"])
            if dados["san_regen"]!='':
                personagem.san_atual = personagem.san_atual + int(dados["san_regen"])
            if dados["pe_gasto"] !='':
                personagem.pe_atual = personagem.pe_atual - int(dados["pe_gasto"])
            db.session.commit()
            print('deu bom')
            resposta = jsonify({"resultado":"sucesso"})
        except Exception as e:
            print(e)
            resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        return resposta
    elif identificador == "complexo":
    # curl -X PUT localhost:5000/update_personagem/complexo -d '{"id":"2","nex":10,"vd_max":30,"san_max":25,"pe_max":4,"forca":3,"agi":2,"vig":3,"int":0,"pre":2,"nome":null}'
    # O update complexo será utilizado quando um jogador subir de nível ou receber um item que quebra os limites padrões de atributos.
    # Realiza a atualização de quase todos os atributos de um personagem.
        try:
            dados = request.get_json(force=True)
            personagem = db.session.query(Personagem).filter_by(jogadorid = dados["id"]).first()# Encontra o registro que sera modificado.
            if dados["nex"] !='':
                personagem.nex = dados["nex"]
            if dados["vd_max"] !='':
                personagem.vd_max = dados["vd_max"]
                personagem.vd_atual = dados["vd_max"]
            if dados["san_max"] !='':
                personagem.san_max = dados["san_max"]
                personagem.san_atual = dados["san_max"]
            if dados["pe_max"] !='':
                personagem.pe_max = dados["pe_max"]
                personagem.pe_atual = dados["pe_max"]
            if dados["forca"] !='':
                personagem.forca = dados["forca"]
            if dados["agi"] !='':
                personagem.agi = dados["agi"]
            if dados["int"] !='':
                personagem.int = dados["int"]
            if dados["vig"] !='':
                personagem.vig = dados["vig"]
            if dados["pre"] !='':
                personagem.pre = dados["pre"]
            if dados["nome"] !='':
                personagem.nome = dados["nome"]
            db.session.commit()
            resposta = jsonify({"resultado":"sucesso"})
        except Exception as e:
            print(e)
            resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        return resposta

@app.route("/deletar_personagem", methods = ["DELETE"])# curl -X DELETE localhost:5000/deletar_personagem -d '{"id":"2"}' -H "Content-Type: application/json"
def deletar_personagem():
    """Deleta um personagem do banco de dados.

    Returns:
        resposta: Retorna sucesso caso tudo ocorra certo.
    """
    try:
        dados = request.get_json(force = True)
        personagem = db.session.query(Personagem).filter_by(id = dados["id"]).first()
        db.session.delete(personagem)
        db.session.commit()
        resposta = jsonify({"resultado":"sucesso"})
    except Exception as e:
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route('/excluir_personagem', methods=['POST'])
def excluir_personagem():
    dados = request.get_json(force = True)
    nome_personagem = dados['nome']
    personagem = Personagem.query.filter(Personagem.nome_do_personagem.ilike(nome_personagem)).first()
    
    if personagem:
        db.session.delete(personagem)
        db.session.commit()
        resposta = jsonify({'retorno': 'sucesso'})
    else:
        resposta =  jsonify({'retorno': 'erro'})
        return resposta
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    

app.run(debug=True)