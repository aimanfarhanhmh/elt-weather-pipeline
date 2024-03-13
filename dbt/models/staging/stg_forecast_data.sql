{{config(materialized='view')}}

with source as (
    select * from {{source('staging', 'forecast')}}
),

renamed as (
    select
        {{dbt_utils.generate_surrogate_key(['date','location__location_id'])}} as forecastid,
        date as datetime,
        location__location_id as location_id,
        location__location_name as location_name,
        morning_forecast,
        afternoon_forecast,
        night_forecast,
        summary_forecast,
        summary_when,
        min_temp,
        max_temp
    from source
)

select * from renamed



