import json
import csv

with open ('C:\\Users\\Asus\\Desktop\\LS\\raw.json','r') as file:
    data = json.load(file)
    
with open('data.csv','w') as to_write:
    csv_writer = csv.writer(to_write)
    csv_writer.writerow(['pk','model','codename','name','content_type'])
    for item in data['json_variable']:
        csv_writer.writerow([item['pk'],item['model'],item['fields']['codename'],item['fields']['name'],item['fields']['content_type']])