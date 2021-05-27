import sys
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

def get_noun(news):

        okt = Okt()
        noun = okt.nouns(news)
        for i,v in enumerate(noun):
                if len(v) < 2:
                        noun.pop(i)

        count = Counter(noun)
        noun_list = count.most_common(100)

        return noun_list

def visualize(noun_list):


        wc = WordCloud(font_path = 'C:\\Users\\USER\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BMJUA_ttf.ttf',
        background_color="white",
        width=1000,
        height=1000,
        max_words=100,
        max_font_size = 300)

        wc.generate_from_frequencies(dict(noun_list))
        wc.to_file('keyword.png')


if __name__=="__main__":

    
        f = open("C:\\Users\\USER\\Desktop\\NLP\\crawl.txt",'r',encoding='utf-8')
        news = f.read()
        noun_list = get_noun(news)
        visualize(noun_list)