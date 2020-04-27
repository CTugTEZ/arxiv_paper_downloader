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
        all_file = list_file.readlines()


        for a, lines in enumerate(all_file):
            if lines[:7] == "    PDF":
                pdf_links.append(lines.split('\"')[1]) # splitting just for link
            if lines[:7] == "\"title\"":
                if len(lines.split("\"")[3]) != 2:
                    pdf_links.append(lines.split("\"")[3])
            if lines[:11] == "\"published\"":
                pdf_links.append(lines.split("\"")[3][:4])
            if lines[:9] == "\"authors\"":
                pdf_links.append(all_file[a+1].split("\"")[1])


        year, title, authors, link = [], [], [], []
        for num1 in range(0,4,1):
            for line_num in range(num1, len(pdf_links), 4):
                if num1 == 0:
                    title.append(pdf_links[line_num])
                elif num1 == 1:
                    year.append(pdf_links[line_num])
                elif num1 == 2:
                    authors.append(pdf_links[line_num])
                elif num1 == 3:
                    link.append(pdf_links[line_num])


        self.printProgressBar(0,len(link),prefix='Progress:', suffix='Complete', length=50)

        for i, pdfs in enumerate(link):
            self.printProgressBar(i+1,len(link),prefix='Progress:', suffix='Complete', length=50)
            file_name_path = args.path[0:-1]+"/"+str(year[i])+"_"+str(title[i])+"_"+str(authors[i])+".pdf"
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
