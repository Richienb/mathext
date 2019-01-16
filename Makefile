# Force install the latest production version of Quilt
inst:
	pip install -U mathext

# Test the code
test:
	cd src/mathext
	python __init__.py -v

# Install the dependencies
deps:
    pip install -r requirements.txt

# Generate the Mkdocs documentation
mdoc:
    pip install mkdocs mkdocs-material pymdown-extensions pygments
    mkdocs build --verbose --clean --strict

# Generate the Sphinx documentation
sdoc:
	pip install sphinx sphinx_materialdesign_theme
	cd docs-sphinx
	sphinx-build -b html rst html

# Build the PyPi package
pack:
    pip install setuptools-git-version setuptools wheel
    cd src
    python setup.py sdist bdist_wheel
