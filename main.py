import data
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(
                        html.Label("BAW", className="label4"),
                        width=3
                    ),
                    dbc.Col(
                        [
                            html.Label("BINANCE ANALYTICAL WALLET", className="label1"),
                            html.Label("YOUR BINANCE SPOT TRANSACTIONS FOR FOUR SELECTED CRYPTOCURRENCIES",
                                       className="label3",
                                       ),
                            html.Label("OPEN-SOURCE BINANCE WALLET WITH DATA ANALYTICS AND FULL TRANSPARENCY",
                                       className="label3"
                                       ),
                        ],
                        width=6
                    ),
                    dbc.Col(
                        [
                            html.H1(data.roe, className="label2"),
                            html.H1(data.roa, className="label2"),
                        ],
                        width=3, align='right'
                    ),
                ],

            ),
        ),
    ],
)

tab1_content = (
    html.Div(
        [

            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(data.card_1),  # LEFT
                                    ],
                                    sm=4,
                                ),
                                dbc.Col(
                                    [

                                        dbc.Row(data.card_2),  # CENTER
                                    ],
                                    sm=4,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row(data.card_3),  # RIGHT
                                    ],
                                    sm=4,
                                ),
                            ],
                        ),
                    ]
                ),
            ),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        data.card_10,  # LEFT
                                    ],
                                    sm=6,
                                ),
                                dbc.Col(
                                    [
                                        data.card_11,  # RIGHT
                                    ],
                                    sm=6,
                                ),
                            ],
                        ),
                    ]
                ),
            ),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    data.card_4,  # LEFT 1
                                    sm=3,
                                ),
                                dbc.Col(
                                    data.card_5,  # LEFT 2
                                    sm=3,
                                ),
                                dbc.Col(
                                    data.card_6,  # RIGHT 2
                                    sm=3,
                                ),
                                dbc.Col(
                                    data.card_7,  # RIGHT 1
                                    sm=3,
                                ),
                            ],
                        ),
                    ]
                ),
            ),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        data.card_8,  # LEFT
                                    ],
                                    sm=6,
                                ),
                                dbc.Col(
                                    data.card_9,  # RIGHT
                                    sm=6,
                                ),
                            ],
                        ),
                    ]
                ),
            ),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        data.card_15,  # CENTER
                                    ],
                                    sm=12,
                                ),
                            ],
                        ),
                    ]
                ),
            ),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        data.card_12,  # LEFT
                                    ],
                                    sm=4,
                                ),
                                dbc.Col(
                                    [
                                        data.card_13,  # CENTER
                                    ],
                                    sm=4,
                                ),
                                dbc.Col(
                                    [
                                        data.card_14,  # RIGHT
                                    ],
                                    sm=4,
                                ),
                            ],
                        ),
                    ]
                ),
            ),

        ]
    ),
)

app.layout = dbc.Container(
    [
        navbar,
        dbc.Tabs(
            [
                dbc.Tab(tab1_content, label="Wallet"),
            ],
        ),
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
