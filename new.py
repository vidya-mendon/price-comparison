import simplejson
import tkinter as tk
import tkinter
import csv
from tkinter import *
master = tk.Tk()
import matplotlib.pyplot as plt
master.geometry('1500x800')
master.title('Price Comparison')
master.configure(bg='#ffdddd')



#=========== This is the BIG text box...

#==================================================================



def test():


    if __name__ == '__main__':
        price_data = None
        price = []
        with open('data.json', encoding='utf8') as f:
            price_data = f.read()

        if price_data is not None:
            json_price_data = simplejson.loads(price_data)
    #txt2 = tk.Text(master, height=20, width=100, font="Helvetica 13 bold", fg="white", bg='#000fff000')
    #txt2.grid(row=10, column=0)
    for d in json_price_data:



        price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
        price.append({'name': d['name'], 'price': d['walmart_price'], 'url': d['walmart_url']})
        price.append({'name': d['name'], 'price': d['ebay_price'], 'url': d['ebay_url']})
        minPricedItem = min(price, key=lambda x: float(x['price']))
        print()
        store_name = ''
        # Pick the store name based on url
        if 'amazon' in minPricedItem['url'].lower():
            store_name = 'Amazon'
        elif 'walmart' in minPricedItem['url'].lower():
            store_name = 'walmart'
        elif 'ebay' in minPricedItem['url'].lower():
            store_name = 'eBay'

        print('{} is available in cheap price at {}. The price is ${}'.format(minPricedItem['name'], store_name,
                                                                             minPricedItem['price']))


        txt2.insert(tk.END,"\n"+ str(d['name'])+"\n\n\n")
        txt3.insert(tk.END,"\n"+"      "+ str(d['amazon_price'])+"\n\n\n")
        txt4.insert(tk.END, "\n"+"     "+  str(d['walmart_price']) + "\n\n\n")
        txt5.insert(tk.END, "\n"+"     "+ str(d['ebay_price']) + "\n\n\n")
        tk.Button(master, text='Find Minimum', command=minprice, font="Helvetica 15 bold", fg="#ffdddd", bg='magenta',justify="center",border=3).grid(row=14, column=6, sticky=tk.W, pady=4)

        price = []


        #txt2.insert(tk.INSERT, str(positive))

def dispitems():
    if __name__ == '__main__':

        price_data = None
        price = []
        with open('data.json', encoding='utf8') as f:
            price_data = f.read()

        if price_data is not None:
            json_price_data = simplejson.loads(price_data)

    for d in json_price_data:



        price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
        price.append({'name': d['name'], 'price': d['walmart_price'], 'url': d['walmart_url']})
        price.append({'name': d['name'], 'price': d['ebay_price'], 'url': d['ebay_url']})
        minPricedItem = min(price, key=lambda x: float(x['price']))
        print()
        store_name = ''
        # Pick the store name based on url
        if 'amazon' in minPricedItem['url'].lower():
            store_name = 'Amazon'
        elif 'walmart' in minPricedItem['url'].lower():
            store_name = 'walmart'
        elif 'ebay' in minPricedItem['url'].lower():
            store_name = 'eBay'
def minprice():


    if __name__ == '__main__':
        price_data = None
        price = []
        with open('data.json', encoding='utf8') as f:
            price_data = f.read()

        if price_data is not None:
            json_price_data = simplejson.loads(price_data)
    #txt2 = tk.Text(master, height=20, width=100, font="Helvetica 13 bold", fg="khaki", bg='#fffffff')
    #txt2.grid(row=9, column=0)
    for d in json_price_data:



        price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
        price.append({'name': d['name'], 'price': d['walmart_price'], 'url': d['walmart_url']})
        price.append({'name': d['name'], 'price': d['ebay_price'], 'url': d['ebay_url']})
        minPricedItem = min(price, key=lambda x: float(x['price']))
        print()
        store_name = ''
        # Pick the store name based on url
        if 'amazon' in minPricedItem['url'].lower():
            store_name = 'Amazon'
        elif 'walmart' in minPricedItem['url'].lower():
            store_name = 'walmart'
        elif 'ebay' in minPricedItem['url'].lower():
            store_name = 'eBay'

        print('{} is available in cheap price at {}. The price is ${}'.format(minPricedItem['name'], store_name,
                                                                             minPricedItem['price']))

        txt6.insert(tk.END, str(minPricedItem['name']) + " is available in cheap price at " + str(store_name) + "=  "+str(
            minPricedItem['price'])+"\n\n")


def graph():
    import pandas as pd
    csvFile = open('compare.csv', 'a', newline='')  # this will open comapre.csv file in append mode
    csvWriter = csv.writer(csvFile)  # this is used to write a data to csv file

    price_data = pd.read_json('data.json')  # here we take the data.json one by one and put it to price_data
    with open('data.json', encoding='utf8') as f:
        price_data = f.read()

    if price_data is not None:
        json_price_data = simplejson.loads(price_data)
    csvWriter.writerow(
        ['name', 'ebayprice', 'amazonprice', 'walmartprice'])  # this will give the column header name in csv file.
    for d in json_price_data:
        lst1 = [d['name'], d['ebay_price'], d['amazon_price'],
                d['walmart_price']]  # we have taken the product name and all price and store it in list
        csvWriter.writerow(lst1)  # then we write the above list to the csv file.
    df = pd.read_csv("compare.csv", sep=",")  # read the csv file...which we stored product name and price above....
    df.plot.barh(x='name', y=['ebayprice', 'amazonprice', 'walmartprice'],
                 color=['crimson', 'b', 'lightgreen'])  # and plot the graph on that csv file...

    plt.show(block=False)
    csvFile = open('compare.csv', 'w')


#--------You can change the Project Title here... Color etc
tk.Label(master, text="Price Comparison For Online Shopping ",font = "Helvetica 16 bold",border="2",fg="white",bg='green',justify="left").grid(row=0)

tk.Label(master, text="Amazon",font = "Helvetica 16 bold",fg="white",bg='maroon',justify="center").grid(row=8,column=1)
tk.Label(master, text="Walmart",font = "Helvetica 16 bold",fg="white",bg='red',justify="center").grid(row=8,column=2)
tk.Label(master, text="ebay",font = "Helvetica 16 bold",fg="white",bg='purple',justify="center").grid(row=8,column=3)

tk.Label(master, text="ITEM",font = "Helvetica 16 bold",fg="white",bg='Coral',justify="center").grid(row=12,column=0)
tk.Label(master, text="PRICE",font = "Helvetica 12 bold",fg="white",bg='maroon',justify="center").grid(row=12,column=1)
tk.Label(master, text="PRICE",font = "Helvetica 12 bold",fg="white",bg='red',justify="center").grid(row=12,column=2)

tk.Label(master, text="PRICE",font = "Helvetica 12 bold",fg="white",bg='purple',justify="center").grid(row=12,column=3)
tk.Label(master, text="\t\t",bg='#ffdddd').grid(row=0,column=4)

tk.Button(master, text='Analyse', command=test,font = "Helvetica 15 bold",fg="white",bg='magenta',justify="center",border='5').grid(row=14,column=0,sticky=tk.W,pady=4)
tk.Button(master, text='Graph', command=graph,font = "Helvetica 15 bold",fg="white",bg='magenta',justify="center").grid(row=15,column=6,sticky=tk.W,pady=4)
txt2 = tk.Text(master, height=25,width=40, font="Helvetica 13 bold", fg="green")
txt2.grid(row=13,column=0)

txt3 = tk.Text(master, height=25, width=15, font="Helvetica 13 bold", fg="green")
txt3.grid(row=13, column=1)
txt4 = tk.Text(master, height=25, width=15, font="Helvetica 13 bold", fg="green")
txt4.grid(row=13, column=2)
txt5 = tk.Text(master, height=25, width=15, font="Helvetica 13 bold", fg="green")
txt5.grid(row=13, column=3)
txt6 = tk.Text(master, height=25, width=60, font="Helvetica 12 bold", fg="green")
txt6.grid(row=13, column=6)

master.mainloop()
