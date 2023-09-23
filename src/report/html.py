def generate(extreme_buy, can_buy, stock_data_dict):
    html = """<!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
        border: 1px solid black;
    }
    </style>
    </head>
    <body>"""

    if extreme_buy:
        html += """<h2>Extreme Buy</h2>
        <table>
            <tr>
                <th>Ticker</th>
                <th>Stock Price</th>
                <th>Score</th>
            </tr>"""
        for ticker in extreme_buy:
            html += "<tr><td>{}</td><td>{}</td><td>{:.2f}</td></tr>".format(ticker, stock_data_dict[ticker]['stock_price'], stock_data_dict[ticker]['score'])
        html += "</table>"

    if can_buy:
        html += """<h2>Can Buy</h2>
        <table>
            <tr>
                <th>Ticker</th>
                <th>Stock Price</th>
                <th>Score</th>
            </tr>"""
        for ticker in can_buy:
            html += "<tr><td>{}</td><td>{}</td><td>{:.2f}</td></tr>".format(ticker, stock_data_dict[ticker]['stock_price'], stock_data_dict[ticker]['score'])
        html += "</table>"

    html += """</body>
    </html>"""

    if extreme_buy or can_buy:
      with open('report.html', 'w') as f:
          f.write(html)
