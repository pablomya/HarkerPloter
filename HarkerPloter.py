import matplotlib.pyplot as plt
import pandas as pd
import os

file_path = 'input_oxides.txt'
delimiter = '\t'
data = pd.read_csv(file_path, delimiter=delimiter)

print(data.head())

output_directory = 'diagramas_harker'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

other_oxides = [oxide for oxide in data.columns[1:] if oxide != 'SiO2']

for oxide in other_oxides:
    plt.figure()
    plt.scatter(data['SiO2'], data[oxide])
    plt.xlabel('SiO2 (wt%)')
    plt.ylabel(f'{oxide} (wt%)')
    #plt.title(f'Diagrama Harker: SiO2 vs {oxide}')
    # EN CASO DE QUERER AGREGAR UN TÍTULO A CADA DIAGRAMA, BORRAR EL "#" DE LA LÍNEA 22 Y ASIGNAR UN TÍTULO
    
    output_file = os.path.join(output_directory, f'SiO2_vs_{oxide}_harker.png')
    plt.savefig(output_file)
    plt.close()

print('Los diagramas Harker han sido guardados en el directorio:', output_directory)
