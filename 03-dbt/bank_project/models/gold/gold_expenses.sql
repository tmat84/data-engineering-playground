{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'gold',
    alias = 'expenses'
)
}}


with expense_time as
(select 
extract(year from "data_księgowania") as year, 
extract(month from "data_księgowania") as month,
"data_księgowania",
"kwota_operacji",
"tytułem"
from {{ref('silver_expenses')}}
)


select year,month,sum("kwota_operacji") as total
from expense_time
Group by year,month
