import pandas

def model(dbt, session):
    dbt.config(
        materialized = 'table',
        packages = ['pandas'],
        schema = 'testing'
    )
    
    df = dbt.ref('retail_categories')
    
    return df