#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objs as go
import psycopg2
from sqlalchemy import create_engine


# In[2]:


# Conectarse a la base de datos
conn = psycopg2.connect(
                        database="Prueba",
                        user='postgres', 
                        password='Leo1993+', 
                        host='127.0.0.1', 
                        port= '5432'
)

# Obtener los datos necesarios de la base de datos
cursor = conn.cursor()

# Total de canciones
cursor.execute("SELECT COUNT(*) FROM canciones")
total_canciones = cursor.fetchone()[0]

# Total de artistas
cursor.execute("SELECT COUNT(*) FROM artistas")
total_artistas = cursor.fetchone()[0]

# Artistas más populares
cursor.execute("""
    SELECT c.id_artists, COUNT(*) AS reproducciones
    FROM canciones c
    GROUP BY c.id_artists
    ORDER BY reproducciones DESC
    LIMIT 10
""")
artistas_populares = cursor.fetchall()

# Géneros más populares
cursor.execute("""

    SELECT d.genres, COUNT(*) AS reproducciones
    FROM generos d
    GROUP BY d.genres
    ORDER BY reproducciones DESC
    LIMIT 10
    
""")
generos_populares = cursor.fetchall()

# Crear las gráficas
grafica_artistas = go.Bar(
    x=[row[0] for row in artistas_populares],
    y=[row[1] for row in artistas_populares],
    name="Artistas populares"
)

grafica_generos = go.Bar(
    x=[row[0] for row in generos_populares],
    y=[row[1] for row in generos_populares],
    name="Géneros populares"
)

# Crear el dashboard
dashboard = go.Figure(
    data=[grafica_artistas, grafica_generos],
    layout=go.Layout(
        title="Estado actual de la plataforma",
        xaxis=dict(title="Nombre"),
        yaxis=dict(title="Reproducciones")
    )
)

# Mostrar el dashboard
dashboard.show()


# In[ ]:




