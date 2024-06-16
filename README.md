# About this project

This project consist of two scripts:

### calcular_distancias.py

Taking as input an Excel file with columns c1 and c2 corresponding to two 
geographical points and another excel containing the coordinates of each point, 
calculates the distance between points for each Excel row.

### generar_combinaciones.py

Given a list of geographical points, return all the edges of a fully connected graph with their distance.

# Instructions to run scripts

## 1- Install dependencies

Run:

    pip install -r requirements.txt

## 2 - Create input files (or use sample data)

### Files for calcular_distancias.py

#### 1 - Coordinates dict file
Excel containing columns:
* **c:** geographical point name (i.e. city name)
* **lat:** latitude
* **long:** longitude

#### 2 - Graph edges file
Excel containing columns:
* **c1:** node a name in dict file
* **c2:** node b name in dict file

Each row represents a connection between two geographical points.

### Files for generar_combinaciones.py

#### 1 - Coordinates dict file
(same as in previous script)

#### 2 - Nodes list
Excel containing column:
* **c:** name of the nodes

## 3 - Run scripts

