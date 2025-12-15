from models.scholarScraper import ScholarScraper
from models.scholarScraperConfig import ScholarScraperConfig
from models.paper import Paper


if __name__ == "__main__":
    scraper = ScholarScraper()
    scraper.request_scholar("Joko Siswantoro")
    papers = scraper.scrape_scholar_papers(5,output_format="dict")

    print(papers)

