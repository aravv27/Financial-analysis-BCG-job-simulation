import pandas as pd
import numpy as np

data = pd.read_csv(r"DATA\\final data.csv")

def response(query):
    #query = query.lower()
    print("Great! enter your query now: ")
    query_2 = input()
    query_2 = query_2.lower()

    if "revenue" in query_2:
        revenue(query)
    elif "income" in query_2:
        income(query)
    elif "cashflow" in query_2 or "cash" in query_2:
        cash(query)
    elif "asset" in query_2 or "assets" in query_2:
        asset(query)
    elif "liability" in query_2 or "liabilities" in query_2:
        lib(query)
    else:
        print("Sorry that data is not available right now")


def revenue(company_name):
    
    company_data = data[data['Company'].str.lower() == company_name.lower()]
    
    if company_data.empty:
        print(f"No revenue data found for {company_name}. sorry :/")
        return

    print(f"Revenue data for {company_name} (in MILLONS):")
    for index, row in company_data.iterrows():
        print(f"Year: {row['Year']}, Revenue: {row['TOTAL REVENUE']}")

def income(company_name):
    
    company_data = data[data['Company'].str.lower() == company_name.lower()]
    
    if company_data.empty:
        print(f"No income data found for {company_name}. sorry :/")
        return

    print(f"Income data for {company_name} (in MILLONS):")
    for index, row in company_data.iterrows():
        print(f"Year: {row['Year']}, Income: {row['NET INCOME']}")

def asset(company_name):
    company_data = data[data['Company'].str.lower() == company_name.lower()]
    
    if company_data.empty:
        print(f"No asset data found for {company_name}. sorry :/")
        return

    print(f"Asset data for {company_name} (in MILLONS):")
    for index, row in company_data.iterrows():
        print(f"Year: {row['Year']}, Total Assets: {row['TOTAL ASSETS']}")

def lib(company_name):
    
    company_data = data[data['Company'].str.lower() == company_name.lower()]
    
    if company_data.empty:
        print(f"No liability data found for {company_name}. sorry :/")
        return

    print(f"Liability data for {company_name} (in MILLONS):")
    for index, row in company_data.iterrows():
        print(f"Year: {row['Year']}, Total Liabilities: {row['TOTAL LIABILITIES']}")

def cash(company_name):
    
    company_data = data[data['Company'].str.lower() == company_name.lower()]
    
    if company_data.empty:
        print(f"No cash flow data found for {company_name}. sorry :/")
        return

    print(f"Cash flow data for {company_name} (in MILLONS):")
    for index, row in company_data.iterrows():
        print(f"Year: {row['Year']}, Net Cash from Operations: {row['NET CASH FROM OPERATIONS']}")

def convert(name):
    #name = name.lower()
    if name in ("microsoft", "msft", "msc"):
        return "msc"
    elif name in ("apple", "aapl", "app"):
        return "app"
    elif name in ("tesla", "tsla", "tes"):
        return "tes"
    elif name == "bye":
        return "bye"
    else:
        return 0

def main():
    print("Good Day! Im excited to help you")
    while(True):
        print("What company can I help you with: (enter bye to exit!)")
        name = input()
        name = name.lower()
        name = convert(name)
        if(name !=0):
            if(name != "bye"):
                response(name)
            else:
                print("Thank you, if you any any more queries feel free to contact!")
                break
        else:
            print("looks like the company is not in our database please re-check the name, thank you")

if __name__ == "__main__":
    main()

