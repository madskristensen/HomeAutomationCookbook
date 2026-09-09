@echo off
cd /d "%~dp0"
bundle exec jekyll serve --source docs --destination _site --port 4001
