from collections import Counter

def n_frequent(path, n):
    with open(path,'r',encoding='utf-8') as f: #open the file (I convert the file before from .txt.xlsx to .txt by the Excel convertor)
        chunk_size = 10000 #split the file to small chunck
        c = Counter() # define the Counter collection- it count the elements and them frequency.

        while True: 
            f_chunk = f.readlines(chunk_size) # limit the number of lines returned to chunk_size bytes
            if len(f_chunk) <= 0: # while the f_chunk len bigger then 0- stay in the loop, else break.
                break
            c.update(f_chunk) # update our Counter element 

        print(c.most_common(n)) # print n most common logs

def main():
    n = 3
    n_frequent(r"PartA\logs.txt", n) # call to n_frequent with file path and N.

if __name__ == "__main__":
    main()

'''
the output:
n = 1:
PS C:\HadassimProjects> & C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe c:/HadassimProjects/PartA/n_most_frequent_logs.py

[('"Timestamp: 2023-10-27 10:00:00, Error: WARN_101"\n', 200098)]

n = 2:
PS C:\HadassimProjects> & C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe c:/HadassimProjects/PartA/n_most_frequent_logs.py

[('"Timestamp: 2023-10-27 10:00:00, Error: WARN_101"\n', 200098), ('"Timestamp: 2023-10-27 10:00:00, Error: ERR_404"\n', 200094)]


n = 3:

PS C:\HadassimProjects> & C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe c:/HadassimProjects/PartA/n_most_frequent_logs.py

[('"Timestamp: 2023-10-27 10:00:00, Error: WARN_101"\n', 200098), ('"Timestamp: 2023-10-27 10:00:00, Error: ERR_404"\n', 200094)]

.
.
.

n = 5: (all the log type)

PS C:\HadassimProjects> & C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe c:/HadassimProjects/PartA/n_most_frequent_logs.py

[('"Timestamp: 2023-10-27 10:00:00, Error: WARN_101"\n', 200098), ('"Timestamp: 2023-10-27 10:00:00, Error: ERR_404"\n', 200094), ('"Timestamp: 2023-10-27 10:00:00, Error: ERR_400"\n', 200069), ('"Timestamp: 2023-10-27 10:00:00, Error: INFO_200"\n', 199931), ('"Timestamp: 2023-10-27 10:00:00, Error: ERR_500"\n', 199808)]

'''