import requests
import sys
from optparse import OptionParser
from bs4 import BeautifulSoup

### Arguments
parser = OptionParser()
parser.add_option("-u", "--url", dest="url_id",
                help="Google Drive URL")
parser.add_option("-o", "--output", dest="output_file",
                help="Filename")

(options, args) = parser.parse_args()

if (options.url_id == None):
    parser.error("-u url google frive is required")
if (options.output_file == None):
    parser.error("-o output filename is required")


try:
    session = requests.Session()
    response = session.get(options.url_id)

    soup = BeautifulSoup(response.text, features="lxml")

    for a in soup.find_all('a', href=True):
        if "download&confirm" in a['href']:
            r = session.get("https://docs.google.com"+a['href'])
            with open(options.output_file,'wb') as f:
                f.write(r.content)
                f.close
                break
except Exception as e:
    print("status err Error running getdrive: %s" % e.error_message)
