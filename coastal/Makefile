TARGETS = format lint test typecheck

.PHONY: $(TARGETS)

all:
	$(error Valid targets are: $(TARGETS))

format:
	black *.py
	isort *.py

lint:
	pylint *.py

test: lint typecheck

typecheck:
	mypy *.py
