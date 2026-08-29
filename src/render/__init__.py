from . import yaml_parser
from . import renderer

import logging

logger = logging.getLogger(__name__)

def main() -> None:
    logging.basicConfig(level=logging.INFO)

    logger.info("Starting resume rendering process...")
    resume_parser = yaml_parser.YamlParser("data.yaml")
    resume_data = resume_parser.load("resume.view.yaml")
    logger.info(resume_data)
    latex_renderer = renderer.LatexRenderer("dist/resume/resume.tex")
    latex_renderer.render(resume_data)
    logger.info("Resume rendering process completed successfully.")

    logger.info("Starting Jekyll site render process...")
    jekyll_parser = yaml_parser.YamlParser("site.view.yaml")
    jekyll_data = jekyll_parser.load("site.view.yaml")
    logger.info(jekyll_data)
    jekyll_renderer = renderer.JekyllRenderer("dist/site")
    jekyll_renderer.render(jekyll_data)
    logger.info("Jekyll site render process completed successfully.")
