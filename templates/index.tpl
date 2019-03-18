{% extends "base.html" %}

{% block title %}Miðannarverkefni{% endblock %}

{% block content %}

{% set one = [] %}
    {% if item.company not in one %}
        {% for item in gogn['results'] %}
            <p>fyrirtæki: {{item.company}}</p>
            <p>nafn: {{item.name}}</p>
            <p>bensín: {{item.bensin95}}</p>
            <p>dísil: {{item.diesel}}</p>      
        {% endfor %}
    {% endif %}
    
{% endblock %}