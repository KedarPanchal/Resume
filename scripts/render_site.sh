#!/bin/zsh

mkdir -p dist/site
uv run render
mkdir -p site/_rendered
cp -r dist/site/. site/
cd site && bundle exec jekyll serve
