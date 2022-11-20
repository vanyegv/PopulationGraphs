from utils    import population_by_country  as population_by_country
from read_csv import read_csv               as read_csv
from charts   import generate_bar_chart     as generate_bar_chart
from charts   import generate_pie_chart     as generate_pie_chart

def bar():
    # Ingreso de usuario
    country = input('\tIngresa el pais\n    =>    ') 
    try:                
        # Lectura del archivo
        data=read_csv('./data.csv')                     
        # Filtro por pais
        dict_country = population_by_country(data,country.capitalize())  
        # Selección de las columnas con terminación 'Population'
        keys = [key for key in dict_country[0].keys() if key.endswith('Population')] 
        # Extracción de los años respecto de cada columna
        years = [key[0:4] for key in keys] 
        # Retorno de valores por cada columna en el resultado del pais
        values = [ int(dict(dict_country[0].items())[key]) for key in keys ]     
        # Generación de la grafica
        generate_bar_chart(years,values)
    except IndexError as error:
        print('\tOpción no valida.')
        bar()
        

def pie():
    # Filtra por región
    region = input('\tIntroduce una región\nSouth America\tNorth America\tAsia\tAfrica\tEurope\n    =>    ').capitalize()
    # Lectura del archivo
    data=read_csv('./data.csv')
    # Filtrado por región seleccinada
    data = list(filter(lambda item:item['Continent'] == region,data))
    if len(data) == 0:
        print('\tOpción no válida')
        pie()
    # Filtrado de los nombres de naciones
    country = [ data[i]['Country/Territory'] for i in range(0,len(data)) ]
    # Filtrado de los porcentajes de cada nación
    percentage_by_country = [ data[i]['World Population Percentage'] for i in range(0,len(data)) ]
    # Generación del grafico
    generate_pie_chart(country,percentage_by_country)


    
if __name__ == '__main__':
    # Pide al usuario la seleción del tipo de grafico
    selection = input('\tSelecciona el tipo de grafico \n\tBar chart\tPie chart\n    =>    ').lower()
    # Comprobación de la selección que contenga las palabras clave
    if ('bar' in selection) and ('pie' in selection):
        raise Exception('\tSelección no valida')
    if 'bar' in selection:
        bar()
    if 'pie' in selection:
        pie()
    