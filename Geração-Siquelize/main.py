from config.database import get_table
from jinja2 import Environment, FileSystemLoader
import os

def create_siquelize(tables, path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('model_template.js')

    for table_name, table in tables.items():
        columns = []
        for column in table.columns:
            columns.append({
                'name': column.name,
                'data_type': str(column.type),
                'nullable': column.nullable,
                'primary_key': column.primary_key
            })
        model_code = template.render(table_name=table_name, model_name=table_name.capitalize(), columns=columns)