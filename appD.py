import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])  # Sensor 1 (X negativo, Y positivo)
posicao_sensor2 = np.array([100, 100])   # Sensor 2 (X positivo, Y positivo)
posicao_sensor3 = np.array([100, -100])  # Sensor 3 (X positivo, Y negativo)
posicao_sensor4 = np.array([-100, -100]) # Sensor 4 (X negativo, Y negativo)

# Leituras dos sensores (distâncias da tora)
distancia_sensor1 = 70  # Sensor 1
distancia_sensor2 = 70   # Sensor 2
distancia_sensor3 = 70   # Sensor 3
distancia_sensor4 = 70   # Sensor 4

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS
resultado = minimize(regressao_circular_LMS, chute_inicial, args=([distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4], [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio
centro_estimado = resultado.x[:2]
raio_estimado = resultado.x[2]

# Criando a pasta para salvar as imagens, se ainda não existir
pasta_imagens = 'imagens_toras'
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

# Plotando os sensores
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores')

# Plotando as distâncias medidas pelos sensores com texto em verde e um pouco afastado dos sensores
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4} cm', fontsize=10, verticalalignment='top', color='green')

# Calculando o diâmetro da tora
diametro_estimado = raio_estimado * 2

# Plotando o diâmetro estimado
plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {diametro_estimado:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada (um círculo)
teta = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

    # Função para desenhar as linhas do sensor até a leitura
    def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
        x1, y1 = sensor_pos
        x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
        y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
        plt.plot([x1, x2], [y1, y2], color=cor)

# Linhas conectando os sensores aos pontos finais de leitura (amarelas)
desenhar_linha_sensor_leitura(posicao_sensor1, distancia_sensor1)
desenhar_linha_sensor_leitura(posicao_sensor2, distancia_sensor2)
desenhar_linha_sensor_leitura(posicao_sensor3, distancia_sensor3)
desenhar_linha_sensor_leitura(posicao_sensor4, distancia_sensor4)

# Plotando linhas nos eixos x e y
plt.axhline(0, color='blue', linestyle='--', linewidth=1)
plt.axvline(0, color='blue', linestyle='--', linewidth=1)

# Configurando o gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.axis('equal')

# Salvando a imagem na pasta
nome_arquivo = os.path.join(pasta_imagens, 'tora_estimada.png')
plt.savefig(nome_arquivo)

# Exibindo o gráfico
plt.show()

DESILGALDADE MATRICIAL LINEAR LMI
PROGRAMAÇÃO CONVEXA 
SDPA 
SDP


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from datetime import datetime

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])
posicao_sensor2 = np.array([100, 100])
posicao_sensor3 = np.array([100, -100])
posicao_sensor4 = np.array([-100, -100])

# Leituras dos sensores (distâncias da tora)
distancia_sensor1 = 70
distancia_sensor2 = 70
distancia_sensor3 = 70
distancia_sensor4 = 70

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS
resultado = minimize(regressao_circular_LMS, chute_inicial, args=(
    [distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4],
    [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio
centro_estimado = resultado.x[:2]
raio_estimado = resultado.x[2]

# Calculando o diâmetro estimado
diametro_estimado = raio_estimado * 2

# Verificar se o diâmetro está dentro dos limites
if diametro_estimado > 250:
    print("Falha: Diâmetro Excessivo, Descartar tora")
elif diametro_estimado < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte, Descartar tora")

# Calculando o volume da tora em metros cúbicos (m³)
altura_tora = 400  # Altura da tora em centímetros (correspondente a 4 metros)
volume_tora = np.pi * (diametro_estimado / 2) ** 2 * altura_tora / 1000000  # Convertendo para metros cúbicos (m³)

# Criando a pasta para salvar as imagens e o arquivo Excel, se não existirem
pasta_imagens = 'imagens_toras'
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

# Salvando a imagem na pasta com nome único
contador_imagens = len(os.listdir(pasta_imagens)) + 1
nome_arquivo_imagem = os.path.join(pasta_imagens, f'tora_estimada_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores')

# Plotando as distâncias medidas pelos sensores com texto em verde e um pouco afastado dos sensores
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado
plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {diametro_estimado:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada (um círculo)
teta = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

# Linhas conectando os sensores aos pontos finais de leitura (amarelas)
def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
    x1, y1 = sensor_pos
    x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
    y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
    plt.plot([x1, x2], [y1, y2], color=cor)

desenhar_linha_sensor_leitura(posicao_sensor1, distancia_sensor1)
desenhar_linha_sensor_leitura(posicao_sensor2, distancia_sensor2)
desenhar_linha_sensor_leitura(posicao_sensor3, distancia_sensor3)
desenhar_linha_sensor_leitura(posicao_sensor4, distancia_sensor4)

# Plotando linhas nos eixos x e y
plt.axhline(0, color='blue', linestyle='--', linewidth=1)
plt.axvline(0, color='blue', linestyle='--', linewidth=1)

# Configurando o gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Salvando a imagem na pasta com nome único
plt.savefig(nome_arquivo_imagem)

# Exibindo o volume da tora no console
print(f'Volume da Tora: {volume_tora:.2f} m³')
plt.show()

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
from datetime import datetime

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])
posicao_sensor2 = np.array([100, 100])
posicao_sensor3 = np.array([100, -100])
posicao_sensor4 = np.array([-100, -100])

# Leituras dos sensores (distâncias da tora)
distancia_sensor1 = 70
distancia_sensor2 = 60
distancia_sensor3 = 75
distancia_sensor4 = 20

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS
resultado = minimize(regressao_circular_LMS, chute_inicial, args=(
    [distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4],
    [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio
centro_estimado = resultado.x[:2]
raio_estimado = resultado.x[2]

# Calculando o diâmetro estimado
diametro_estimado = raio_estimado * 2

# Verificar se o diâmetro está dentro dos limites
if diametro_estimado > 250:
    print("Falha: Diâmetro Excessivo, Descartar tora")
elif diametro_estimado < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte, Descartar tora")

# Calculando o volume da tora em metros cúbicos (m³)
altura_tora = 400  # Altura da tora em centímetros (correspondente a 4 metros)
volume_tora = np.pi * (diametro_estimado / 2) ** 2 * altura_tora / 1000000  # Convertendo para metros cúbicos (m³)

# Criando a pasta para salvar as imagens e o arquivo Excel, se não existirem
pasta_imagens = 'imagens_toras'
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

# Salvando a imagem na pasta com nome único
contador_imagens = len(os.listdir(pasta_imagens)) + 1
nome_arquivo_imagem = os.path.join(pasta_imagens, f'tora_estimada_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores')

# Plotando as distâncias medidas pelos sensores com texto em verde e um pouco afastado dos sensores
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado
plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {diametro_estimado:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada (um círculo)
teta = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

# Linhas conectando os sensores aos pontos finais de leitura (amarelas)
def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
    x1, y1 = sensor_pos
    x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
    y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
    plt.plot([x1, x2], [y1, y2], color=cor)

desenhar_linha_sensor_leitura(posicao_sensor1, distancia_sensor1)
desenhar_linha_sensor_leitura(posicao_sensor2, distancia_sensor2)
desenhar_linha_sensor_leitura(posicao_sensor3, distancia_sensor3)
desenhar_linha_sensor_leitura(posicao_sensor4, distancia_sensor4)

# Plotando linhas nos eixos x e y
plt.axhline(0, color='blue', linestyle='--', linewidth=1)
plt.axvline(0, color='blue', linestyle='--', linewidth=1)

# Configurando o gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Salvando a imagem na pasta com nome único
plt.savefig(nome_arquivo_imagem)

# Exibindo o volume da tora no console
print(f'Volume da Tora: {volume_tora:.2f} m³')

# Adicionando informações ao arquivo Excel
data_atual = datetime.now().strftime('%Y-%m-%d')  # Data atual no formato YYYY-MM-DD
hora_atual = datetime.now().strftime('%H:%M:%S')  # Hora atual no formato HH:MM:SS
nome_arquivo_excel = 'dados_toras.xlsx'

if os.path.exists(nome_arquivo_excel):
    # Carregando o DataFrame existente do arquivo Excel
    df_existente = pd.read_excel(nome_arquivo_excel)
    # Adicionando uma nova linha com os dados da leitura atual
    quantidade_toras = int(contador_imagens / 3)  # Contabiliza 1 tora a cada 3 leituras
    medição_atual = contador_imagens % 3
    medição_01 = diametro_estimado if medição_atual == 1 else 0
    medição_02 = diametro_estimado if medição_atual == 2 else 0
    medição_03 = diametro_estimado if medição_atual == 0 else 0
    diametro_tora = np.mean([medição_01, medição_02, medição_03]) if medição_atual == 0 else 0
    df_novo = pd.DataFrame({
        "Data": [data_atual],
        "Hora": [hora_atual],
        "Quantidade de Medição": [contador_imagens],
        "Quantidade de Tora": [quantidade_toras],
        "Medição 01": [medição_01],
        "Medição 02": [medição_02],
        "Medição 03": [medição_03],
        "Média Diâmetro Tora": [diametro_tora],
    })
    df_final = pd.concat([df_existente, df_novo], ignore_index=True)
else:
    quantidade_toras = int(contador_imagens / 3)  # Contabiliza 1 tora a cada 3 leituras
    medição_atual = contador_imagens % 3
    medição_01 = diametro_estimado if medição_atual == 1 else 0
    medição_02 = diametro_estimado if medição_atual == 2 else 0
    medição_03 = diametro_estimado if medição_atual == 0 else 0
    diametro_tora = np.mean([medição_01, medição_02, medição_03]) if medição_atual == 0 else 0
    df_final = pd.DataFrame({
        "Data": [data_atual],
        "Hora": [hora_atual],
        "Quantidade de Medição": [contador_imagens],
        "Quantidade de Tora": [quantidade_toras],
        "Medição 01": [medição_01],
        "Medição 02": [medição_02],
        "Medição 03": [medição_03],
        "Média Diâmetro Tora": [diametro_tora],
    })

# Salvando no arquivo Excel
df_final.to_excel(nome_arquivo_excel, index=False)

print("Dados exportados para o arquivo:", nome_arquivo_excel)
plt.show()

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # Importando pandas para trabalhar com DataFrames
from scipy.optimize import minimize
from datetime import datetime

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])  # Sensor 1 (X negativo, Y positivo)
posicao_sensor2 = np.array([100, 100])   # Sensor 2 (X positivo, Y positivo)
posicao_sensor3 = np.array([100, -100])  # Sensor 3 (X positivo, Y negativo)
posicao_sensor4 = np.array([-100, -100]) # Sensor 4 (X negativo, Y negativo)

# Leituras dos sensores (distâncias da tora)
distancia_sensor1 = 70  # Sensor 1
distancia_sensor2 = 50   # Sensor 2
distancia_sensor3 = 70   # Sensor 3
distancia_sensor4 = 20   # Sensor 4

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS
resultado = minimize(regressao_circular_LMS, chute_inicial, args=([distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4], [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio
centro_estimado = resultado.x[:2]
raio_estimado = resultado.x[2]

# Calculando o diâmetro estimado
diametro_estimado = raio_estimado * 2

# Verificar se o diâmetro está dentro dos limites
if diametro_estimado > 250:
    print("Falha: Diâmetro Excessivo, Descartar tora")
elif diametro_estimado < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte, Descartar tora")

# Calculando o volume da tora em metros cúbicos (m³)
altura_tora = 400  # Altura da tora em centímetros (correspondente a 4 metros)
volume_tora = np.pi * (diametro_estimado / 2) ** 2 * altura_tora / 1000000  # Convertendo para metros cúbicos (m³)

# Criando a pasta para salvar as imagens e o arquivo Excel, se não existirem
pasta_imagens = 'imagens_toras'
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

# Salvando a imagem na pasta com nome único
contador_imagens = len(os.listdir(pasta_imagens)) + 1
nome_arquivo_imagem = os.path.join(pasta_imagens, f'tora_estimada_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores')

# Plotando as distâncias medidas pelos sensores com texto em verde e um pouco afastado dos sensores
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado
plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {diametro_estimado:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada (um círculo)
teta = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

# Linhas conectando os sensores aos pontos finais de leitura (amarelas)
def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
    x1, y1 = sensor_pos
    x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
    y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
    plt.plot([x1, x2], [y1, y2], color=cor)

desenhar_linha_sensor_leitura(posicao_sensor1, distancia_sensor1)
desenhar_linha_sensor_leitura(posicao_sensor2, distancia_sensor2)
desenhar_linha_sensor_leitura(posicao_sensor3, distancia_sensor3)
desenhar_linha_sensor_leitura(posicao_sensor4, distancia_sensor4)

# Plotando linhas nos eixos x e y
plt.axhline(0, color='blue', linestyle='--', linewidth=1)
plt.axvline(0, color='blue', linestyle='--', linewidth=1)

# Configurando o gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Salvando a imagem na pasta com nome único
plt.savefig(nome_arquivo_imagem)

# Exibindo o volume da tora no console
print(f'Volume da Tora: {volume_tora:.2f} m³')

# Contabilizando a quantidade de toras e valor da tora
if contador_imagens % 3 == 0:
    quantidade_toras = contador_imagens // 3
    # Criando DataFrame com os dados
    dados = {
        "Data": [datetime.now().strftime("%Y-%m-%d")],
        "Hora": [datetime.now().strftime("%H:%M:%S")],
        "Quantidade de Tora": [quantidade_toras],  # Quantidade de toras
    }
    df = pd.DataFrame(dados)

    # Exportando para Excel
    nome_arquivo_excel = 'Dados_ProdToras.xlsx'
    if os.path.exists(nome_arquivo_excel):
        # Carregando o DataFrame existente do arquivo Excel
        df_existente = pd.read_excel(nome_arquivo_excel)
        # Adicionando uma nova linha com os dados da leitura atual
        df_final = pd.concat([df_existente, df], ignore_index=True)
    else:
        df_final = df  # Se o arquivo não existir, o DataFrame final é o atual

    # Salvando no arquivo Excel
    df_final.to_excel(nome_arquivo_excel, index=False)

    print("Dados exportados para o arquivo:", nome_arquivo_excel)
    
plt.show()


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
from datetime import datetime

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])  # Sensor 1 (X negativo, Y positivo)
posicao_sensor2 = np.array([100, 100])   # Sensor 2 (X positivo, Y positivo)
posicao_sensor3 = np.array([100, -100])  # Sensor 3 (X positivo, Y negativo)
posicao_sensor4 = np.array([-100, -100]) # Sensor 4 (X negativo, Y negativo)

# Mensagem para confirmar a posição inicial da tora
input("Posição inicial da tora, OK para confirmar: ")

# Solicitar os valores de leitura dos sensores na posição inicial
distancia_sensor1_ini = float(input("Digite a distância lida pelo Sensor 1 na posição inicial (cm): "))
distancia_sensor2_ini = float(input("Digite a distância lida pelo Sensor 2 na posição inicial (cm): "))
distancia_sensor3_ini = float(input("Digite a distância lida pelo Sensor 3 na posição inicial (cm): "))
distancia_sensor4_ini = float(input("Digite a distância lida pelo Sensor 4 na posição inicial (cm): "))

# Função de regressão circular usando LMS para a posição inicial
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Chute inicial para os parâmetros: centro e raio na posição inicial
chute_inicial_ini = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS na posição inicial
resultado_ini = minimize(regressao_circular_LMS, chute_inicial_ini, args=([distancia_sensor1_ini, distancia_sensor2_ini, distancia_sensor3_ini, distancia_sensor4_ini], [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio na posição inicial
centro_estimado_ini = resultado_ini.x[:2]
raio_estimado_ini = resultado_ini.x[2]

# Calculando o diâmetro estimado na posição inicial
diametro_estimado_ini = raio_estimado_ini * 2

# Verificar se o diâmetro está dentro dos limites na posição inicial
if diametro_estimado_ini > 250:
    print("Falha: Diâmetro Excessivo na posição inicial, Descartar tora")
elif diametro_estimado_ini < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte na posição inicial, Descartar tora")

# Solicitar a confirmação da posição do meio da tora
input("Posição Meio da Tora, para confirmar OK: ")

# Solicitar os valores de leitura dos sensores na posição do meio
distancia_sensor1_meio = float(input("Digite a distância lida pelo Sensor 1 na posição do meio (cm): "))
distancia_sensor2_meio = float(input("Digite a distância lida pelo Sensor 2 na posição do meio (cm): "))
distancia_sensor3_meio = float(input("Digite a distância lida pelo Sensor 3 na posição do meio (cm): "))
distancia_sensor4_meio = float(input("Digite a distância lida pelo Sensor 4 na posição do meio (cm): "))

# Função de regressão circular usando LMS para a posição do meio
def regressao_circular_LMS_meio(x, distancias_ini, distancias_meio, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d_ini, d_meio, posicao_sensor in zip(distancias_ini, distancias_meio, posicoes_sensores):
        distancia_centro_sensor_ini = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro_ini = distancia_centro_sensor_ini - raio - d_ini
        distancia_centro_sensor_meio = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro_meio = distancia_centro_sensor_meio - raio - d_meio
        soma_erros += (erro_ini ** 2) + (erro_meio ** 2)
    return soma_erros

# Chute inicial para os parâmetros: centro e raio na posição do meio
chute_inicial_meio = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS na posição do meio
resultado_meio = minimize(regressao_circular_LMS_meio, chute_inicial_meio, args=([distancia_sensor1_ini, distancia_sensor2_ini, distancia_sensor3_ini, distancia_sensor4_ini], [distancia_sensor1_meio, distancia_sensor2_meio, distancia_sensor3_meio, distancia_sensor4_meio], [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio na posição do meio
centro_estimado_meio = resultado_meio.x[:2]
raio_estimado_meio = resultado_meio.x[2]

# Calculando o diâmetro estimado na posição do meio
diametro_estimado_meio = raio_estimado_meio * 2

# Verificar se o diâmetro está dentro dos limites na posição do meio
if diametro_estimado_meio > 250:
    print("Falha: Diâmetro Excessivo na posição do meio, Descartar tora")
elif diametro_estimado_meio < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte na posição do meio, Descartar tora")

# Solicitar a confirmação da posição final da tora
input("Posição final da tora, OK para confirmar: ")

# Solicitar os valores de leitura dos sensores na posição final
distancia_sensor1_final = float(input("Digite a distância lida pelo Sensor 1 na posição final (cm): "))
distancia_sensor2_final = float(input("Digite a distância lida pelo Sensor 2 na posição final (cm): "))
distancia_sensor3_final = float(input("Digite a distância lida pelo Sensor 3 na posição final (cm): "))
distancia_sensor4_final = float(input("Digite a distância lida pelo Sensor 4 na posição final (cm): "))

# Função de regressão circular usando LMS para a posição final
def regressao_circular_LMS_final(x, distancias_ini, distancias_meio, distancias_final, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d_ini, d_meio, d_final, posicao_sensor in zip(distancias_ini, distancias_meio, distancias_final, posicoes_sensores):
        distancia_centro_sensor_ini = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro_ini = distancia_centro_sensor_ini - raio - d_ini
        distancia_centro_sensor_meio = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro_meio = distancia_centro_sensor_meio - raio - d_meio
        distancia_centro_sensor_final = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro_final = distancia_centro_sensor_final - raio - d_final
        soma_erros += (erro_ini ** 2) + (erro_meio ** 2) + (erro_final ** 2)
    return soma_erros

# Chute inicial para os parâmetros: centro e raio na posição final
chute_inicial_final = [0, 50, 100]

# Minimizando a função de erro usando o algoritmo LMS na posição final
resultado_final = minimize(regressao_circular_LMS_final, chute_inicial_final, args=([distancia_sensor1_ini, distancia_sensor2_ini, distancia_sensor3_ini, distancia_sensor4_ini], [distancia_sensor1_meio, distancia_sensor2_meio, distancia_sensor3_meio, distancia_sensor4_meio], [distancia_sensor1_final, distancia_sensor2_final, distancia_sensor3_final, distancia_sensor4_final], [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados: centro e raio na posição final
centro_estimado_final = resultado_final.x[:2]
raio_estimado_final = resultado_final.x[2]

# Calculando o diâmetro estimado na posição final
diametro_estimado_final = raio_estimado_final * 2

# Verificar se o diâmetro está dentro dos limites na posição final
if diametro_estimado_final > 250:
    print("Falha: Diâmetro Excessivo na posição final, Descartar tora")
elif diametro_estimado_final < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte na posição final, Descartar tora")

# Calculando o volume da tora em metros cúbicos (m³) na posição inicial
altura_tora_ini = 400  # Altura da tora em centímetros (correspondente a 4 metros)
volume_tora_ini = np.pi * (diametro_estimado_ini / 2) ** 2 * altura_tora_ini / 1000000  # Convertendo para metros cúbicos (m³)

# Calculando o volume da tora em metros cúbicos (m³) na posição do meio
altura_tora_meio = 200  # Altura da tora em centímetros (correspondente a 2 metros)
volume_tora_meio = np.pi * (diametro_estimado_meio / 2) ** 2 * altura_tora_meio / 1000000  # Convertendo para metros cúbicos (m³)

# Calculando o volume da tora em metros cúbicos (m³) na posição final
altura_tora_final = 100  # Altura da tora em centímetros (correspondente a 1 metro)
volume_tora_final = np.pi * (diametro_estimado_final / 2) ** 2 * altura_tora_final / 1000000  # Convertendo para metros cúbicos (m³)

# Criando a pasta para salvar as imagens e o arquivo Excel, se não existirem
pasta_imagens = 'imagens_toras'
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

# Salvando a imagem da posição inicial na pasta com nome único
contador_imagens = len(os.listdir(pasta_imagens)) + 1
nome_arquivo_imagem_ini = os.path.join(pasta_imagens, f'tora_estimada_ini_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico da posição inicial
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores na posição inicial')

# Plotando as distâncias medidas pelos sensores na posição inicial com texto em verde e um pouco afastado dos sensores
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1_ini} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2_ini} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3_ini} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4_ini} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado na posição inicial
plt.text(centro_estimado_ini[0] - raio_estimado_ini, centro_estimado_ini[1], f'Diâmetro: {diametro_estimado_ini:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada na posição inicial (um círculo)
teta_ini = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada_ini = centro_estimado_ini[0] + raio_estimado_ini * np.cos(teta_ini)
y_tora_estimada_ini = centro_estimado_ini[1] + raio_estimado_ini * np.sin(teta_ini)
plt.plot(x_tora_estimada_ini, y_tora_estimada_ini, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada na posição inicial')

# Configurações adicionais do gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Eixo X (cm)')
plt.ylabel('Eixo Y (cm)')
plt.title('Posição Inicial da Tora')
plt.legend()
plt.grid(True)
plt.savefig(nome_arquivo_imagem_ini)
plt.close()

# Salvando a imagem da posição do meio na pasta com nome único
nome_arquivo_imagem_meio = os.path.join(pasta_imagens, f'tora_estimada_meio_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico da posição do meio
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores na posição do meio')

# Plotando as distâncias medidas pelos sensores na posição do meio com texto em verde
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1_meio} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2_meio} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3_meio} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4_meio} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado na posição do meio
plt.text(centro_estimado_meio[0] - raio_estimado_meio, centro_estimado_meio[1], f'Diâmetro: {diametro_estimado_meio:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada na posição do meio (um círculo)
teta_meio = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada_meio = centro_estimado_meio[0] + raio_estimado_meio * np.cos(teta_meio)
y_tora_estimada_meio = centro_estimado_meio[1] + raio_estimado_meio * np.sin(teta_meio)
plt.plot(x_tora_estimada_meio, y_tora_estimada_meio, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada na posição do meio')

# Configurações adicionais do gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Eixo X (cm)')
plt.ylabel('Eixo Y (cm)')
plt.title('Posição do Meio da Tora')
plt.legend()
plt.grid(True)
plt.savefig(nome_arquivo_imagem_meio)
plt.close()

# Salvando a imagem da posição final na pasta com nome único
nome_arquivo_imagem_final = os.path.join(pasta_imagens, f'tora_estimada_final_{contador_imagens}.png')
plt.figure(figsize=(8, 6))

# Plotando o gráfico da posição final
plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
            [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
            color='red', label='Leituras dos Sensores na posição final')

# Plotando as distâncias medidas pelos sensores na posição final com texto em verde
plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancia_sensor1_final} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancia_sensor2_final} cm', fontsize=10, verticalalignment='bottom', color='green')
plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancia_sensor3_final} cm', fontsize=10, verticalalignment='top', color='green')
plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancia_sensor4_final} cm', fontsize=10, verticalalignment='top', color='green')

# Plotando o diâmetro estimado na posição final
plt.text(centro_estimado_final[0] - raio_estimado_final, centro_estimado_final[1], f'Diâmetro: {diametro_estimado_final:.2f} cm', fontsize=10, verticalalignment='top', color='black')

# Plotando a tora estimada na posição final (um círculo)
teta_final = np.linspace(0, 2 * np.pi, 100)
x_tora_estimada_final = centro_estimado_final[0] + raio_estimado_final * np.cos(teta_final)
y_tora_estimada_final = centro_estimado_final[1] + raio_estimado_final * np.sin(teta_final)
plt.plot(x_tora_estimada_final, y_tora_estimada_final, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada na posição final')

# Configurações adicionais do gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Eixo X (cm)')
plt.ylabel('Eixo Y (cm)')
plt.title('Posição Final da Tora')
plt.legend()
plt.grid(True)
plt.savefig(nome_arquivo_imagem_final)
plt.close()

# Salvando os resultados em um arquivo Excel
dados_toras = {
    'Posição': ['Inicial', 'Meio', 'Final'],
    'Diâmetro Estimado (cm)': [diametro_estimado_ini, diametro_estimado_meio, diametro_estimado_final],
    'Volume Estimado (m³)': [volume_tora_ini, volume_tora_meio, volume_tora_final]
}

df_toras = pd.DataFrame(dados_toras)

nome_arquivo_excel = f'dados_toras_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx'
df_toras.to_excel(nome_arquivo_excel, index=False)

print("Processo concluído! Resultados salvos no arquivo Excel e imagens geradas na pasta 'imagens_toras'.")

xxxxxxxxxxxxxxxxxxxxxxxx

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])  # Sensor 1 (X negativo, Y positivo)
posicao_sensor2 = np.array([100, 100])   # Sensor 2 (X positivo, Y positivo)
posicao_sensor3 = np.array([100, -100])  # Sensor 3 (X positivo, Y negativo)
posicao_sensor4 = np.array([-100, -100]) # Sensor 4 (X negativo, Y negativo)

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Função para calcular o volume da tora com base no raio
def calcular_volume(raio, comprimento=400):  # Comprimento padrão de 4 metros em centímetros
    return np.pi * (raio / 2) ** 2 * comprimento / 1000000  # Convertendo para metros cúbicos (m³)

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Leitura dos sensores
def realizar_leitura(posicao_texto):
    input(f"posição {posicao_texto}, OK para confirmar: ")
    distancia_sensor1 = float(input("Digite a leitura do sensor 1 (cm): "))
    distancia_sensor2 = float(input("Digite a leitura do sensor 2 (cm): "))
    distancia_sensor3 = float(input("Digite a leitura do sensor 3 (cm): "))
    distancia_sensor4 = float(input("Digite a leitura do sensor 4 (cm): "))
    return [distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4]

# Leitura da posição de início da tora
distancias_inicio = realizar_leitura("Inicio da Tora")

# Leitura da posição do meio da tora
distancias_meio = realizar_leitura("Meio da Tora")

# Leitura da posição final da tora
distancias_final = realizar_leitura("Final da Tora")

# Minimizando a função de erro usando o algoritmo LMS para cada medição
resultado_inicio = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_inicio, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))
resultado_meio = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_meio, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))
resultado_final = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_final, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados para cada medição: centro e raio
centro_estimado_inicio = resultado_inicio.x[:2]
raio_estimado_inicio = resultado_inicio.x[2]
centro_estimado_meio = resultado_meio.x[:2]
raio_estimado_meio = resultado_meio.x[2]
centro_estimado_final = resultado_final.x[:2]
raio_estimado_final = resultado_final.x[2]

# Calculando o diâmetro estimado para cada medição
diametro_estimado_inicio = raio_estimado_inicio * 2
diametro_estimado_meio = raio_estimado_meio * 2
diametro_estimado_final = raio_estimado_final * 2

# Verificar se os diâmetros estão dentro dos limites
if diametro_estimado_inicio > 250 or diametro_estimado_meio > 250 or diametro_estimado_final > 250:
    print("Falha: Diâmetro Excessivo, Descartar tora")
elif diametro_estimado_inicio < 10 or diametro_estimado_meio < 10 or diametro_estimado_final < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte, Descartar tora")
else:
    # Calculando a média dos diâmetros
    diametro_medio = (diametro_estimado_inicio + diametro_estimado_meio + diametro_estimado_final) / 3

    # Calculando o volume da tora em metros cúbicos (m³) com base no diâmetro médio e comprimento de 4 metros
    volume_tora_medio = calcular_volume(diametro_medio)

    # Plotando os gráficos para cada medição
    def plotar_grafico(distancias, centro_estimado, raio_estimado, nome_arquivo_imagem):
        plt.figure(figsize=(8, 6))
        plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
                    [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
                    color='red', label='Leituras dos Sensores')

        plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancias[0]} cm', fontsize=10, verticalalignment='bottom', color='green')
        plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancias[1]} cm', fontsize=10, verticalalignment='bottom', color='green')
        plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancias[2]} cm', fontsize=10, verticalalignment='top', color='green')
        plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancias[3]} cm', fontsize=10, verticalalignment='top', color='green')

        plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {raio_estimado * 2:.2f} cm', fontsize=10, verticalalignment='top', color='black')

        teta = np.linspace(0, 2 * np.pi, 100)
        x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
        y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
        plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

        def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
            x1, y1 = sensor_pos
            x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
            y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
            plt.plot([x1, x2], [y1, y2], color=cor)

        desenhar_linha_sensor_leitura(posicao_sensor1, distancias[0])
        desenhar_linha_sensor_leitura(posicao_sensor2, distancias[1])
        desenhar_linha_sensor_leitura(posicao_sensor3, distancias[2])
        desenhar_linha_sensor_leitura(posicao_sensor4, distancias[3])

        plt.axhline(0, color='blue', linestyle='--', linewidth=1)
        plt.axvline(0, color='blue', linestyle='--', linewidth=1)

        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.savefig(nome_arquivo_imagem)
        plt.show()

    # Salvando as imagens na pasta com nome único
    pasta_imagens = 'imagens_toras'
    if not os.path.exists(pasta_imagens):
        os.makedirs(pasta_imagens)

    contador_imagens = len(os.listdir(pasta_imagens)) + 1
    nome_arquivo_imagem_inicio = os.path.join(pasta_imagens, f'tora_inicio_{contador_imagens}.png')
    nome_arquivo_imagem_meio = os.path.join(pasta_imagens, f'tora_meio_{contador_imagens}.png')
    nome_arquivo_imagem_final = os.path.join(pasta_imagens, f'tora_final_{contador_imagens}.png')

    plotar_grafico(distancias_inicio, centro_estimado_inicio, raio_estimado_inicio, nome_arquivo_imagem_inicio)
    plotar_grafico(distancias_meio, centro_estimado_meio, raio_estimado_meio, nome_arquivo_imagem_meio)
    plotar_grafico(distancias_final, centro_estimado_final, raio_estimado_final, nome_arquivo_imagem_final)

    # Exibindo o volume e diâmetro da tora no console
    print(f'Diâmetro da Tora no Início: {diametro_estimado_inicio:.2f} cm')
    print(f'Diâmetro da Tora no Meio: {diametro_estimado_meio:.2f} cm')
    print(f'Diâmetro da Tora no Final: {diametro_estimado_final:.2f} cm')
    print(f'Diâmetro Médio da Tora: {diametro_medio:.2f} cm')
    print(f'Volume da Tora: {volume_tora_medio:.2f} m³')




    xxxxxxxxxxxxxxxxxxxxxxxxxx



    import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date
from scipy.optimize import minimize

# Definir um contador global para a quantidade de toras
contador_toras = 0

# Posições dos sensores
posicao_sensor1 = np.array([-100, 100])  # Sensor 1 (X negativo, Y positivo)
posicao_sensor2 = np.array([100, 100])   # Sensor 2 (X positivo, Y positivo)
posicao_sensor3 = np.array([100, -100])  # Sensor 3 (X positivo, Y negativo)
posicao_sensor4 = np.array([-100, -100]) # Sensor 4 (X negativo, Y negativo)

# Função de regressão circular usando LMS
def regressao_circular_LMS(x, distancias, posicoes_sensores):
    centro_x, centro_y, raio = x
    soma_erros = 0
    for d, posicao_sensor in zip(distancias, posicoes_sensores):
        distancia_centro_sensor = np.linalg.norm(posicao_sensor - np.array([centro_x, centro_y]))
        erro = distancia_centro_sensor - raio - d
        soma_erros += erro ** 2
    return soma_erros

# Função para calcular o volume da tora com base no raio
def calcular_volume(raio, comprimento=400):  # Comprimento padrão de 4 metros em centímetros
    return np.pi * (raio / 2) ** 2 * comprimento / 1000000  # Convertendo para metros cúbicos (m³)

# Chute inicial para os parâmetros: centro e raio
chute_inicial = [0, 50, 100]

# Leitura dos sensores
def realizar_leitura(posicao_texto):
    input(f"posição {posicao_texto}, OK para confirmar: ")
    distancia_sensor1 = float(input("Digite a leitura do sensor 1 (cm): "))
    distancia_sensor2 = float(input("Digite a leitura do sensor 2 (cm): "))
    distancia_sensor3 = float(input("Digite a leitura do sensor 3 (cm): "))
    distancia_sensor4 = float(input("Digite a leitura do sensor 4 (cm): "))
    return [distancia_sensor1, distancia_sensor2, distancia_sensor3, distancia_sensor4]

# Função para exportar os dados para Excel
def exportar_para_excel(df):
    global contador_toras  # Acessar a variável global contador_toras
    # Obter a data atual
    data_atual = date.today().strftime("%Y-%m-%d")
    
    # Criar o nome do arquivo Excel com base na data
    nome_arquivo_excel = f'{data_atual}_DadosProd.xlsx'

    # Verificar se o arquivo Excel já existe
    if os.path.exists(nome_arquivo_excel):
        # Carregar o arquivo existente e adicionar os novos dados
        df_existente = pd.read_excel(nome_arquivo_excel)
        df_final = pd.concat([df_existente, df], ignore_index=True)
    else:
        df_final = df

    # Salvar o DataFrame no arquivo Excel
    df_final.to_excel(nome_arquivo_excel, index=False)

# Leitura da posição de início da tora
distancias_inicio = realizar_leitura("Inicio da Tora")

# Leitura da posição do meio da tora
distancias_meio = realizar_leitura("Meio da Tora")

# Leitura da posição final da tora
distancias_final = realizar_leitura("Final da Tora")

# Minimizando a função de erro usando o algoritmo LMS para cada medição
resultado_inicio = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_inicio, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))
resultado_meio = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_meio, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))
resultado_final = minimize(regressao_circular_LMS, chute_inicial, args=(distancias_final, [posicao_sensor1, posicao_sensor2, posicao_sensor3, posicao_sensor4]))

# Obtendo os parâmetros estimados para cada medição: centro e raio
centro_estimado_inicio = resultado_inicio.x[:2]
raio_estimado_inicio = resultado_inicio.x[2]
centro_estimado_meio = resultado_meio.x[:2]
raio_estimado_meio = resultado_meio.x[2]
centro_estimado_final = resultado_final.x[:2]
raio_estimado_final = resultado_final.x[2]

# Calculando o diâmetro estimado para cada medição
diametro_estimado_inicio = raio_estimado_inicio * 2
diametro_estimado_meio = raio_estimado_meio * 2
diametro_estimado_final = raio_estimado_final * 2

# Verificar se os diâmetros estão dentro dos limites
if diametro_estimado_inicio > 250 or diametro_estimado_meio > 250 or diametro_estimado_final > 250:
    print("Falha: Diâmetro Excessivo, Descartar tora")
elif diametro_estimado_inicio < 10 or diametro_estimado_meio < 10 or diametro_estimado_final < 10:
    print("Falha: Diâmetro menor que os parâmetros de corte, Descartar tora")
else:
    # Incrementar o contador de toras apenas quando todas as leituras são feitas
    contador_toras += 1

    # Obtendo a data atual para criar a pasta
    data_atual = date.today().strftime("%Y-%m-%d")

    # Criando o nome da pasta com base na data
    pasta_imagens = f'{data_atual}_ImagensToras'

    # Verificando se a pasta já existe, caso contrário, criando-a
    if not os.path.exists(pasta_imagens):
        os.makedirs(pasta_imagens)

    # Salvando as imagens na pasta com nome único
    contador_imagens = len(os.listdir(pasta_imagens)) + 3
    nome_arquivo_imagem_inicio = os.path.join(pasta_imagens, f'tora_inicio_{contador_imagens / 3}.png')
    nome_arquivo_imagem_meio = os.path.join(pasta_imagens, f'tora_meio_{contador_imagens / 3}.png')
    nome_arquivo_imagem_final = os.path.join(pasta_imagens, f'tora_final_{contador_imagens/ 3}.png')

    contador_tora = contador_imagens / 3

    # Plotando os gráficos para cada medição
    def plotar_grafico(distancias, centro_estimado, raio_estimado, nome_arquivo_imagem):
        plt.figure(figsize=(8, 6))
        plt.scatter([posicao_sensor1[0], posicao_sensor2[0], posicao_sensor3[0], posicao_sensor4[0]],
                    [posicao_sensor1[1], posicao_sensor2[1], posicao_sensor3[1], posicao_sensor4[1]],
                    color='red', label='Leituras dos Sensores')

        plt.text(posicao_sensor1[0] + 5, posicao_sensor1[1] - 5, f'{distancias[0]} cm', fontsize=10, verticalalignment='bottom', color='green')
        plt.text(posicao_sensor2[0] + 5, posicao_sensor2[1] - 5, f'{distancias[1]} cm', fontsize=10, verticalalignment='bottom', color='green')
        plt.text(posicao_sensor3[0] + 5, posicao_sensor3[1] + 5, f'{distancias[2]} cm', fontsize=10, verticalalignment='top', color='green')
        plt.text(posicao_sensor4[0] + 5, posicao_sensor4[1] + 5, f'{distancias[3]} cm', fontsize=10, verticalalignment='top', color='green')

        plt.text(centro_estimado[0] - raio_estimado, centro_estimado[1], f'Diâmetro: {raio_estimado * 2:.2f} cm', fontsize=10, verticalalignment='top', color='black')

        teta = np.linspace(0, 2 * np.pi, 100)
        x_tora_estimada = centro_estimado[0] + raio_estimado * np.cos(teta)
        y_tora_estimada = centro_estimado[1] + raio_estimado * np.sin(teta)
        plt.plot(x_tora_estimada, y_tora_estimada, color='#8B4513', linestyle='-', linewidth=3, label='Tora Estimada')

        def desenhar_linha_sensor_leitura(sensor_pos, leitura_dist, cor='yellow'):
            x1, y1 = sensor_pos
            x2 = sensor_pos[0] + leitura_dist * (centro_estimado[0] - sensor_pos[0]) / np.linalg.norm(centro_estimado - sensor_pos)
            y2 = sensor_pos[1] + leitura_dist * (centro_estimado[1] - sensor_pos[1]) / np.linalg.norm(centro_estimado - sensor_pos)
            plt.plot([x1, x2], [y1, y2], color=cor)

        desenhar_linha_sensor_leitura(posicao_sensor1, distancias[0])
        desenhar_linha_sensor_leitura(posicao_sensor2, distancias[1])
        desenhar_linha_sensor_leitura(posicao_sensor3, distancias[2])
        desenhar_linha_sensor_leitura(posicao_sensor4, distancias[3])

        plt.axhline(0, color='blue', linestyle='--', linewidth=1)
        plt.axvline(0, color='blue', linestyle='--', linewidth=1)

        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Scanner de Leitura de Toras com Sensores a Laser (LMS)')
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.savefig(nome_arquivo_imagem)
        plt.show()

    plotar_grafico(distancias_inicio, centro_estimado_inicio, raio_estimado_inicio, nome_arquivo_imagem_inicio)
    plotar_grafico(distancias_meio, centro_estimado_meio, raio_estimado_meio, nome_arquivo_imagem_meio)
    plotar_grafico(distancias_final, centro_estimado_final, raio_estimado_final, nome_arquivo_imagem_final)

    # Criar um DataFrame com os dados
    dados = {
        'Data': [data_atual],
        'Hora': [datetime.now().strftime("%H:%M:%S")],
        'Quantidade de Tora': [contador_tora]
    }
    df = pd.DataFrame(dados)

    # Adicionar a chamada da função para exportar para Excel
    exportar_para_excel(df)

    # Calculando a média dos diâmetros
    diametro_medio = (diametro_estimado_inicio + diametro_estimado_meio + diametro_estimado_final) / 3

    # Calculando o volume da tora em metros cúbicos (m³) com base no diâmetro médio e comprimento de 4 metros
    volume_tora_medio = calcular_volume(diametro_medio)

    # Exibindo o volume e diâmetro da tora no console
    print(f'Diâmetro da Tora no Início: {diametro_estimado_inicio:.2f} cm')
    print(f'Diâmetro da Tora no Meio: {diametro_estimado_meio:.2f} cm')
    print(f'Diâmetro da Tora no Final: {diametro_estimado_final:.2f} cm')
    print(f'Diâmetro Médio da Tora: {diametro_medio:.2f} cm')
    print(f'Volume da Tora: {volume_tora_medio:.2f} m³')

xxxxxxxxxxxxxxxxxxxxxxxx

import pandas as pd
import streamlit as st
from datetime import date



# Definir a configuração da página
st.set_page_config(layout="wide")

# Permitir que o usuário selecione a data desejada
data_selecionada = st.date_input("Selecione a data desejada:", date.today(), min_value=date(2020, 1, 1), max_value=date.today())

# Transformar a data selecionada em uma string no formato 'YYYY-MM-DD'
data_formatada = data_selecionada.strftime("%Y-%m-%d")

# Construir o nome do arquivo correspondente à data selecionada
arquivo_selecionado = f"{data_formatada}_DadosProd.xlsx"

try:
    # Carregar os dados do arquivo Excel selecionado
    df = pd.read_excel(arquivo_selecionado)

    # Certifique-se de que 'Date' (ou 'Data') é uma coluna de data
    if 'Date' in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    elif 'Data' in df.columns:
        df["Date"] = pd.to_datetime(df["Data"])
    else:
        st.error("A coluna de data não foi encontrada no DataFrame.")

    # Remover a última coluna 'Date' da tabela
    if 'Date' in df.columns:
        df = df.drop(columns=['Date'])

    # Iniciar o aplicativo Streamlit
    st.title("Meu Dashboard")

    # Adicionar um dataframe ao dashboard (exibindo as primeiras linhas)
    st.write("Dados do DataFrame:")
    st.write(df.head())
except FileNotFoundError:
    st.error(f"Nenhum arquivo de dados encontrado para a data {data_formatada}.")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
