from shiny import render, ui
from ipyleaflet import Map, Marker
import pandas as pd
from shinywidgets import output_widget, render_widget
from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from os.path import join
import plotly.express as px
import matplotlib.pyplot as plt
import ipywidgets as widgets

df = pd.read_csv("data/MergedTeam.csv")
choices = df["Team"].unique().tolist()
choice = df["QB"].tolist()
divisions = df["Division"].unique().tolist()
app_ui = ui.page_fluid(
        ui.panel_title("NFL Stats & Information"),
        ui.navset_card_tab(  
            ui.nav_panel( "NFL Information", ui.markdown("This page gives you information about the team, its location on the map and the logo for that specific team"),
                        ui.page_sidebar(
                            ui.sidebar(
                                ui.input_selectize(
                                    "team",
                                    "Team",
                                    choices=choices,
            ),
            ui.output_text("team_conference"),  
            ui.output_text("team_division"),
            ui.output_text("stadium"),
            ui.output_text("coach"),
            ui.output_image("image"),
            ),
            output_widget("map"), 
            ui.output_data_frame("table"),
            ui.output_text("team_win_percentages"),
            ui.output_text("team_loss_percentages"),
            ),
            ),
            ui.nav_panel("QB Rate Comparisions", ui.markdown("Pick 2 qbs and compare there stats."),
           
                    ui.input_selectize(
                        "qb1",
                          "QB",
                            choices=choice,
                            ),
                    ui.output_text('team_qb1'),
                    ui.input_selectize(
                        "qb2",
                          "QB",
                            choices=choice,
                            ),  
                        ui.output_text('team_qb2'),        
            ui.card(
                output_widget("plot2"),
                
        ),
  
            ),
            ui.nav_panel("QB Stats", ui.markdown("This is the 2023 QB stats and graph."),       
                    ui.input_selectize(
                        "qb",
                          "QB",
                            choices=choice,
                            ),
                        
                        ui.output_text('team_qb'),                  
            
            ui.card(
                output_widget("plot"),
                
        ),
        ui.card(
            ui.output_data_frame("table2"),
        ),

        ),        
    ),
)


def server(input: Inputs, output: Outputs, session: Session): 
    #page 1
    @render_widget 
    def map():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        latitude = selected_team_data.iloc[0]['latitude']
        longitude = selected_team_data.iloc[0]['longitude']
        m = Map(center=(latitude, longitude), zoom=10)
        marker = Marker(location=(latitude, longitude))
        m.add_layer(marker)
        return m
    @render.image 
    def image():
        selected_team = input.team()
        img_path = join("data/nflTeam_logos", f"{selected_team}.png") 
        img = {"src": img_path, "width": "100px"}
        return img
    
    @render.data_frame
    def table():
        selected_team = input.team()
        filtered_df = df[df['Team'] == selected_team]
        filtered_df = filtered_df.drop(columns=['latitude', 'longitude', 'Stadium','Division', 'Conference', 'Coach'])
        return filtered_df

    @render.text
    def team_conference():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        conference = selected_team_data.iloc[0]['Conference']
        return f"Conference: {conference}"

    @render.text
    def team_division():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        division = selected_team_data.iloc[0]['Division']
        return f"Division: {division}"
    
    @render.text
    def stadium():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        division = selected_team_data.iloc[0]['Stadium']
        return f"Stadium: {division}"
    @render.text
    def coach():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        division = selected_team_data.iloc[0]['Coach']
        return f"Head Coach: {division}"
    
    @render.text
    def team_win_percentages():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        wins = selected_team_data.iloc[0]['Wins']
        losses = selected_team_data.iloc[0]['Losses']
        total_games = wins + losses
        win_percentage = (wins / total_games) * 100
        return f"Win Percentage: {win_percentage}%"
    
    @render.text
    def team_loss_percentages():
        selected_team = input.team()
        selected_team_data = df[df['Team'] == selected_team]
        wins = selected_team_data.iloc[0]['Wins']
        losses = selected_team_data.iloc[0]['Losses']
        total_games = wins + losses
        loss_percentage = (losses / total_games) * 100
        return f"Loss Percentage: {loss_percentage}%"


    #Page 2   
    @render.text
    def team_qb1():
        selected_team = input.qb1()
        selected_team_data = df[df['QB'] == selected_team]
        division = selected_team_data.iloc[0]['Team']
        return f"Team QB: {division}"

    
    @render.text
    def team_qb1():
        selected_team = input.qb1()
        selected_team_data = df[df['QB'] == selected_team]
        division = selected_team_data.iloc[0]['Team']
        return f"Team QB: {division}"
    
    @render.text
    def team_qb2():
        selected_team = input.qb2()
        selected_team_data = df[df['QB'] == selected_team]
        division = selected_team_data.iloc[0]['Team']
        return f"Team QB: {division}"

    
    @render_widget
    def plot2():
        selected_qb1 = input.qb1()
        selected_qb2 = input.qb2()

        qb1_data = pd.read_csv(join("data/nflQBStats", f"{selected_qb1}.csv"))
        qb2_data = pd.read_csv(join("data/nflQBStats", f"{selected_qb2}.csv"))

        combined_data = pd.concat([qb1_data.assign(QB=selected_qb1), qb2_data.assign(QB=selected_qb2)])

        lineplot = px.scatter(
            data_frame=combined_data,
            x="WK",
            y="RATE",
            color="QB"
        ).update_layout(
            title={"text": "Passing Yards QB Performance Rate", "x": 0.5},
            yaxis_title="RATE",
            xaxis_title="WK",
        )

        return lineplot

    #page 3
    @render.data_frame
    def table2():
        selected_team = input.qb()
        roster_path = join("data/nflQBStats", f"{selected_team}.csv")
        roster_df = pd.read_csv(roster_path)
        return roster_df
    
    
    @render_widget
    def plot():
        selected_team = input.qb()
        roster_path = join("data/nflQBStats", f"{selected_team}.csv") 
        roster_path = pd.read_csv(join("data/nflQBStats", f"{selected_team}.csv"))
        lineplot = px.scatter(
            data_frame=roster_path,
            x="WK",
            y="RATE",
        ).update_layout(
            title={"text": "Passing Yards QB Performance Rate", "x": 0.5},
            yaxis_title="RATE",
            xaxis_title="WK",
        )
        return lineplot
            
    @render.text
    def team_qb():
        selected_team = input.qb()
        selected_team_data = df[df['QB'] == selected_team]
        division = selected_team_data.iloc[0]['Team']
        return f"Team QB: {division}"
  
app = App(app_ui, server)