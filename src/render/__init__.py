from . import yaml_parser
from . import renderer

import logging

logger = logging.getLogger(__name__)

def main() -> None:
    logging.basicConfig(level=logging.INFO)

    parser = yaml_parser.YamlParser("data.yaml")
    data = parser.load("resume.view.yaml")
    logger.info(data)
    latex_renderer = renderer.LatexRenderer("dist/resume.tex")
    latex_renderer.render(data)
