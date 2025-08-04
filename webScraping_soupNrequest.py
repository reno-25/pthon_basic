from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') 
print(soup.prettify()) 

# parser adalah sebuah library yang digunakan untuk mengurai HTML atau XML menjadi struktur data yang dapat dimanipulasi.
# .text digunakan untuk mengambil teks dari elemen HTML yang telah diurai.
# .prettify() digunakan untuk menampilkan HTML dengan format yang lebih mudah dibaca, dengan indentasi yang sesuai.

soup.find('div')

soup.find_all('div', class_='row')

soup.find_all('p', class_='lead')

soup.find('p', class_='lead').text.strip()

# .find() digunakan untuk menemukan elemen pertama yang cocok dengan kriteria yang diberikan.
# .find_all() digunakan untuk menemukan semua elemen yang cocok dengan kriteria yang diberikan.
# .strip() digunakan untuk menghapus spasi di awal dan akhir string.

soup.find_all('th')
soup.find_all('td')

soup.find('th').text.strip()

