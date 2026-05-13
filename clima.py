import requests
import json
from datetime import datetime

class Cor:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    BRANCO = '\033[0m'
    NEGRITO = '\033[1m'

print("=== Previsão do tempo - Persi Clima ===\n")

api_key = "33ece5af"

try:
    with open("historico.json", "r") as arquivo:
        historico = json.load(arquivo)
    print(f" Historico carregado: {len(historico)} consultas anteriores.\n")
except FileNotFoundError:
    historico = []
    print(" Nenhum histórico anterior encontrado.\n")

print("Digite sair para encerrar ou historico para ver as buscas anteriores.\n")

while True:
    print("\n" + "-" * 40)

    cidade = input("Digite o nome da cidade ex: São Paulo: ")
    
    if cidade.lower() == "sair":
        print("\n Até logo!")
        break
    
    elif cidade.lower() == "historico":
        if len(historico) == 0:
            print(" Nenhuma cidade consultada ainda.")
        else:
            print("\n Historico de consultas:")
            for i, item in enumerate(historico):
                if isinstance(item, dict):
                    print(f" {i+1}. {item['cidade']} - {item['data']}")
                else:
                    print(f" {i+1}. {item} - (sem data)")
        continue
    url = f"https://api.hgbrasil.com/weather?key={api_key}&city_name={cidade}"

    print("\n🔍 Buscando dados...")
    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200 and dados.get("results"):
        clima = dados["results"]
        
        # Verifica se a API retornou a cidade correta (não um padrão)
        cidade_retornada = clima['city'].split(',')[0].lower()
        cidade_buscada = cidade.lower()
        
        if cidade_retornada not in cidade_buscada and cidade_buscada not in cidade_retornada:
            print(f"{Cor.VERMELHO}❌ Cidade '{cidade}' não encontrada.{Cor.BRANCO}")
            continue
    
        print(f"\n{Cor.NEGRITO}📍 Cidade: {clima['city']}{Cor.BRANCO}")
        
        temp = clima['temp']
        if temp > 30:
            print(f"{Cor.VERMELHO}🌡️ Temperatura: {temp}°C{Cor.BRANCO}")
        elif temp < 15:
            print(f"{Cor.AZUL}🌡️ Temperatura: {temp}°C{Cor.BRANCO}")
        else:
            print(f"🌡️ Temperatura: {temp}°C")
            
        print(f"📈 Máxima: {clima['forecast'][0]['max']}°C | 📉 Mínima: {clima['forecast'][0]['min']}°C")
        print(f"💧 Umidade: {clima['humidity']}%")
        print(f"🌥️ Condição: {clima['description']}")

        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        historico.append({"cidade": cidade, "data": agora})

        with open("historico.json", "w") as arquivo:
            json.dump(historico, arquivo)
        print(f"{Cor.VERDE}✅ Histórico salvo automaticamente{Cor.BRANCO}")
    else:
        print(f"{Cor.VERMELHO}❌ Cidade '{cidade}' não encontrada.{Cor.BRANCO}")