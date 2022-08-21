import sys
import requests

def check_link_ok(link:str) -> bool:
    result = True

    if link[0:24] != "https://www.youtube.com/":
        result = False
    
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argument error: expected 1 argument instead of ", len(sys.argv) , ".", sep='')
        sys.exit()

    link = sys.argv[1]    

    req = requests.get(link, 'html.parser', cookies = {'CONSENT' : 'YES+'})

    index = req.text.find("\"UC")+1
    print(req.text[index:index+24])
