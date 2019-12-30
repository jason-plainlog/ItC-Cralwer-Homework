from crawler import Crawler
from args import get_args
from datetime import datetime


if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)

    # TODO: write content to file according to spec

    with open(args.output, 'w') as f:
        for content in contents:
            output = (datetime.strftime(content[0], "%Y-%m-%d"), content[1].replace('"', '""'), content[2].replace('"', '""'))

            f.write(f'{output[0]},"{output[1]}","{output[2]}"\n')
