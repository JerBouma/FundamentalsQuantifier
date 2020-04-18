import FundamentalAnalysis as fa
from tqdm import tqdm
import json


def collect_working_companies(company_list):
    companies = {}
    no_data_companies = {}

    print("Parsing companies")
    for company in tqdm(company_list.index):
        try:
            fa.cash_flow_statement(company)
            companies[company] = company_list['name'].loc[company]
        except KeyError:
            no_data_companies[company] = company_list['name'].loc[company]

    with open('companies.json', 'w') as json1:
        json.dump(companies, json1)

    with open('no_data_companies.json', 'w') as json2:
        json.dump(no_data_companies, json2)


# collect_working_companies(fa.available_companies())

def collect_sectors_and_industries(companies_json):
    with open(companies_json, "r") as read_file:
        company_list = json.load(read_file)

    sectors = []
    sector_per_company = {}

    industries = []
    industry_per_company = {}

    for company in tqdm(company_list.keys()):
        data = fa.profile(company)

        sector = data.loc['sector']['profile']
        industry = data.loc['industry']['profile']

        if sector is not None:
            sector_per_company[company] = sector
        if industry is not None:
            industry_per_company[company] = industry

        if sector not in sectors:
            if sector is not None:
                sectors.append(sector)
        if industry not in industries:
            if industry is not None:
                industries.append(industry)

    with open ('sectors.json', 'w') as json1:
        json.dump(sorted(sectors), json1)

    with open('industries.json', 'w') as json2:
        json.dump(sorted(industries), json2)

    with open ('sector_per_company.json', 'w') as json3:
        json.dump(sector_per_company, json3)

    with open('industry_per_company.json', 'w') as json4:
        json.dump(industry_per_company, json4)


collect_sectors_and_industries("companies.json")
