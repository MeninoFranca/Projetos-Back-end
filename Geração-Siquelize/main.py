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
        save = os.path.join(path, f'{table_name}.js')
        with open(save, 'w') as model_file:
            model_file.write(model_code)
        
def main():

    connection = "mysql+pymysql://u721539099_sigeps:/XVQ+y6T[y4@193.203.175.84:3306/u721539099_SIGEPS"
    tables = get_table(connection)
    create_siquelize(tables, './models')

if __name__ == '__main__':
    main()

