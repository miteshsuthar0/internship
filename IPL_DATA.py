import pandas as pd
import numpy as np
from dash import Dash, html, dash_table, dcc, callback, Input, Output
import plotly.express as px
import matplotlib.pyplot as plt
import dash_mantine_components as dmc
import csv
import seaborn as sns


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)


df = pd.read_csv("each_ball_records.csv")
x = df["bowler"].groupby(df["outcome"])
# print(x.get_group("w").count())
powerplay = df['ballnumber'][:37].count()
# print(sum(df["outcome"].count() for i in range(powerplay) ))

df = df.drop('comment',axis=1)
# match_num = int(input("Enter the match number( between 1 to 74 ) :"))
# match1 = df[df['match_no'] == match_num]
#
# inp = int(input("Enter which innings  do you want (1 or 2) : "))
# balls_played1 = match1[match1['inningno'] == inp]
# # balls_played2 = len(match1[match1['inningno'] == 2])
# # print(type(balls_played1))
#
# assd = balls_played1.loc[:,['index','score']]
# print(assd)
# # for i in balls_played1['ballnumber']:
# #     print(assd)


# at = (df["ballnumber"].count())
# print(at)
First_inning_Outcome = df["outcome"][:121]
First_inning_bowler_data = df["bowler"][:121]
First_inning_batter_data = df["batter"][:121]
First_inning_batting_score = df["score"][:121]
First_inning_Overs = df["over"][:121]

Current_season_Outcome = df["outcome"][:242]
Current_season_bowler_data = df["bowler"][:242]
Current_season_batter_data = df["batter"][:242]
Current_season_batting_score = df["score"][:242]
Current_season_Overs = df["over"][:242]


PowerPlay_Outcome = df["outcome"][:37]
PowerPlay_batter_data = df["batter"][:37]
PowerPlay_batting_score = df["score"][:37]
PowerPlay_Overs = df["over"][:37]
PowerPlay_bowler_data = df["bowler"][:37]

Dead_Over_Outcome = df["outcome"][97:121]
Dead_Over_batter_data = df["batter"][97:121]
Dead_Over_batting_score = df["score"][97:121]
Dead_Over_Overs = df["over"][97:121]
Dead_Over_bowler_data = df["bowler"][97:121]

Middle_order_Overs_Outcome = df["outcome"][37:97]
Middle_order_Overs_batter_data = df["batter"][37:97]
Middle_order_Overs_batting_score = df["score"][37:97]
Middle_order_Overs_Overs = df["over"][37:97]
Middle_order_Overs_bowler_data = df["bowler"][37:97]

# print(Dead_Over_batting_score.sum())

Total_score_first_inning = sum(First_inning_batting_score)
Total_score_PowerPlay = sum(PowerPlay_batting_score)
Total_score_Dead_Over = sum(Dead_Over_batting_score)
Total_score_Middle_order_Overs = sum(Middle_order_Overs_batting_score)
# print(s)

# v = df['score'].groupby(df['batter']).get_group('Ruturaj Gaikwad')
# # print(v)
#
# x1 = df.groupby(df['batter']).get_group('Ruturaj Gaikwad')[:50]
# x = df['score'].groupby(df['batter']).get_group('Ruturaj Gaikwad')
#
# cv = df["score"].value_counts("6").groupby(df["batter"]).get_group("Ruturaj Gaikwad")
#
# xa = player = df[df["outcome"] == '6']
# ca = player['batter'].value_counts()
#
# mm = xa.groupby(df['batter']).get_group('Ruturaj Gaikwad')
#
# # df['count'] =
# ()
# for i in df['score'].items():
#     if i == 6:
#         print(i)

df["wickets"] = df["outcome"].str.contains('w',case = False).astype(int)
wickets = df["wickets"][:121]

df["sixes"] = df["outcome"].str.contains('6',case = False).astype(int)
sixes = df["sixes"][:121]

df["Fours"] = df["outcome"].str.contains('4',case = False).astype(int)
Fours = df["Fours"][:121]

# print(mm)
# print(ca)
# print(First_inning_batter_data)
app = Dash(__name__)

app.layout = html.Div([

    # my_input := dcc.RadioItems(options=['PowerPlay', 'Middle', 'Dead'], value='PowerPlay'),
    html.Div(children="My Project"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15),

    html.Div([
        html.Div(children="Pie Chart of bowlers vs. total runs given by them in PowerPlay.",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, PowerPlay_bowler_data, PowerPlay_batting_score)),
        html.Div(children="Pie Chart of batsman vs. total runs scored by them in PowerPlay .",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, PowerPlay_batter_data, PowerPlay_batting_score)),
        dcc.Graph(figure=px.bar(df, PowerPlay_batting_score, PowerPlay_batter_data)),
        html.Div(children="Chart to show in which manner runs are scored in PowerPlay : ",
                 style={'textAlign': 'center', 'fontSize': 28}),
        dcc.Graph(figure=px.histogram(df, x=df["outcome"][:37], y=df['over'][:37], histfunc='count')),
        html.Div(children=f"Total runs scored in PowerPlay : {Total_score_PowerPlay}", style={'fontSize': 26}), ]),
        # dcc.Graph(figure=px.pie(df,"rg_balls" ,'rg_score' )),

    html.Div([
        # html.Div(children="Ruturaj Gaikwad"),
        # dcc.Graph(figure=px.histogram(df,x=(df['score'].groupby(df['batter']).get_group('Ruturaj Gaikwad')[:122]),y= (df['ballnumber'].groupby(df['batter']).get_group('Ruturaj Gaikwad')[:122]),histfunc="count")),

        html.Div(children="Pie Chart of bowlers vs. total runs given by them in Middle overs.",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, Middle_order_Overs_bowler_data, Middle_order_Overs_batting_score)),
        html.Div(children="Pie Chart of batsman vs. total runs scored by them in Middle Overs .",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, Middle_order_Overs_batter_data, Middle_order_Overs_batting_score)),
        dcc.Graph(figure=px.bar(df, Middle_order_Overs_batting_score, Middle_order_Overs_batter_data)),
        html.Div(children="Chart to show in which manner runs are scored in Middle Overs : ",
                 style={'textAlign': 'center', 'fontSize': 28}),
        dcc.Graph(figure=px.histogram(df, x=df["outcome"][37:97], y=df['over'][37:97], histfunc='count')),
        html.Div(children=f"Total runs scored in Middle Overs : {Total_score_Middle_order_Overs}",
                 style={'fontSize': 26}),
    ]),

    html.Div([
        html.Div(children="Pie Chart of bowlers vs. total runs given by them in DeadOver.",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, Dead_Over_bowler_data, Dead_Over_batting_score)),
        html.Div(children="Pie Chart of batsman vs. total runs scored by them in DeadOver .",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, Dead_Over_batter_data, Dead_Over_batting_score)),
        dcc.Graph(figure=px.bar(df, Dead_Over_batting_score, Dead_Over_batter_data)),
        html.Div(children="Chart to show in which manner runs are scored in Dead Overs : ",
                 style={'textAlign': 'center', 'fontSize': 28}),
        dcc.Graph(figure=px.histogram(df, x=df["outcome"][97:121], y=df['over'][97:121], histfunc='count')),
        html.Div(children=f"Total runs scored in DeadOvers : {Total_score_Dead_Over}", style={'fontSize': 26}),
    ]),

    html.Div([

        html.Div(children="Pie Chart of bowlers vs. total runs given by them 1st inning.",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.pie(df, First_inning_bowler_data, First_inning_batting_score)),
        html.Div(children="Histogram of batsman vs. total runs scored by them in 1st inning .",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = First_inning_batter_data ,y = First_inning_batting_score)),
        html.Div(children="Histogram of bowlers vs. Wickets in 1st inning",style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = First_inning_bowler_data,y = wickets)),
        html.Div(children="Histogram of Batsmen vs. sixes hit by them in 1st Inning",style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = First_inning_batter_data, y = sixes )),
        html.Div(children="Histogram of Batsmen vs. Fours hit by them in 1st Inning",style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = First_inning_batter_data, y = Fours )),
        html.Div(children="Each batsman's bowl-to-bowl data : "),
        dcc.Graph(figure=px.bar(df, First_inning_batting_score, First_inning_batter_data)),
        html.Div(children="Runs made in each over : ",style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = First_inning_Overs, y = First_inning_batting_score,histfunc="sum")),
        html.Div(children="Chart to show in which manner runs are scored in whole 1st inning : ",
                 style={'textAlign': 'center', 'fontSize': 28}),
        dcc.Graph(figure=px.histogram(df, x=df["outcome"][:121], y=df['over'][:121], histfunc='count')),
        html.Div(children=f"Total runs scored in 1st innings : {Total_score_first_inning}", style={'fontSize': 26}),
    ]),

    html.Div([

        html.Div(children="Pie Chart of bowlers vs. total runs given by them in whole season.",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df,x = Current_season_bowler_data ,y = Current_season_batting_score  )),
        html.Div(children="Pie Chart of batsman vs. total runs scored by them in Whole Season .",
                 style={'textAlign': 'center', 'fontSize': 30}),
        dcc.Graph(figure=px.histogram(df, x=Current_season_batter_data, y=Current_season_batting_score)),
        dcc.Graph(figure=px.bar(df, x= Current_season_batting_score, y = Current_season_batter_data)),
        html.Div(children="Chart to show in which manner runs are scored in whole Season : ",
                 style={'textAlign': 'center', 'fontSize': 28}),
        dcc.Graph(figure=px.histogram(df, x=df["outcome"][:121], y=df['over'][:121], histfunc='count')),
        # html.Div(children=f"Total runs scored in 1st innings : {}", style={'fontSize': 26}),
    ]),
])


# @callback(
#     Output(my_output1, 'children'),
#     Input(my_input, 'value')
# )
# def update_graph(input_value):
#     return f"output : {input_value}"


if __name__ == '__main__':
    app.server.run(debug=True)
