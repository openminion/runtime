.PHONY: check release-check

check:
	python3 scripts/validate.py

release-check: check
	git diff --check
