import argparse

from modules import webget

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('--destination', help='The name of the file to store the url in')
    args = parser.parse_args()

    if(args.destination == None):
      newDest = args.url.replace('https://', '').strip('.com') +'.dat'
      destination = newDest
    else:
      destination = args.destination
      
    webget.download(args.url, destination)