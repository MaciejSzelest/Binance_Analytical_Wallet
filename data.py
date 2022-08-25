from wallet import Binance
import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc

# PARAMETERS: SELECT CRYPTOCURRENCIES ##################################################################################

asset = ['###', '###', '###', '###']                              # PROVIDE FOUR CRYPTOS (EXAMPLE: 'XRP')
trades = ['###USDT', '###USDT', '###USDT', '###USDT']             # PROVIDE FOUR CRYPTOS FROM SPOT ACCOUNT (EXAMPLE: 'XRPUSDT')

fig_dict1 = {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', 'showlegend': True,
             'legend': dict(orientation="h", yanchor='bottom', y=-0.4, xanchor='center', x=0.5),
             'font_color': '#858585', 'margin': dict(l=10, r=10, t=10, b=10)}
fig_dict2 = {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', 'showlegend': False,
             'font_color': '#858585', 'margin': dict(l=10, r=10, t=10, b=10)}


# CLASS: DATA ##########################################################################################################

class Data(object):

    def __init__(self):
        None

    def __str__(self):
        ret = 'Class Data'
        return ret

    def get_data(trades):
        df = pd.DataFrame(columns=['symbol', 'id', 'isBuyer', 'time', 'price_x', 'qty', 'quoteQty', 'factor', 'price_y',
                                   'Profit/Loss Price', 'Holdings', 'Profit/Loss', 'Volume'])
        for _ in trades:
            temp = Binance.account(_)
            df = pd.concat([df, temp], ignore_index=True)
        df.rename(columns={'price_x': 'Purchase Price', 'price_y': 'Current Price', 'qty': 'Amount',
                           'quoteQty': 'Nominal Value', 'time': 'Date', 'symbol': 'Asset'}, inplace=True)
        df['Asset'].replace({trades[0]: asset[0], trades[1]: asset[1], trades[2]: asset[2], trades[3]: asset[3]},
                            inplace=True)
        return df

    def get_wallet(df):
        wallet = df[['Asset', 'Amount', 'Nominal Value', 'Profit/Loss', 'Holdings']].groupby(by='Asset').sum()
        wallet.reset_index(inplace=True)
        return wallet

    def get_crypto(df, symbol):
        ccy = df[df['Asset'] == symbol]
        return ccy

    def get_price(df, symbol):
        ccy = df[df['Asset'] == symbol]
        return ccy

    def get_hist_price(asset):
        df = pd.DataFrame(columns=['Date', 'Price', 'Asset'])
        for _ in asset:
            temp = Binance.hist_price(_)
            df = pd.concat([df, temp], ignore_index=True)
        return df

    def get_card(fig, txt, id_card):
        card = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Label(txt),
                        dcc.Graph(id=id_card, config={'displayModeBar': False}, animate=True,
                                  figure=fig),
                    ]
                )
            ],
            body=True,
            className="card_attributes",
        )
        return card


class Graphs(object):

    def __init__(self):
        None

    def __str__(self):
        ret = 'Class Graphs'
        return ret

    def get_pie(wallet, value):
        fig = px.pie(values=wallet[value], names=wallet['Asset'], template='plotly_dark', height=350,
                     color_discrete_sequence=px.colors.qualitative.Bold).update_layout(fig_dict1)
        return fig

    def get_bar(wallet, x_input, y_input):
        fig = px.bar(wallet, x=x_input, y=y_input, hover_data=['Amount', 'Nominal Value'],
                     color='Asset', barmode="relative", template='plotly_dark', height=350,
                     color_discrete_sequence=px.colors.qualitative.Bold).update_layout(fig_dict2)
        return fig

    def get_scatter(wallet, value):
        fig = px.scatter(wallet, x=value, y='Profit/Loss', color='Asset', size='Purchase Price', template='plotly_dark',
                         height=350,
                         color_discrete_sequence=px.colors.qualitative.Bold).update_layout(fig_dict1)
        return fig

    def get_line(wallet, x_input, y_input):
        fig = px.line(wallet, x=x_input, y=y_input, color='Asset', line_group='Asset', template='plotly_dark',
                      height=350, color_discrete_sequence=px.colors.qualitative.Bold).update_layout(fig_dict1)
        return fig

    def get_area(wallet, x_input, y_input):
        fig = px.area(wallet, x=x_input, y=y_input, color=y_input, template='plotly_dark',
                      height=350, color_discrete_sequence=px.colors.qualitative.Bold).update_layout(fig_dict2)
        return fig

    def get_density_contour(wallet, x_input, y_input):
        fig = px.density_contour(wallet, x=x_input, y=y_input, color='Asset', template='plotly_dark',
                                 height=400, color_discrete_sequence=px.colors.qualitative.Bold).update_layout(
            fig_dict1)
        return fig

    def get_density_heatmap(wallet, x_input, y_input):
        fig = px.density_heatmap(wallet, x=x_input, y=y_input, template='plotly_dark', height=400).update_layout(
            fig_dict1)
        return fig


if __name__ == "__main__":
    print('This is a Data class to get account details and current wallet value')
    input('\n\n Press a key to close')

# DATA: SOURCING #######################################################################################################

data = Data.get_data(trades)
wallet = Data.get_wallet(data)
hist_price = Data.get_hist_price(asset)
crypto_1 = Data.get_crypto(data, asset[0])
crypto_2 = Data.get_crypto(data, asset[1])
crypto_3 = Data.get_crypto(data, asset[2])
crypto_4 = Data.get_crypto(data, asset[3])

# DATA: TEXT ###########################################################################################################

wallet_txt = f'CURRENT BALANCE: {round(wallet["Holdings"].sum(), 2)} USDT'
wallet_pnl_txt = f'PROFIT/LOSS: {round(wallet["Profit/Loss"].sum(), 2)} USDT'
wallet_txt_goal = f'PROJECT GOAL ACHIEVED IN: {round(((wallet["Holdings"].sum()) / 250000) * 100, 2)} %'
crypto_1_txt = f'{asset[0]} PROFIT/LOSS: {round(crypto_1["Profit/Loss"].sum(), 2)} USDT'
crypto_2_txt = f'{asset[1]}  PROFIT/LOSS: {round(crypto_2["Profit/Loss"].sum(), 2)} USDT'
crypto_3_txt = f'{asset[2]}  PROFIT/LOSS: {round(crypto_3["Profit/Loss"].sum(), 2)} USDT'
crypto_4_txt = f'{asset[3]}  PROFIT/LOSS: {round(crypto_4["Profit/Loss"].sum(), 2)} USDT'
roe = f'{round(((wallet["Profit/Loss"].sum()) / (wallet["Nominal Value"].sum())) * 100, 2)} % ROE'
roa = f'{round(((wallet["Profit/Loss"].sum()) / (wallet["Holdings"].sum())) * 100, 2)} % ROA'

# DATA: GRAPHS #########################################################################################################

wallet_pie = Graphs.get_pie(wallet, 'Holdings')
wallet_bar = Graphs.get_bar(wallet, 'Asset', 'Holdings')
wallet_bar_pnl = Graphs.get_bar(wallet, 'Asset', 'Profit/Loss')
wallet_crypto_1 = Graphs.get_area(crypto_1, 'Holdings', 'Profit/Loss')
wallet_crypto_2 = Graphs.get_area(crypto_2, 'Holdings', 'Profit/Loss')
wallet_crypto_3 = Graphs.get_area(crypto_3, 'Holdings', 'Profit/Loss')
wallet_crypto_4 = Graphs.get_area(crypto_4, 'Holdings', 'Profit/Loss')
wallet_scatter = Graphs.get_scatter(data, 'Holdings')
wallet_scatter_pnl = Graphs.get_scatter(data, 'Date')
wallet_line = Graphs.get_line(data, 'Date', 'Volume')
wallet_line_price = Graphs.get_line(data, 'Date', 'Purchase Price')
wallet_line_hist_price = Graphs.get_line(hist_price, 'Date', 'Price')
wallet_contour_amount = Graphs.get_density_contour(data, 'Amount', 'Purchase Price')
wallet_contour_volume = Graphs.get_density_contour(data, 'Volume', 'Purchase Price')
wallet_contour_price = Graphs.get_density_contour(data, 'Current Price', 'Purchase Price')

# DATA: CARDS ##########################################################################################################

card_1 = Data.get_card(wallet_bar, wallet_txt, 'card_1')
card_2 = Data.get_card(wallet_pie, 'WALLET BREAKDOWN', 'card_2')
card_3 = Data.get_card(wallet_bar_pnl, wallet_pnl_txt, 'card_3')
card_4 = Data.get_card(wallet_crypto_1, crypto_1_txt, 'card_4')
card_5 = Data.get_card(wallet_crypto_2, crypto_2_txt, 'card_5')
card_6 = Data.get_card(wallet_crypto_3, crypto_3_txt, 'card_6')
card_7 = Data.get_card(wallet_crypto_4, crypto_4_txt, 'card_7')
card_8 = Data.get_card(wallet_scatter, 'PROFIT/LOSS HOLDINGS SCATTER', 'card_8')
card_9 = Data.get_card(wallet_scatter_pnl, 'PROFIT/LOSS OVERTIME SCATTER', 'card_9')
card_10 = Data.get_card(wallet_line, 'PORTFOLIO GROWTH', 'card_10')
card_11 = Data.get_card(wallet_line_price, 'PURCHASE PRICE VARIATION', 'card_11')
card_12 = Data.get_card(wallet_contour_amount, 'PURCHASE PRICE/AMOUNT DENSITY CONTOURS', 'card_12')
card_13 = Data.get_card(wallet_contour_volume, 'PURCHASE PRICE/VOLUME DENSITY CONTOURS', 'card_13')
card_14 = Data.get_card(wallet_contour_price, 'PURCHASE/CURRENT PRICE DENSITY CONTOURS', 'card_14')
card_15 = Data.get_card(wallet_line_hist_price, 'HISTORICAL PRICE', 'card_15')
