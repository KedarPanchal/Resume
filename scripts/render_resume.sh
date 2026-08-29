#!/bin/zsh

mkdir -p dist/resume
uv run resume
cd dist/resume && pdflatex -interaction=nonstopmode resume.tex
