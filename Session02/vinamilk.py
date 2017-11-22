from urllib.request import urlopen
from bs4 import BeautifulSoup

#1 Download webpage
url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
website = urlopen(url)
html_content = website.read.decode('utf8')


#2 Put html_content intop soup
soup = BeautifulSoup(html_content, 'html.parser

#3 Find table
table_data = soup.find('table', id='tableContent')

temp = open('temp.html', 'w')
temp.write(table_data.prettify())
temp.close()

# 4 Find all trs
trs = table_data.find_all('tr')
