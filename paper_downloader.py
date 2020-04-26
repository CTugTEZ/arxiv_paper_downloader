# ARXiV Paper Downloader
# Need a list as txt taken from Arx APP iOS

import requests, sys, argparse

class paper_download:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--list", "-l", help="Enter list file path")
        parser.add_argument("--path", "-p", help="Enter download path")

        args = parser.parse_args()
        list_file_name = args.list

        list_file = open(list_file_name, "r")
        pdf_links = []

        # first 7 character must be: "    PDF"
        for lines in list_file.readlines():
            if lines[:7] == "    PDF":
                pdf_links.append(lines.split('\"')[1]) # splitting just for link

        self.printProgressBar(0,len(pdf_links),prefix='Progress:', suffix='Complete', length=50)

        for i, pdfs in enumerate(pdf_links):

            self.printProgressBar(i+1,len(pdf_links),prefix='Progress:', suffix='Complete', length=50)
            file_name_path = args.path+pdfs.split("/")[-1]+".pdf"
            r = requests.get(pdfs, stream=True)
            with open(file_name_path, "wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        pdf.write(chunk)

    def printProgressBar(self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

paper_download()
print("Download Completed!")
sys.exit()
