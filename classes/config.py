import os
import yaml


class Config:

    def get(self):
        with open('data/config.yml', 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def initial_config():

        if not os.path.isdir('data'):
            os.mkdir('data')

        if not os.path.isfile('data/config.yml'):
            with open('data/config.yml', 'w') as file:
                yaml.dump({'weight': 0}, file)
