from flask import Flask, render_template

app = Flask(__name__)

# Nosso dicionário de cenas (igual ao anterior!)
cenas = {
    "inicio": {
        "texto": "A fumaça do incenso denso recobre o ambiente. A madeira rangendo sob os seus pés é o único som... Diante de você, o altar aguarda.",
        "escolhas": [
            {"texto": "Avançar e acender a primeira vela.", "destino": "vela_acesa"},
            {"texto": "Recuar e buscar mais informações no grimório.", "destino": "ler_grimorio"}
        ]
    },
    "vela_acesa": {
        "texto": "A chama treme, projetando sombras alongadas nas paredes. Você sente uma presença no quarto. O ritual de fato começou.",
        "escolhas": [
            {"texto": "Perguntar 'Quem está aí?'", "destino": "final_presenca"},
            {"texto": "Manter o silêncio e continuar a prece.", "destino": "final_prece"}
        ]
    },
    "ler_grimorio": {
        "texto": "As páginas estão gastas. Você encontra um aviso rabiscado com urgência: 'Nunca acenda a vela antes da meia-noite'. Você olha para o relógio... são 23:50.",
        "escolhas": [
            {"texto": "Esperar a meia-noite.", "destino": "final_espera"},
            {"texto": "Ignorar o aviso e acender mesmo assim.", "destino": "vela_acesa"}
        ]
    },
    "final_presenca": {
        "texto": "A presença não responde com palavras. A vela se apaga instantaneamente. O escuro é absoluto. \n\n[ FIM DO RITUAL ]"
    },
    "final_prece": {
        "texto": "Sua concentração inabalável é recompensada. As sombras recuam e uma claridade quente toma conta da sala. \n\n[ RITUAL CONCLUÍDO COM SUCESSO ]"
    },
    "final_espera": {
        "texto": "Os dez minutos parecem uma eternidade. Quando o relógio marca 00:00, o grimório se fecha sozinho. A janela bate com força. \n\n[ O MOMENTO PASSOU ]"
    }
}

# Rota principal (quando o jogador entra na aplicação)
@app.route('/')
def pagina_inicial():
    # Renderiza o index.html enviando os dados da cena "inicio"
    return render_template('index.html', cena=cenas["inicio"])

# Rota dinâmica (muda dependendo do botão que o jogador clicar)
@app.route('/<cena_id>')
def mudar_cena(cena_id):
    # Se o ID existir no dicionário, mostra a cena. Se não, volta pro início.
    if cena_id in cenas:
        return render_template('index.html', cena=cenas[cena_id])
    else:
        return render_template('index.html', cena=cenas["inicio"])

if __name__ == '__main__':
    # Roda o servidor web do Flask!
    app.run(debug=True)