
import time
import requests
from multiprocessing import Pool


class Index:

    def __init__(self, urls, stops):
        '''
        Here I used pythons multiprocessor to speed the large # of requests needed to be made. 
        This was the fastest way I could think of. :) I'd love to know how you got 1.52 seconds!
        '''
        self.urls = urls
        self.stops = stops
        self.review_dict = {}

        pool = Pool(33)  # any greater or lower resulted in less optimal timing
        data = pool.map(self.process_requests, urls)

        count = len(data)  # this is pretty basic I know, but it did the job!
        while count > 0:
            self.review_dict[data[count-1][0]] = data[count-1][1]
            count -= 1
        pool.terminate()


    def process_requests(self, url):
        ''' This method is to clean data and open each singular http '''
        print(f'indexing {url}')
        r = requests.get(url)
        full_text = r.text.split('\n')
        school = full_text.pop(0)
        school = school.replace('\r', '')
        reviews = [review.replace('\r', '').lower() for review in full_text]
        return school, reviews


    def get_reviews_by_keyword(self, term):
        ''' 
        Bulk of the main logic; I tried using re to be more specific 
        but this ended up looking the most accurate
        '''
        if term not in stops:
            # exclude stops added here rather than remove all stops from review bc it seemed friendlier
            # as well as accounting for any full phrases such as "we won" vs "we" which is in stops
            for college in self.review_dict:
                review_count = len([review for review in self.review_dict[college] if term in review])
                if review_count > 0:
                    print(f"In {review_count} review[s] for {college}")
        else:
            # this was not in the requirements, but it seemed "nicer" to provide some response to the user
            print(f"Search term '{term}' In 0 review[s]")



if __name__ == '__main__':
    with open('stopWords.txt', 'r') as stopwords:
        # exclude these words from result count, line #44
        stops = stopwords.read().split()
    with open('urls.txt', 'r') as url_file:
    # create basic index
        urls, start = url_file.read().split(), time.time()
        index = Index(urls, stops)
        end = time.time()
        print(f"\n\n\nFinished downloading & indexing {len(urls)} colleges in {end-start} seconds")

    instructions = '''
    ===== INSTRUCTIONS =====
    To find all colleges with reviews matching a search term
    enter a term.
    
    To exit the program, type "exit" or "q".
    '''
    print(instructions)
    # For user experience, I added this to make the program a little more enjoyable to use rather than looking
    # in the readme or using ctrl+c to esc

    term = input('Enter a search token: ').lower()
    while term not in ["exit", "q"]:
        index.get_reviews_by_keyword(term)
        term = input('\n\n\nEnter a search token: ').lower()
