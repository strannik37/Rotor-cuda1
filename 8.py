import subprocess

# Базовая команда
base_command = './clientRotorCudaX64 -prog Rotor -d {device_ids} -name Vast3090{gpu_id} -pass x -pool 213.242.45.187:8000 -b 256,256 -nopow'

# Список процессов
processes = []

# Запуск программы для каждого GPU от 0 до 13
for i in range(8):
    # Форматирование команды с учетом индекса GPU
    command = base_command.format(device_ids=i, gpu_id=i)
    # Запускаем процесс и добавляем его в список
    processes.append(subprocess.Popen(command, shell=True))

# Ожидание завершения всех процессов
for proc in processes:
    proc.wait()
