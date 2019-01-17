# GliaCloud 考題 for Backend Engineer  
## Part 1
### 1) counting \(counting.py\)
Done.  
I use regex and the build-in method sorted to solve this problem and have tried to handle all possibilities.
### 2) integration \(integration.py\)
Done.  
anonymous(intercept) * step = y * x = area of each little interval  
So the sum of little areas is the integration of the anonymous function
### 3) multiples of 3 or 5 \(multiples.py\)
Done.  
I solved this with my intuition given a limited time. I think there are some better approaches.
## Part 2
a) 請用 Python 寫出一個可以爬 ptt /reddit 任意看板 (https://www.ptt.cc) 的爬蟲
程式，可以使用任意 Python 套件
Done.  
PTT crawler implemented with scrapy  
PTT article can have complex patterns, I've tried my best to handle these possible patterns.
### Installation

    pip install scrapy
    cd pttcrawler

### Example Usage

Command pattern:  

    scrapy crawl ptt <-a argument=value> <-o outputfile.json>  

Example 1: Crawl 5 articles from PTT Goossiping and dump the data into output.json

    scrapy crawl ptt -a max_articles=5 -a board='Gossiping' -o output.json

Example 2: Crawl 5 articles that title contain 丹丹 from PTT Goossiping and dump the data into output.json  

    scrapy crawl ptt -a max_articles=5 -a board='Gossiping' -a keyword=丹丹 -o output.json

Example 3: Crawl an article from url (https://www.ptt.cc/bbs/WomenTalk/M.1494689998.A.2AA.html) and dump the data into output.json  

    scrapy crawl ptt -a test_url=https://www.ptt.cc/bbs/WomenTalk/M.1494689998.A.2AA.html -o output.json

### Available Arguments
**`max_articles`**: Maximium articles to crawl. *default=5*  
**`max_retry`**: Maximium retries during the process. *default=5*  
**`board`**: PTT board to crawl. *default='HatePolitics'*  
**`keyword`**: If specified, the spider will only retrieve articles that has the given keyword in its title. *optional argument*    
**`test_url`**: If set, only the article in the given url will be crawled and all arguments above will be ignored. This argument is especially helpful when debugging. *optional argument*  
**`get_content`**: If set *False*, content of articles will not be retrieved. This helps to reduce the size of dataset if you are not interested in them. *default=True*  
**`get_comments`**: If set *False*, comments of articles will not be retrieved and article scores will not be calculated. This helps to reduce the size of dataset if you are not interested in them. *default=True*  