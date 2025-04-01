from collections import Counter

with open(r"PartA\logs.txt",'r',encoding='utf-8') as f:
    chunk_size = 10000
    f_chunk = f.read(chunk_size)
    c = Counter()
    
    while True:
        chunk = [f.readline().strip() for _ in range(chunk_size)]
        if not chunk or all(line == "" for line in chunk):  # בדיקה אם הגענו לסוף הקובץ
            break
        c.update(chunk)
    print(c.most_common(10))
    
