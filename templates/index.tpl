{% extends "base.html" %}

{% block title %}Miðannarverkefni{% endblock %}

{% block content %}
    {% for item in gogn['results'] %}
        {% if item.key == k %}
            {{item.company}}
            {{item.name}}
            {{item.bensin95}}
            {{item.diesel}}            
        {% endif %}
    {% endfor %}
{% endblock %}