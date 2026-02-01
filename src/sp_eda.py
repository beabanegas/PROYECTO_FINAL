import pandas as pd
pd.set_option("display.max_columns", None)


def eda_preliminar (df):
    
    display(df.sample(5))
    
    print ('------------')
    print('DIMENSIONES')
    print(f'Nuestro conjunto de datos presenta un conjunto de datos de {df.shape[0]} filas y {df.shape[1]} columnas')

    print ('------------')
    print('INFO')
    display(df.info())

    print ('------------')
    print('REVISIÓN NULOS')
    display (df.isnull().mean()*100)

    print ('------------')
    print('REVISIÓN DUPLICADOS')
    print (F'Tenemos un total de {df.duplicated().sum()} duplicados')

    print ('------------')
    print('FRECUENCAS CATEGÓRICAS')
    for col in df.select_dtypes(include='object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print ('-------')