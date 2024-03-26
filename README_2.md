#    https://stackoverflow.com/questions/70920378/poetry-returns-dyld-library-not-loaded-image-not-found-following-brew-ins
# Uninstall poetry
curl -sSL https://install.python-poetry.org | python3 - --uninstall

# change to required python
pyenv local 3.10.8

# activate python
eval "$(pyenv init --path)"

# check python version
python --version

# Install latest poetry
curl -sSL https://install.python-poetry.org | python3 -



/Users/andi/.local/bin/poetry env use pyhton
Funktioneirt aus irgendeinen Grund nicht, aber richtige Vewrsion wird gezogen.

/Users/andi/.local/bin/poetry shell   

