{{config (
    materialized = 'table',
    database = 'dev',
    schema = 'bronze',
    alias = '_posting'
)
}}

select *
from {{source('raw','posting')}}