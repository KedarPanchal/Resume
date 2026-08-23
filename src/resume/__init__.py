from . import yaml_parser

def main() -> None:
    parser = yaml_parser.YamlParser("data.yaml")
    data = parser.load("resume.view.yaml")
    print(data)
