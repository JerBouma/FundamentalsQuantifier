# Fundamentals Quantifier

This is the source code of the website: https://fundamentals-quantifier.herokuapp.com/
    
The Fundamentals Quantifier is a tool that allows you to visually compare the fundamentals 
of over 6,000 companies. You can filter the companies based on Sector and/or Industry. Thereby, it is possible
to make a selection of companies that are closely related to each other making comparison a valuable insight.
    
> *The key to investing is not assessing how much an industry is going to affect society, or how much it will grow,
> but rather determining the competitive advantage of any given company and, above all,
> the durability of that advantage.* - **Warren Buffet**
    
The following data can be collected for each company (linear and log):
* **Stock Data**: daily adjusted close prices over a 10 year period for each individual company.
* **Key Metrics**: the most important metrics. This includes, among other things, the Price-to-Earnings ratio
and Debt to Equity ratio. All of these metrics can be displayed either annually or quarterly.
* **Financial Ratios**: an extensive list of ratios that covers pretty much all of the most used ratios. This
data can only displayed on an annual basis.
* **Financial Statements**: a collection of financial statements over the last 10 years. You have the option
to display the data annually (10 years) and quarterly (40 quarters). This includes the Balance Sheet Statement,
Income Statement and Cash Flow Statement. Furthermore, growth of each item is also
captured over set time intervals.
    
Thanks to Dash and Plotly, graphs are fully interactive. For example, by clicking the tickers in the legenda,
you can remove (and add) companies from each graph as well as zoom into the graph by making a selection. Data is
collected through the package [FundamentalAnalysis](https://github.com/JerBouma/FundamentalAnalysis).

Note that I am not responsible for any investment loss (or gain) you make thanks to this interface. 