#!/bin/bash
# convert the obsidian format into mkdocs format
python3 utils/TextConverter/src/main.py docs

# maintain git and deploy
git add . 
git commit -m "update" 
git push origin main
