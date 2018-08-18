from bs4 import BeautifulSoup
import csv

def make_soup(url):
    the_page = open(url)
    soup_data = BeautifulSoup(the_page.read(), "html.parser")
    return soup_data

def stir_the_soup(url , year):
    # playerdatasaved = ""
    soup = make_soup(url)
    # table = soup.find('table', attrs={'class': 'sortable stats_table now_sortable'})
    header = [[val.text.encode('utf8') for val in soup.find(lambda tag: tag.name=='table')]]
    rows = []
    for row in soup.find_all('tr'):
        rows.append([val.text.encode('utf8') for val in row.find_all('th')])
        rows.append([val.text.encode('utf8') for val in row.find_all('tr')])
        rows.append([val.text.encode('utf8') for val in row.find_all('td')])

    with open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_School_Stats/%d_School_Stats.csv" % year, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(row for row in rows if row)
    return writer

# needed for arsing only in testing
def Read_and_pars_text_to_csv():
    # Set up input and output variables for the script
    gpsTrack = open("SaritHadad.csv", 'rb')

    # Set up CSV reader and process the header
    csvReader = csv.reader(gpsTrack)

    # Make an empty list
    coordList = []

    # Loop through the lines in the file and get each coordinate
    for row in csvReader:
        if "NCAA" in row[0]:
            coordList.append(row)
    with open("SaritHadad_2.csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(row for row in coordList)


def create_clean_csv():
    for year in range(1993, 2018):
    #Part 2 - clean csv's
        csv_file = open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_School_Stats/%d_School_Stats.csv" % year, 'rb')
        csvReader = csv.reader(csv_file)

        # Make an empty list
        coordList = []
        # Loop through the lines in the file and get each coordinate
        index = 0
        for i in range(1, 10):
            next(csvReader, None)
            index += 1

        for row in csvReader:
            # Print Header to csv
            if index == 9:
                # print("SAaaaaaaarrrrriiiiittttttHaddddddaaaaaddddd")
                # Print the header to result file (without the "RK")
                coordList.append(['School', 'G', 'W', 'L', 'W - L %', 'SRS', 'SOS', 'W', 'L', 'W', 'L', 'W', 'L', 'Tm.', ' Opp.', ' ', 'MP', 'FG', 'FGA', 'FG %', '3P', '3PA', '3P %', 'FT', 'FTA', 'FT %', 'ORB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
                index += 1
            if ("Overall" in row):
                next(csvReader, None)
            else:
                if ("Rk" in row) and ("School" in row) and ("G" in row) :
                    next(csvReader, None)
                else:
                    if len(row) > 1:
                        #print(row)

                        coordList.append(row)

        # # Print the output file
        with open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_School_Stats/%d_School_Stats_res.csv" % year, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(row for row in coordList)


def add_exists_in_NCAA_column():
    for year in range(1993, 2018):
        csv_file_1 = "/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_School_Stats/%d_School_Stats_res.csv" % year
        with open(csv_file_1, 'rb') as fin:
            reader = csv.reader(fin)
            print(reader)
            with open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_new_School_State_res/%d_new_School_Stats_res.csv" % year, 'wb') as fout:
                writer = csv.writer(fout)
                # set headers here, grabbing headers from reader first
                writer.writerow(next(reader) + ["InNCAA"])
                for row in reader:
                    # use whatever index for the value, or however you want to construct your new value
                    if "NCAA" in row[0]:
                        row.append(1)

                    else:
                        row.append(0)
                    writer.writerow(row)

def remove_NCAA_from_school_name():
    for year in range(1993, 1994):
        csv_file_1 = "/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_new_School_State_res/%d_new_School_Stats_res.csv" % year

        res = []
        with open(csv_file_1, 'rb') as fin:
            content = csv.reader(fin)
            for row in content:
                if "NCAA" in row[0]:
                    row[0] = row[0].replace("NCAA"," ")
                res.append(row)
            # fin.close()
        with open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_new_School_State_res/%d_new_School_Stats_res.csv" % year,'wb') as fout:
            writer = csv.writer(fout)
            for rows in res:
                writer.writerow(rows)
        # fout.close()

def remove_shittt_from_school_name():
    for year in range(1993, 1994):
        csv_file_1 = "/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_new_School_State_res/%d_new_School_Stats_res.csv" % year

        res = []
        with open(csv_file_1, 'rb') as fin:
            content = csv.reader(fin)
            for row in content:
                if "¬" in row[0]:
                    row[0] = row[0].replace("¬†"," ")
                res.append(row)
            # fin.close()
        with open("/Users/mihushamsh/PycharmProjects/ML_project_NCAA_March_Madness/f_new_School_State_res/%d_new2_School_Stats_res.csv" % year,'wb') as fout:
            writer = csv.writer(fout)
            for rows in res:
                writer.writerow(rows)
        # fout.close()


def main():
    # Extarct the Tables information from the urls (of Html type)
    # for year in range(1993, 1994):
    #     url = r'/Users/mihushamsh/Google Drive/Technion/Sem_8/data parsing/%d School Stats _ College Basketball at Sports-Reference.com.html' % year
    #     stir_the_soup(url , year)

    # Clean each csv file with only needed rows
    # create_clean_csv()
    # Add new column contains 1 if the school played in NCAA or 0 if not
    # add_exists_in_NCAA_column()
    # Edit the CSV by remove the "NCAA" from Schools names
    # remove_NCAA_from_school_name()
    remove_shittt_from_school_name()
if __name__ == "__main__":
    main()


