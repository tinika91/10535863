# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:19:55 2020

@author: Tina
"""
# Beautiful Soup and the Python website scraping - IMDB Top 250 Movies

# import unittest
import pandas as pd
import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'www.imdb.com',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7,bs;q=0.6,sr;q=0.5',
    'cookie': 'session-id=130-3981468-6305660; adblk=adblk_yes; ubid-main=130-1549715-1165201; x-main=g7aBCi0hmxn567KbAgQNAK32Fw0xC0Gy5Gyo0K5juuyM7Kar9yAMZmNYlx5FyxUP; at-main=Atza^|IwEBIPp5vl-ZRZwGm3iFuq21Aoo7vOiX3sH49UMzICc_Hk82nyYzF4gBr3JnoCIWp-NpEX6gfcQvRqQ5PSFei87J4pj51qVolZo9n48W2kC8phI1-LQ8f2zS5L4DdcMe804wBKPn26cP6Zm0bVr-WyVUoDVdW-148RsmjAugYswSwyZkTZaBnHLXvjV0YerJlIDx1x89yL51b_Q5YXv4JwTlP7Z-uMHS-o_X5VfAhN37DrNzKzBwswg39wOh2cMRIBH7iEu1BPmpymLYx2QehG2jy9lPS--zHB9aX2wlxU8SuQaVkL-oHegDPiy-K1SIjgN4LWJyRXI4ftR5B8szBYOfxm3_zSYRm1_w25Gx1YNak6TP5c4Iqdv1Aw-IjiG13_orV6VEaK9QaH9p9VHKYAzkY7w2; sess-at-main=^\\^KjiK0FHGovs7+urFZTArMY1fz319mjO7cVEku9ji0Rs=^\\^; uu=BCYhtjj2YF-acS60DVeD7zEg0BTw3F_aA19V__6QLKVKlVmpG57ZQ3tYhCraoBe9AmEJcXu9u40v^%^0D^%^0AwpEOMA68sYVL54sRkr1GQNOfiAg72Y3OgsPffYvIFVJDSW0uqTUn2ZC8L0aWwnbuLpkQH3Ce3xxO^%^0D^%^0AHv1Um_dwYv_ijkAUX5UqJrk^%^0D^%^0A; session-id-time=2082787201l; session-token=Nvd/b7KB3I8dJn+P6BadNfMK3k0tjaeVmLok/W4o56YeQi5zT2zR058SNu7bU87j9yxStieyefMsIvbIEiJB7E48CVStT8g2KC2zoZWlb8wFe/l7kzXpvJSOFdQ8UAVNDZutlEQXeL1/2rd9jIFbDyVFG9/7lUJQ6eiK1XS/P8Ap4Cr6lb33zC85tS0ES/1jsubxbR6P6Pk/vsDmw6Pe7u4ptl6iGQiCGK4chvzXdzQ=; csm-hit=tb:s-YHFZMQJFHEF4H2VH04JK^|1586164587456^&t:1586164596535^&adb:adblk_yes',
}


def main():
    response = requests.get('https://www.imdb.com/chart/top/', headers=headers)

    soup = BeautifulSoup(response.content, features='html.parser')

    # print(soup.prettify())

    moviemarks = soup.select('td.titleColumn')
    inner_moviemarks = soup.select('td.titleColumn a')
    ratingmarks = soup.select('td.posterColumn span[name=ir]')
    rankingmarks = soup.select('td.posterColumn span[name=rk]')


    def get_year(movie_mark):
        moviesplit = movie_mark.text.split()
        year = moviesplit[-1] 
        return year

    years = [get_year(mark) for mark in moviemarks]
    actors_list =[mark['title'] for mark in inner_moviemarks]
    titles = [mark.text for mark in inner_moviemarks]
    ratings = [float(mark['data-value']) for mark in ratingmarks]
    rankings = [eval(mark['data-value']) for mark in rankingmarks]

   
    df = pd.DataFrame({'Rank':rankings,
                    'Movie Title':titles,
                    'Year':years, 
                    'Rating':ratings, 
                    'Starring':actors_list})
    # print(df)

    df.to_csv('CA1MartinaLehkec.csv', index=False, encoding='utf-8')
    
main()
    

# if __name__ == '__main__':
#     unittest.main()
