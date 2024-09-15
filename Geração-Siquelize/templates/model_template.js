const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const {{ model_name }} = sequelize.define('{{ model_name }}', {
    {% for column in columns %} //columns lista todas as tabelas do banco. column é a coleçao de objeto que representa a coluna do banco.
    {{ column.name }}: { //Nome da coluna
        type: DataTypes.{{ column.data_type }}, //tipo de dados da coluna
        allowNull: {{ column.nullable }}, //Define se a coluna é null, retorna true ou false
        {% if column.primary_key %}primaryKey: true,{% endif %} //Adiciona pk se a coluna tiver chave primaria
    },
    {% endfor %}
},{
    tableName: '{{ table_name }}', 
    timestamps: false
});

module.exports = {{ model_name }};