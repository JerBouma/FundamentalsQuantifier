import FundamentalAnalysis as fa
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
from assets.introduction_text import introduction_text
from utilities import create_drop_down_options

with open("data/companies.json", "r") as read_file:
    company_list = json.load(read_file)
company_options_list = []
for company in company_list:
    company_options_list.append({'label': str(company_list[company] + ' (' + company + ')'),
                                 'value': company})

with open("data/sector_per_company.json", "r") as read_file:
    sector_per_company = json.load(read_file)

with open("data/industry_per_company.json", "r") as read_file:
    industry_per_company = json.load(read_file)

sectors_options_list = create_drop_down_options("sectors.json", dictionary=False)
industries_options_list = create_drop_down_options("industries.json", dictionary=False)
key_metrics_options_list = create_drop_down_options("key_metrics.json")
ratios_options_list = create_drop_down_options("financial_ratios.json")
balance_sheet_statement_options = create_drop_down_options("balance_sheet_statement.json", dictionary=False)
income_statement_options = create_drop_down_options("income_statement.json", dictionary=False)
cash_flow_statement_options = create_drop_down_options("cash_flow_statement.json", dictionary=False)
financial_statement_growth_options = create_drop_down_options("financial_statement_growth.json", dictionary=False)

app = dash.Dash(__name__)
app.title = "Fundamentals Quantifier"
server = app.server

app.layout = html.Div(
    children=[
        html.Div([
            html.Div([
                html.H2("Fundamentals Quantifier",
                        style={'text-align': 'center',
                               'text-shadow': '-1px 0 black, 0 1px black,'
                                              '1px 0 black, 0 -1px black'}),
                html.Div([
                    html.Summary('API Key'),
                    dcc.Input(
                        id="api", style={'width': '100%'})],
                    style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Sectors'),
                    dcc.Dropdown(
                        id="sectors",
                        options=sectors_options_list,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Industries'),
                    dcc.Dropdown(
                        id="industries",
                        options=industries_options_list,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Companies'),
                    dcc.Dropdown(
                        id="companies",
                        options=company_options_list,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Div([
                        html.Summary('Period',
                                     style={'padding-right': "10px"}),
                        dcc.RadioItems(
                            id='period',
                            value='annual',
                            options=[
                                {'label': 'Annually', 'value': 'annual'},
                                {'label': 'Quarterly', 'value': 'quarter'}],
                            labelStyle={'display': 'inline-block', 'padding-right': '5px'})
                    ], style={'display': 'flex', "padding-top": "10px"}),

                    html.Div([
                        html.Summary('Data',
                                     style={'padding-right': "20px"}),
                        dcc.RadioItems(
                            id='data_type',
                            value='linear',
                            options=[
                                {'label': 'Linear', 'value': 'linear'},
                                {'label': 'Log', 'value': 'log'}],
                            labelStyle={'display': 'inline-block', 'padding-right': '5px'})
                    ], style={'display': 'flex', "padding-bottom": "10px",
                              'border-bottom': '1px solid #ffeedd'})
                ]),

                html.Div([
                    html.Summary('Key Metrics'),
                    dcc.Dropdown(
                        id="key_metrics",
                        options=key_metrics_options_list,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Financial Ratios'),
                    dcc.Dropdown(
                        id="financial_ratios",
                        options=ratios_options_list,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Balance Sheet Statement'),
                    dcc.Dropdown(
                        id="balance_sheet_statement",
                        options=balance_sheet_statement_options,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Income Statement'),
                    dcc.Dropdown(
                        id="income_statement",
                        options=income_statement_options,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Cash Flow Statement'),
                    dcc.Dropdown(
                        id="cash_flow_statement",
                        options=cash_flow_statement_options,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div([
                    html.Summary('Financial Statement Growth'),
                    dcc.Dropdown(
                        id="financial_statement_growth",
                        options=financial_statement_growth_options,
                        multi=True)], style={'padding-top': '10px'}),

                html.Div(id="company_profile_container"),
                html.Div(id='company_profile_data', style={'display': 'none'}),

                html.Div("Designed by Jeroen Bouma",
                         style={'margin-top': '20px', 'padding-top': '10px',
                                'border-top': '1px solid #ffeedd'}),
                html.Div(("Data is obtained through my package FundamentalAnalysis "
                          "which can be found by clicking the first GitHub icon. "
                          "Source code of this app can be found by clicking "
                          "the second GitHub icon."),
                         style={"font-size": "10px"}),
                html.A(html.Img(src='assets/GitHub-Mark-Light-32px.png',
                                style={"padding": "10px 10px 10px 0px"}),
                       href="https://github.com/JerBouma/FundamentalAnalysis",
                       target="_blank"),
                html.A(html.Img(src='assets/GitHub-Mark-Light-32px.png',
                                style={"padding": "10px"}),
                       href="https://github.com/JerBouma/FundamentalsQuantifier",
                       target="_blank"),
                html.A(html.Img(src='assets/linkedin-3-32.png',
                                style={"padding": "10px"}),
                       href="https://www.linkedin.com/in/boumajeroen/",
                       target="_blank")

            ], className="left columns"),

            html.Div([
                html.Div(children=dcc.Markdown(introduction_text,
                                               style={"color": "black"}),
                         id="introduction"),

                html.Div(id="stock_data_container"),
                html.Div(id="key_metrics_container"),
                html.Div(id="ratios_container"),
                html.Div(id="balance_sheet_container"),
                html.Div(id="income_statement_container"),
                html.Div(id="cash_flow_statement_container"),
                html.Div(id="financial_statement_growth_container"),

                html.Div(id='stock_data', style={'display': 'none'}),
                html.Div(id='key_metrics_data', style={'display': 'none'}),
                html.Div(id='ratios_data', style={'display': 'none'}),
                html.Div(id='balance_sheet_data', style={'display': 'none'}),
                html.Div(id='income_statement_data', style={'display': 'none'}),
                html.Div(id='cash_flow_statement_data', style={'display': 'none'}),
                html.Div(id='financial_statement_growth_data', style={'display': 'none'}),
            ], className="right columns")
        ])])


@app.callback(
    Output(component_id='introduction', component_property='children'),
    [Input(component_id='companies', component_property='value')])
def introduction_text_field(companies):
    if not companies:
        return dcc.Markdown(introduction_text,
                            style={"color": "black"})
    else:
        return None


@app.callback(
    Output(component_id='companies', component_property='options'),
    [Input(component_id='sectors', component_property='value'),
     Input(component_id='industries', component_property='value')])
def show_matching_companies(sectors, industries):
    if (not sectors or sectors is None) and (not industries or industries is None):
        return company_options_list
    try:
        industry_companies = [i for i, j in industry_per_company.items() if j in industries]
    except TypeError:
        None
    try:
        sector_companies = [i for i, j in sector_per_company.items() if j in sectors]
    except TypeError:
        None

    if not industries or industries is None:
        sector_and_industry_companies = sector_companies
    elif not sectors or sectors is None:
        sector_and_industry_companies = industry_companies
    else:
        sector_and_industry_companies = list(set(industry_companies).intersection(sector_companies))

    new_company_list = []

    for company in sector_and_industry_companies:
        new_company_list.append({'label': str(company_list[company] + ' (' + company + ')'),
                                 'value': company})

    return new_company_list


@app.callback(
    Output(component_id='company_profile_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="api", component_property='value')])
def collect_company_profiles(companies, api_key):
    if not companies or companies is None:
        return None

    company_profiles = {}
    for company in companies:
        company_profiles[company] = fa.profile(company, api_key).to_dict()

    return json.dumps(company_profiles)


@app.callback(
    Output(component_id='company_profile_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="company_profile_data", component_property='children')])
def display_company_profiles(companies, company_profile_data):
    if not companies or companies is None:
        return None

    data_dump = json.loads(company_profile_data)
    profiles = []

    for company in data_dump:
        df = pd.DataFrame(data_dump[company]['profile'], index=[company]).T
        profiles.append(html.Br())
        profiles.append(html.H5([df.loc['companyName'][0]]))
        profiles.append(html.Div(['Sector: ' + df.loc['sector'][0]]))
        profiles.append(html.Div(['Industry: ' + df.loc['industry'][0]]))
        profiles.append(html.Br())
        profiles.append(html.Div([df.loc['description'][0]]))

    return profiles


@app.callback(
    Output(component_id='stock_data', component_property='children'),
    [Input(component_id="companies", component_property='value')])
def collect_stock_data(companies):
    if not companies or companies is None:
        return None

    stock_data = {}
    for company in companies:
        try:
            stock_data[company] = fa.stock_data(company, period="10y")['adjclose'].to_dict()
            stock_data[company] = {k.isoformat(): v for k, v in stock_data[company].items()}
        except Exception:
            stock_data[company] = {}

    return json.dumps(stock_data)


@app.callback(
    Output(component_id='stock_data_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="stock_data", component_property='children')])
def display_stock_data_graph(companies, data_type, stock_data):
    if not companies or companies is None:
        return None

    data_dump = json.loads(stock_data)
    traces = []

    for company in data_dump:
        df = pd.DataFrame(data_dump[company], index=[company]).T
        scatter = {'x': df.index, 'y': df[company], 'name': company}
        traces.append(scatter)

    graph = dcc.Graph(
        id='stock_data_graph',
        figure={'data': traces,
                'layout': {
                    'title': 'Stock Data',
                    'xaxis': {
                        'nticks ': 10},
                    'yaxis': {
                        'type': data_type}}},
        config={'displayModeBar': False})

    return html.Div(graph)


@app.callback(
    Output(component_id='key_metrics_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="period", component_property='value'),
     Input(component_id='key_metrics', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_key_metrics_data(companies, period, key_metrics, api_key):
    if (not companies or companies is None) or key_metrics is None:
        return None

    key_metrics_data = {}
    for company in companies:
        key_metrics_data[company] = fa.key_metrics(company, api_key, period=period).to_dict()

    return json.dumps(key_metrics_data)


@app.callback(
    Output(component_id='key_metrics_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="key_metrics_data", component_property='children'),
     Input(component_id="key_metrics", component_property="value"),
     Input(component_id='key_metrics', component_property='options')])
def display_key_metrics_graph(companies, data_type, key_metrics_data,
                              key_metrics_values, key_metrics_options):
    if (not companies or companies is None) or key_metrics_values is None:
        return None

    graphs = []
    data_dump = json.loads(key_metrics_data)
    for key in key_metrics_values:
        title = next(item for item in key_metrics_options if item["value"] == key)['label']
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[key]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(key),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': title}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


@app.callback(
    Output(component_id='ratios_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id='financial_ratios', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_ratios_data(companies, financial_ratios, api_key):
    if (not companies or companies is None) or financial_ratios is None:
        return None

    ratios_data = {}
    for company in companies:
        ratios_data[company] = fa.financial_ratios(company, api_key).to_dict()

    return json.dumps(ratios_data)


@app.callback(
    Output(component_id='ratios_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="ratios_data", component_property='children'),
     Input(component_id="financial_ratios", component_property="value"),
     Input(component_id="financial_ratios", component_property="options")])
def display_ratios_graphs(companies, data_type, ratios_data,
                          financial_ratios_values, financial_ratios_options):
    if (not companies or companies is None) or financial_ratios_values is None:
        return None

    graphs = []
    data_dump = json.loads(ratios_data)
    for ratio in financial_ratios_values:
        title = next(item for item in financial_ratios_options if item["value"] == ratio)['label']
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[ratio]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(ratio),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': title}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


@app.callback(
    Output(component_id='balance_sheet_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="period", component_property='value'),
     Input(component_id='balance_sheet_statement', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_balance_sheet_statement_data(companies, period, balance_sheet_statement, api_key):
    if (not companies or companies is None) or balance_sheet_statement is None:
        return None

    balance_sheet_statement_data = {}
    for company in companies:
        balance_sheet_statement_data[company] = fa.balance_sheet_statement(company, api_key, period=period).to_dict()

    return json.dumps(balance_sheet_statement_data)


@app.callback(
    Output(component_id='balance_sheet_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="balance_sheet_data", component_property='children'),
     Input(component_id="balance_sheet_statement", component_property="value")])
def display_balance_sheet_statement_graphs(companies, data_type, balance_sheet_data,
                                           balance_sheet_statement):
    if (not companies or companies is None) or balance_sheet_statement is None:
        return None

    graphs = []
    data_dump = json.loads(balance_sheet_data)
    for item in balance_sheet_statement:
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[item]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(item),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': item}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


@app.callback(
    Output(component_id='income_statement_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="period", component_property='value'),
     Input(component_id='income_statement', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_income_statement_data(companies, period, income_statement, api_key):
    if (not companies or companies is None) or income_statement is None:
        return None

    income_statement_data = {}
    for company in companies:
        income_statement_data[company] = fa.income_statement(company, api_key, period=period).to_dict()

    return json.dumps(income_statement_data)


@app.callback(
    Output(component_id='income_statement_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="income_statement_data", component_property='children'),
     Input(component_id="income_statement", component_property="value")])
def display_income_statement_graphs(companies, data_type, income_statement_data,
                                    income_statement):
    if (not companies or companies is None) or income_statement is None:
        return None

    graphs = []
    data_dump = json.loads(income_statement_data)
    for item in income_statement:
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[item]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(item),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': item}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


@app.callback(
    Output(component_id='cash_flow_statement_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="period", component_property='value'),
     Input(component_id='cash_flow_statement', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_cash_flow_statement_data(companies, period, cash_flow_statement, api_key):
    if (not companies or companies is None) or cash_flow_statement is None:
        return None

    cash_flow_statement_data = {}
    for company in companies:
        cash_flow_statement_data[company] = fa.cash_flow_statement(company, api_key, period=period).to_dict()

    return json.dumps(cash_flow_statement_data)


@app.callback(
    Output(component_id='cash_flow_statement_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="cash_flow_statement_data", component_property='children'),
     Input(component_id="cash_flow_statement", component_property="value")])
def display_cash_flow_statement_graphs(companies, data_type, cash_flow_statement_data,
                                       cash_flow_statement):
    if (not companies or companies is None) or cash_flow_statement is None:
        return None

    graphs = []
    data_dump = json.loads(cash_flow_statement_data)
    for item in cash_flow_statement:
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[item]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(item),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': item}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


@app.callback(
    Output(component_id='financial_statement_growth_data', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="period", component_property='value'),
     Input(component_id='financial_statement_growth', component_property='value'),
     Input(component_id='api', component_property='value')])
def collect_financial_statement_growth_data(companies, period, financial_statement_growth, api_key):
    if (not companies or companies is None) or financial_statement_growth is None:
        return None

    financial_statement_growth_data = {}
    for company in companies:
        financial_statement_growth_data[company] = fa.financial_statement_growth(company, api_key,
                                                                                 period=period).to_dict()

    return json.dumps(financial_statement_growth_data)


@app.callback(
    Output(component_id='financial_statement_growth_container', component_property='children'),
    [Input(component_id="companies", component_property='value'),
     Input(component_id="data_type", component_property='value'),
     Input(component_id="financial_statement_growth_data", component_property='children'),
     Input(component_id="financial_statement_growth", component_property="value")])
def display_financial_statement_growth_graphs(companies, data_type, financial_statement_growth_data,
                                              financial_statement_growth):
    if (not companies or companies is None) or financial_statement_growth is None:
        return None

    graphs = []
    data_dump = json.loads(financial_statement_growth_data)
    for item in financial_statement_growth:
        traces = []
        for company in data_dump:
            df = pd.DataFrame(data_dump[company])
            data = df.loc[item]
            scatter = {'x': data.index, 'y': data.values,
                       'name': company, 'type': 'bar'}
            traces.append(scatter)

        graph = dcc.Graph(
            id='graph-{}'.format(item),
            figure={'data': traces,
                    'layout': {
                        'height': 300,
                        'xaxis': {
                            'type': 'category',
                            'categoryorder': 'category ascending'},
                        'yaxis': {
                            'type': data_type},
                        'title': item}},
            config={'displayModeBar': False})

        graphs.append(graph)

    return html.Div(graphs)


if __name__ == '__main__':
    app.run_server(debug=False)
