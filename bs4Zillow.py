import requests
import bs4

url = 'https://www.zillow.com/lodi-ca-95242'
headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'en-US,en;q=0.5',
           'Connection': 'keep-alive',
           'Cookie': 'zguid=24|%248327c904-7335-407e-aa65-a4c4f9feb3cb; _ga=GA1.2.832754622.1654668897; _gid=GA1.2.471045567.1654668897; zjs_anonymous_id=%228327c904-7335-407e-aa65-a4c4f9feb3cb%22; zjs_user_id=null; zg_anonymous_id=%22ebc5ca9a-1f56-404d-a11a-fa72100f8483%22; _pxvid=51368cc8-e6f2-11ec-b2d2-5a476a776a69; _gcl_au=1.1.69398016.1654668898; KruxPixel=true; __pdst=8f23e28402cc4db4ac9f6635cff12e91; utag_main=v_id:018141f3af6100149eda7947ef1605050001700d00978$_sn:1$_se:1$_ss:1$_st:1654670698145$ses_id:1654668898145%3Bexp…MYtg==:1000:wg2JNmK2cKwiOlqjU735wSo4xgFmxbFlaaFSmkiL6rP6YO10oJ9YkQf69jm3o7AfASOBtr3HMMrlZ0mD1Ucog8vXglW1xpaFmZUxUJ2/qlr5iMs2yNGOuGvkFP+iK+TEZkfzHgJS00xEj+bAK8WZ0Wzlx5qk1b1Kfzqib9SJt40r8ppIGhd7bYHMsKZFQZb8ph1db+ShtnmjwnrDSsWAKQ==; _hp2_ses_props.1215457233=%7B%22ts%22%3A1654707982782%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _cs_s=1.5.0.1654709785119; JSESSIONID=81F0329355AB08B2DEB3BB16626AF330; _uetsid=524ffee0e6f211ec9c50eb885df2eadb; _uetvid=52501110e6f211ecb8fde985f5eb3b32; _pxff_bsco=1',
           'Host': 'www.zillow.com',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'TE': 'trailers',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

params = {'searchQueryState': '{"pagination":{"currentPage": 1 }, "usersSearchTerm":"95242","mapBounds":{"west":-121.93445186914063,"east":-120.85504513085938,"south":37.89189731613302,"north":38.38766078463122},"regionSelection":[{"regionId":98069,"regionType":7}],"isMapVisible":true,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}'
          }

req = requests.get(url, headers=headers, params=params)
print(req)