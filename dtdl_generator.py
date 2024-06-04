import os
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import DomainModel
from besser.BUML.metamodel.object import ObjectModel
from besser.generators import GeneratorInterface

class ModelGraph(GeneratorInterface):
    TYPES = {
        "int": "integer",
        "str": "string",
        "float": "float",
        "bool": "boolean",
        "time": "time",
        "date": "date",
        "datetime": "dateTime",
        "timedelta": "Interval",
    }
    
    def __init__(self, model: DomainModel, output_dir: str = None):
        super().__init__(model, output_dir)
    def generate(self):
        file_path = self.build_generation_path(file_name="ModelGraph.py")
        templates_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(
            templates_path), trim_blocks=True, lstrip_blocks=True, extensions=['jinja2.ext.do'])
        template = env.get_template("ModelGraph_template.j2")
        with open(file_path, mode="w") as f:
            generated_code = template.render(model=self.model, types=self.TYPES)
            f.write(generated_code)
            print("Code generated in the location: " + file_path)

class TwinGraph(GeneratorInterface):
    TYPES = {
        "int": "integer",
        "str": "string",
        "float": "float",
        "bool": "boolean",
        "time": "time",
        "date": "date",
        "datetime": "dateTime",
        "timedelta": "Interval",
    }
    
    def __init__(self, obj: ObjectModel, output_dir: str = None):
        super().__init__(obj, output_dir)
    def generate(self):
        file_path = self.build_generation_path(file_name="TwinGraph.py")
        templates_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(
            templates_path), trim_blocks=True, lstrip_blocks=True, extensions=['jinja2.ext.do'])
        template = env.get_template("TwinGraph_template.j2")
        with open(file_path, mode="w") as f:
            generated_code = template.render(object=self.model, types=self.TYPES)
            f.write(generated_code)
            print("Code generated in the location: " + file_path)