import yaml
from abc import ABC, abstractmethod
from enum import Enum

from yaml_parser import YamlParser


class Section(Enum):
    INFO = "info"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    PROJECTS = "projects"
    SKILLS = "skills"
    CERTIFICATIONS = "certifications"


class Renderer(ABC):
    @abstractmethod
    def section_ordering(self) -> dict[Section, int]:
        pass

    @abstractmethod
    def render(self, src: str, dest: str) -> None:
        pass


class LatexRenderer(Renderer):
    def section_ordering(self) -> dict[Section, int]:
        return {
            Section.INFO: 0,
            Section.EDUCATION: 1,
            Section.EXPERIENCE: 2,
            Section.PROJECTS: 3,
            Section.SKILLS: 4,
            Section.CERTIFICATIONS: 4
        }

    def _preamble(self) -> str:
        return r"""
\documentclass[9pt]{article}
\pagestyle{empty}

\usepackage[hidelinks]{hyperref}
\usepackage[margin=0.45in]{geometry}
\usepackage[sfdefault]{carlito}
\usepackage{setspace}
\setstretch{0.92}
\usepackage{scalefnt}

\newcommand{\resumeSection}[1]{\noindent\underline{\makebox[\textwidth][l]{\scalefont{1.1}\textbf{#1}}}}

\begin{document}
"""

    def render(self, src: str, dest: str) -> None:
        parser = YamlParser(src)
        data = parser.load()
        with open(dest, 'w') as f:
            f.write(self._preamble())

