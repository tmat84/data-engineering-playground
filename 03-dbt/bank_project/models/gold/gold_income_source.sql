{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'gold',
    alias = 'income_source'
)
}}


with income_time as
(select 
extract(year from "data_księgowania") as year, 
extract(month from "data_księgowania") as month,
"data_księgowania",
"kwota_operacji",
"tytułem",
"company"
from {{ref('silver_income')}}
)

select 
    year,
    month,
    "company" as source,
    sum("kwota_operacji") over(partition by year order by year) as total_year_income,
    sum("kwota_operacji") over(partition by year,month,company order by year,month) as total_year_mounth_income,
    sum("kwota_operacji") over() as total_income
from income_time

