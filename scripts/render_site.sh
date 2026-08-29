#!/bin/zsh

mkdir -p dist/site
uv run resume
cp -r dist/site site/_rendered
cd site && bundle exec
