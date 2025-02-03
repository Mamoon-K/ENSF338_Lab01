import matplotlib.pyplot as plt
import json 
with open('internetdata.json') as id:
    content = json.load(id)




for n in content:
    if n["incomeperperson"] == None:
        n["incomeperperson"] = 0
        
    else:
        n["incomeperperson"] = n["incomeperperson"]
        
    if n["internetuserate"] == None:
        n["internetuserate"] = 0
        

x1 = [n["internetuserate"]  for n in content if n["incomeperperson"] <10000]

x2 = [n["internetuserate"] for n in content if n["incomeperperson"] >= 10000]


plt.hist(x1, bins=20, alpha=0.5, label='Income < 10,000',edgecolor='black')  

plt.xlabel('Internet Use Rate')
plt.ylabel('frequency')
plt.legend()

plt.title('Income per Person < 10,000 - Internet Usage Rate')
plt.savefig('hist1.png')
plt.show()



plt.hist(x2, bins=20, alpha=0.5, label='Income >= 10,000',edgecolor='black')  

plt.xlabel('Internet Use Rate')
plt.ylabel('frequency')
plt.legend()

plt.title('Income per Person >= 10,000 - Internet Usage Rate')
plt.savefig('hist2.png')
plt.show()

 
