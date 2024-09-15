from config.database import get_table
from jinja2 import Environment, FileSystemLoader
import os

def create_siquelize(tables, path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('model_template.js')