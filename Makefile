.PHONY: help content dev build test sweep check clean stop-servers

SITE := site
NPM  := npm --prefix $(SITE)

help:
	@echo "make content   validate content/, verify reference solutions, emit site/public/content/"
	@echo "make dev       run the dev server at http://localhost:5173 (runs 'content' first)"
	@echo "make build     production build into site/dist (runs 'content' first)"
	@echo "make test      Playwright smoke tests (starts the dev server itself)"
	@echo "make sweep     Playwright sweep of every page: play blocks, reference solutions, links"
	@echo "make check     everything CI runs: content + typecheck + build + test + sweep"
	@echo "make clean     remove generated files"

content:
	python3 scripts/build_content.py

$(SITE)/node_modules: $(SITE)/package.json $(SITE)/package-lock.json
	$(NPM) ci
	@touch $(SITE)/node_modules

dev: content $(SITE)/node_modules
	$(NPM) run dev

build: content $(SITE)/node_modules
	$(NPM) run build

# Playwright starts its own servers on 5173 and 4173; clear any left over
# from an interrupted run so they cannot serve a stale base path or content.
stop-servers:
	-pkill -f "vite --port 5173" 2>/dev/null
	-pkill -f "vite preview --port 4173" 2>/dev/null

test: content $(SITE)/node_modules stop-servers
	cd $(SITE) && npx playwright test --project smoke

sweep: content $(SITE)/node_modules stop-servers
	cd $(SITE) && npx playwright test --project sweep

check: content $(SITE)/node_modules stop-servers
	cd $(SITE) && npx tsc -b
	$(NPM) run build
	cd $(SITE) && npx playwright test

clean:
	rm -rf $(SITE)/public/content $(SITE)/dist $(SITE)/test-results review
