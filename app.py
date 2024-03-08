# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB("caminhos.json")

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/pegar_caminho", methods=["POST", "GET"])
def pegar_caminho(id=0):
    if request.method == "POST":
        requeste = request.get_json()
        id = requeste["id"]
        post = db.get(doc_id=int(id))
        return post

    

@app.route("/novo", methods=["GET", "POST"])
def sobre(x=0, y=0, z=0,r=0,id=0):
    if request.method == "POST":
        print(request.form)
        id = request.form.get("id")
        x = request.form.get("x")
        y = request.form.get("y")
        z = request.form.get("z")
        r = request.form.get("r")
        db.insert({"id":id,"x": x, "y": y, "z": z, "r": r})
        return redirect(url_for("sobre"))
    posts = db.all()
    print(posts)
    return render_template("sobre.html",x=x, y=y, z=z, r=r,id=id, posts=posts)


@app.route("/lista_caminhos", methods=["GET"])
def lista_caminhos():
    posts = db.all()
    print(posts)
    return render_template("sobre.html", posts=posts)


@app.route("/deletar_caminho", methods=["POST"])
def deletar_caminho():
    requeste = request.get_json()
    id = requeste["id"]
    db.remove(doc_ids=[int(id)])
    return f"Caminho de id: {id} deletado com sucesso"


@app.route("/atualizar_caminho", methods=["POST"])
def atualizar_caminho():
    requeste = request.get_json()
    id = requeste["id"]
    x = requeste["x"]
    y = requeste["y"]
    z = requeste["z"]
    r = requeste["r"]
    db.update({"x": x, "y": y, "z": z, "r": r}, doc_ids=[int(id)])
    return f"Caminho de id: {id} atualizado com sucesso"






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)