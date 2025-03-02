{% macro get_bucket_name(data_layer,environment='') -%}



{% set prefix = "s3://data-" %}
{% set target_bucket = prefix ~ data_layer ~ "-" ~ environment%}

{%- endmacro %}