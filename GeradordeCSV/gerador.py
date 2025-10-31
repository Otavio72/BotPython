import csv
import os
import random
import uuid

# --- CONFIGURAÇÕES ---
n_arquivos = 100    # Quantos CSVs criar
n_linhas =  500     # Quantas voltas (linhas) por arquivo
pasta_saida = r"C:\Users\otavi\OneDrive\Área de Trabalho\COMPUTADOR\PROJETOS\BOTpython\CSV"

# --- POSSÍVEIS VALORES FIXOS / ALEATÓRIOS ---
carros = [
    "ks_audi_r8_lms", "ks_ferrari_488_gt3", "ks_porsche_911_gt3_r", "ks_bmw_m4_gt3", "ks_mercedes_amg_gt3"
]
pistas = [
    "mugello", "monza", "nurburgring", "spa", "vallelunga", "brands_hatch","silverstone",
    "laguna_seca"
]
gears = [1, 2, 3, 4, 5, 6]
lap_flags = [0, 1]
valid_bins = [0, 1]

# --- GARANTE QUE A PASTA EXISTE ---
os.makedirs(pasta_saida, exist_ok=True)

# --- CABEÇALHO (EXATO DO ARQUIVO ORIGINAL) ---
colunas = [
    "carId", "trackId", "trackLength", "lapIndex", "lapNum", "lapFlag", "binIndex", "validBin",
    "lap_time", "world_position_X", "world_position_Y", "world_position_Z",
    "world_right_X", "world_right_Y", "world_right_Z",
    "velocity_X", "velocity_Y", "velocity_Z",
    "gforce_Y", "race_position", "throttle", "brake", "steering", "gear", "rpm"
]

# --- FUNÇÃO PARA GERAR UMA LINHA ALEATÓRIA ---
def gerar_linha(car, track, track_length):
    lap_index = random.randint(0, 10)
    lap_num = random.randint(0, 50)
    lap_flag = random.choice(lap_flags)
    bin_index = random.randint(0, 100)
    valid_bin = random.choice(valid_bins)
    lap_time = round(random.uniform(60, 180), 3)
    world_pos = [round(random.uniform(-500, 500), 6) for _ in range(3)]
    world_right = [round(random.uniform(-1, 1), 7) for _ in range(3)]
    velocity = [round(random.uniform(-50, 300), 5) for _ in range(3)]
    gforce_y = round(random.uniform(-3, 3), 5)
    race_position = random.randint(1, 24)
    throttle = round(random.uniform(0, 1), 6)
    brake = round(random.uniform(0, 1), 6)
    steering = round(random.uniform(-1, 1), 6)
    gear = random.choice(gears)
    rpm = random.randint(1000, 9000)

    return [
        car, track, track_length, lap_index, lap_num, lap_flag, bin_index, valid_bin,
        lap_time, *world_pos, *world_right, *velocity, gforce_y, race_position,
        throttle, brake, steering, gear, rpm
    ]

# --- GERAR OS ARQUIVOS ---
for i in range(n_arquivos):
    car = random.choice(carros)
    track = random.choice(pistas)
    track_length = round(random.uniform(1500, 7000), 2)

    nome_arquivo = f"{pasta_saida}/{track}_{uuid.uuid4().hex[:6]}.csv"

    with open(nome_arquivo, mode="w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(colunas)
        for _ in range(n_linhas):
            writer.writerow(gerar_linha(car, track, track_length))

    print(f"✅ Gerado: {nome_arquivo}")

print("\nTodos os arquivos foram gerados no mesmo formato do original!")
