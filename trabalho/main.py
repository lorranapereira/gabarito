from flask import Flask,url_for,session,render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from aluno import Aluno
from dao import AlunoDAO
from form import formulario
app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "a secret key you won't forget"
app.config["BABEL_DEFAULT_LOCALE"] = "pt"	
babel = Babel(app)

@app.route('/')
def lista():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('lista.html',lista = lista)
@app.route('/deletar/<cod>')
def deletar(cod):
    dao = AlunoDAO()
    pessoa = Aluno(codigo=cod)
    dao.excluir(pessoa)
    return redirect('/')
@app.route('/inserir/')
def inserir():
    form = formulario()
    return render_template('formulario.html',form = form,tipo='inserir')
@app.route('/tratandoInserir',methods=['GET','POST'])
def tratandoInserir():
    login = request.form['login']
    idade = request.form['idade']
    a = AlunoDAO()
    aluno = Aluno(login=login,idade=idade)
    a.inserir(aluno)
    return redirect('/')
@app.route('/alterar/<cod>')
def alterar(cod):
    form = formulario()
    a = AlunoDAO()
    aluno = a.buscar(cod)
    return render_template('formulario.html',form = form,tipo='alterar',aluno=aluno)
@app.route('/tratandoAlterar',methods=['GET','POST'])
def tratandoAlterar():
    codigo= request.form['codigo']
    login = request.form['login']
    idade = request.form['idade']
    a = AlunoDAO()
    aluno = Aluno(login=login,idade=idade,codigo=codigo)
    a.alterar(aluno)
    return redirect('/')
if __name__ == "__main__":
    app.env = 'development'
    app.run(debug=True)
