.SILENT:

run:
	scrapy runspider scrape/spiders/adv.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

bandit:
	bandit -r scrape --exclude tests

test:
	pytest -s -v