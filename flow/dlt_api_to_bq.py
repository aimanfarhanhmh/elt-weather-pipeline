import dlt
import pandas as pd
from dlt.sources.helpers import requests
from prefect import flow, task

@task(log_prints=True)
@dlt.resource(table_name="forecast",
              write_disposition="merge",
              primary_key=("location__location_id","date"))
def api_fetch_data(url: str):
    '''Fetches response from API and parses json by line'''

    response = requests.get(url, stream=True)
    response.raise_for_status()

    for lines in response.json():
        yield lines

@flow(log_prints=True)
def create_pipeline(url):
    '''Creates and run dlt pipeline to ingest data from source (API) to destination (Data Warehouse)'''
    pipeline = dlt.pipeline(pipeline_name='forecast_pipeline', 
                            destination='bigquery',
                            dataset_name='weather_data')
    
    return pipeline.run(api_fetch_data(url),
                        loader_file_format='parquet')

@flow()
def elt_main_flow():

    API_URL = 'https://api.data.gov.my/weather/forecast'
    info = create_pipeline(API_URL)
    print(info)

if __name__ == '__main__':
    elt_main_flow()