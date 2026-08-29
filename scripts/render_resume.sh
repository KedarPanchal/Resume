#!/bin/zsh

mkdir -p dist/resume
uv run render
cd dist/resume && pdflatex -interaction=nonstopmode resume.tex
