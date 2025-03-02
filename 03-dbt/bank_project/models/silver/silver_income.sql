{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'silver',
    alias = 'income'
)
}}

select "data_księgowania","kwota_operacji","tytułem",'J-labs' as company
from {{ref('bronze_posting')}} 
where "rachunek_źródłowy" like '%53105014611000009083795220'
union
select "data_księgowania","kwota_operacji","tytułem",'EXPLORIS' as company
from {{ref('bronze_posting')}} 
Where "nadawca_odbiorca" like  '%EXPLORIS%'
union
select "data_księgowania","kwota_operacji","tytułem",'ZUS' as company
from {{ref('bronze_posting')}} 
Where "nadawca_odbiorca" like  '%ZUS%'
union
select "data_księgowania","kwota_operacji","tytułem",'GODEL' as company
from {{ref('bronze_posting')}} 
Where "nadawca_odbiorca" like  '%GODEL TECHNOLOGIES%'





