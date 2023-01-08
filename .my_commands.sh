#!/bin/bash
function create() {
    python3 create.py $1
    cd /Users/markuusen/Documents/Coding/$1
    git init
    git remote add origin git@github.com:markuusen/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
    clear
}