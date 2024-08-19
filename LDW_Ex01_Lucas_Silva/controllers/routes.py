from flask import render_template, request
from datetime import date

def init_app(app):
    data_atual = f"{date.today().day}/{date.today().month}/{date.today().year}"
    
    # Listas de ordens de serviço e soluções
    ordens_oficina = [
        {"id": 1, "mecanico": "Lucas", "data": data_atual, "problema": "Defeito no motor", "solucao": None},
        {"id": 2, "mecanico": "Asher", "data": data_atual, "problema": "Problema na suspensão", "solucao": None},
        {"id": 3, "mecanico": "Victor", "data": data_atual, "problema": "Frenagem irregular", "solucao": None},
        {"id": 4, "mecanico": "Gilmar", "data": data_atual, "problema": "Alinhamento necessário", "solucao": None}
    ]
    solucoes = []
    
    @app.route("/", methods=["GET", "POST"])
    def ordens():
        if request.method == "POST":
            if request.form.get("mecanico") and request.form.get("descricao_problema"):
                ordens_oficina.append({
                    "id": len(ordens_oficina) + 1, 
                    "mecanico": request.form.get("mecanico"), 
                    "problema": request.form.get("descricao_problema"), 
                    "data": data_atual,
                    "solucao": None
                })
        
        return render_template("index.html", ordens_oficina=ordens_oficina, data_atual=data_atual)
    
    @app.route("/solucoes", methods=["GET", "POST"])
    def solucoes_ordens():
        if request.method == "POST":
            ordem_id = int(request.form.get("ordem_id"))
            solucao = request.form.get("solucao")
            for ordem in ordens_oficina:
                if ordem["id"] == ordem_id:
                    ordem["solucao"] = solucao
                    break
        
        return render_template("solucoes.html", ordens_oficina=ordens_oficina)
    
    @app.route("/historico")
    def historico_ordens():
        return render_template("resolvidos.html", ordens_resolvidas=ordens_oficina)
