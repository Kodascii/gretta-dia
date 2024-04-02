{%- extends 'full.tpl' -%}

{%- block header -%}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{{ notebook_name }}</title>
        </head>
    <body>
{%- endblock header -%}

{%- block body -%}
    <div class="container">
        <div class="output_subarea">
        {{ super() }}
        </div>
    </div>
{%- endblock body -%}

{%- block footer -%}
    </body>
</html>
{%- endblock footer -%}