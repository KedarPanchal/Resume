from . import yaml_parser
from . import renderer

def main() -> None:
    parser = yaml_parser.YamlParser("data.yaml")
    data = parser.load("resume.view.yaml")
    print(data)
    latex_renderer = renderer.LatexRenderer("dist/resume.tex")
    latex_renderer.render(data)
