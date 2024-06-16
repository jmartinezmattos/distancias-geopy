import geopy.distance
import pandas as pd

if __name__ == '__main__':

    path_arcos = 'florida_arcos.xlsx'

    coordenadas = pd.read_excel('diccionario_coordenadas.xlsx')
    ciudades = pd.read_excel(path_arcos)

    ciudades['dist'] = 0.0

    coordenadas['c'] = coordenadas['c'].str.lower()
    coordenadas['c'] = coordenadas['c'].str.strip()
    coordenadas['c'] = coordenadas['c'].str.replace(' ', '_')

    ciudades['c1'] = ciudades['c1'].str.lower()
    ciudades['c1'] = ciudades['c1'].str.strip()
    ciudades['c1'] = ciudades['c1'].str.replace(' ', '_')

    ciudades['c2'] = ciudades['c2'].str.lower()
    ciudades['c2'] = ciudades['c2'].str.strip()
    ciudades['c2'] = ciudades['c2'].str.replace(' ', '_')

    for index, row in ciudades.iterrows():

        c1 = row['c1']
        c2 = row['c2']

        print(f'c1: {c1}, c2: {c2}')
        lat_c1 = coordenadas.loc[coordenadas['c'] == c1, 'lat'].values[0]
        long_c1 = coordenadas.loc[coordenadas['c'] == c1, 'long'].values[0]

        coords_1 = (lat_c1, long_c1)

        lat_c2 = coordenadas.loc[coordenadas['c'] == c2, 'lat'].values[0]
        long_c2 = coordenadas.loc[coordenadas['c'] == c2, 'long'].values[0]

        coords_2 = (lat_c2, long_c2)

        dist = geopy.distance.distance(coords_1, coords_2).km

        dist = round(dist, 2)

        ciudades.at[index, 'dist'] = dist

    print(ciudades.head())

    ciudades.to_excel(f'{path_arcos.split('.')[0]}_con_distancia.xlsx', index=False)



