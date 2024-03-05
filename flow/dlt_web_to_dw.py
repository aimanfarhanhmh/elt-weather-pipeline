import dlt
import duckdb
import pandas as pd
from dlt.sources.helpers import requests
#from prefect import flow, task


#@task(log_prints=True)
def api_fetch_data(url: str):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    for lines in response.json():
        yield lines

#@task(log_prints=True)
def create_pipeline(url):

    pipeline = dlt.pipeline(pipeline_name='forecast_pipeline', 
                            destination='duckdb', 
                            dataset_name='weather_data')
    
    return pipeline.run(api_fetch_data(url),
                        primary_key=("location__location_id","date"), 
                        table_name="forecast", 
                        write_disposition="merge")

#@flow()
def elt_main_flow():

    API_URL = 'https://api.data.gov.my/weather/forecast'
    info = create_pipeline(API_URL)
    print(info)

if __name__ == '__main__':
    elt_main_flow()