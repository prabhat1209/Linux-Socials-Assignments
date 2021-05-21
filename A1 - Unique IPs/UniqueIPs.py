def get_unique_ips():
    file = open('C:\\Users\\Asus\\Desktop\\LS\\log.txt','r')
    unique_set = set()
    for line in file:
        unique_set.add(line.split()[0])
    file.close()
    return unique_set

print(get_unique_ips())