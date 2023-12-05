from modelo_config_bd.config import *

class Mestre(db.Model):
    userid = db.Column(db.String(254),primary_key=True)
    senha = db.Column(db.String(254))

    def __str__(self):
        s = self.userid
        return s

class Jogador(db.Model):
    userid = db.Column(db.String(254),primary_key=True)
    senha = db.Column(db.String(254))

    def __str__(self):
        s = self.userid
        return s


class Personagem(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    mestreid = db.Column(db.String(254),db.ForeignKey(Mestre.userid),nullable = False) # Utilizado para reconhecer a qual mesa pertence o personagem.
    jogadorid = db.Column(db.String(254),db.ForeignKey(Jogador.userid),nullable = False) # Utilizado para reconhecer o jogador que criou o personagem.
    nome_do_personagem = db.Column(db.String(254))
    nex = db.Column(db.String(254)) # Nível de exposição paranormal de um personagem(sempre aumenta de 5 em 5, sendo 5% o inicial).
    afinidade = db.Column(db.String(254)) # Afinidade elemental de um personagem(apenas adquirida depois dos 50% de NEX).
    vd_max = db.Column(db.Integer) # Vida maxíma sem bonus.
    vd_atual = db.Column(db.Integer) # Vida atual (pode ultrapassar a vida maxíma).
    san_max = db.Column(db.Integer) # Sanidade maxíma. 
    san_atual = db.Column(db.Integer) # Sanidade atual não pode ser maior que maxíma.
    pe_max = db.Column(db.Integer) # Pontos de esforço maxímos.
    pe_atual = db.Column(db.Integer) # Ponto de esforço atuais (pode ultrapassar o pe maxímo).
    forca = db.Column(db.Integer)
    agi = db.Column(db.Integer) # Agilidade de um personagem.
    int = db.Column(db.Integer) # Int de um personagem.
    pre = db.Column(db.Integer) # Capacidade de socialização ou percepção do ambiente.
    vig = db.Column(db.Integer) # Resistência física.

    def retorna_personagem(self):
        personagem = {
            'nex':self.nex,
            'nome':self.nome_do_personagem,
            'vd_max':self.vd_max,
            'vd': self.vd_atual,
            'san_max':self.san_max,
            'san':self.san_atual,
            'pe_max':self.pe_max,
            'pe':self.pe_atual,
            'forca':self.forca,
            'agi':self.agi,
            'int':self.int,
            'pre':self.pre,
            'vig':self.vig
        }
        return personagem
    
    def __str__(self):
        s = f"{self.nome_do_personagem},{self.san_max},{self.pe_max},{self.forca},{self.agi},{self.int},{self.pre},{self.vig}"
        return s
    
with app.app_context():
    db.create_all()