import cloudscraper
from bs4 import BeautifulSoup

book_name=input("Enter Book/Novel name: ") + ".txt"
url = input("Enter any Chapter URL you want to start from: ")

scraper=cloudscraper.create_scraper()

while True:

    try:
        response=scraper.get(url)
    except:
        print("Error retrieving URL.")
        break
        
    soup=BeautifulSoup(response.text,"html.parser")
    
    #extract title
    title=soup.title.text
    
    #extract chapter contents
    content_div = soup.find('div', class_='contenta')
    chapter_content = '\n\n'.join([p.text.strip() for p in content_div.find_all('p')]) if content_div else 'No content found'
    
    #write to txt
    with open(book_name,"a") as file:
        file.write(soup.title.text+"\n"*2)
        file.write(chapter_content+"\n")
        print(title,"Done...")
    
    #find next url
    next_link = soup.find('a', rel='next')
    if next_link:
        url=str(next_link.get("href"))
    else:
        break
    
    