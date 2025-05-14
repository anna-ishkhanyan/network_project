PROGRAM = cat_comics.py

all: install run

install:
	@echo "Upgrading and installing required Python packages..."
	@pip install --upgrade pip > /dev/null 2>&1
	@pip install beautifulsoup4 selenium pillow requests > /dev/null 2>&1
run:
	@echo "Running the comic downloader..."
	python $(PROGRAM)

.PHONY: all install run
