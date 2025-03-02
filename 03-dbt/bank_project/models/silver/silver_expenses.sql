{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'silver',
    alias = 'expenses'
)
}}

select *
from {{ref('bronze_posting')}} 
where "kwota_operacji" < 0



