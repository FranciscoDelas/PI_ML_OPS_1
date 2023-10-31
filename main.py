from fastapi import FastAPI

app= FastAPI()

#http://127.0.0.1:8000

@app.get("/")
def index():
    return "hola"

@app.get("/Funcion01/{desarrollador}")
def developer(desarrollador):
    import pandas as pd
    from tabulate import tabulate
    dfgame = pd.read_csv('df_Funcion1.csv')
    # Filtra el DataFrame para obtener los datos del desarrollador especificado
    dfgame_filtered = dfgame[dfgame['developer'] == desarrollador]

    # Agrupa por año y calcula la cantidad de ítems y el porcentaje de contenido gratuito
    result = dfgame_filtered.groupby('year').agg(
        Cantidad_de_Items=('developer', 'count'),
        Contenido_Free_porcentual =('price', lambda x: (x.astype(str).str.contains('Free', case=False, regex=False).sum()) / len(x) * 100)
).reset_index()

    # Convertir los resultados a formato tabular
    table = tabulate(result, headers='keys', tablefmt='psql')

    # Devolver la representación de tabla como respuesta
    return table

@app.get("/Funcion02/{user_id}")
def userdata(user_id: str):
    import pandas as pd
    df_merged_grouped = pd.read_csv('df_Funcion2.csv')

    if user_id in df_merged_grouped['user_id'].values:
        row = df_merged_grouped[df_merged_grouped['user_id'] == user_id]
        dinero_gastado = row['total_spent'].values[0]
        recomendacion = row['percent_recommended'].values[0]
        cantidad_items = row['total_items_played'].values[0]

        return {
            "Usuario": user_id,
            "Dinero gastado": f"{dinero_gastado:.2f} USD",
            "porcentaje de recomendación": f"{recomendacion:.2f}%",
            "Cantidad de items": cantidad_items
        }
    else:
        return f"El usuario con ID {user_id} no se encuentra en la base de datos."


@app.get("/sistema_recomendacion_item_item/{id_producto}")
def recomendacion_juego(id_producto:int):
    import pandas as pd
    from sklearn.metrics.pairwise import cosine_similarity
    # Cargar el DataFrame desde el archivo CSV
    df = pd.read_csv('df_SistemaRecomendacion2.csv')
    num_recomendaciones=5
    
    # Calcula la similitud de coseno entre juegos
    features = df[['recommend', 'sentiment_analysis'] + list(df.columns[df.columns.str.startswith('genres_')])]
    similarities = cosine_similarity(features)
    
    # Mapea los índices de los juegos a sus nombres (item_id)
    index_to_item = {i: item_id for i, item_id in enumerate(df['item_id'])}
    
    # Encuentra el índice del juego dado su ID
    juego_index = df[df['item_id'] == id_producto].index[0]
    
    # Obtiene las similitudes de coseno del juego con otros juegos
    juego_similarities = similarities[juego_index]
    
    # Encuentra los índices de los juegos más similares (excluyendo el propio juego)
    juegos_similares_indices = juego_similarities.argsort()[-num_recomendaciones-1:-1][::-1]
    
    # Obtiene los nombres de los juegos recomendados
    juegos_recomendados = [index_to_item[i] for i in juegos_similares_indices]
    
    return juegos_recomendados