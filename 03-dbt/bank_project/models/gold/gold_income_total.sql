{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'gold',
    alias = 'income_total'
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

select year,month,sum("kwota_operacji") as total
from income_time
Group by year,month
