@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=  --xformers --medvram-sdxl --no-half-vae --opt-split-attention  --autolaunch

call webui.bat
