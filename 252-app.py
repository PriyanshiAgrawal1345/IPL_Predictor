import tkinter as tk
import pickle
import pandas as pd

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

pipe = pickle.load(open('pipe.pkl', 'rb'))

root = tk.Tk()
root.title('IPL Win Predictor')

title=tk.Label(root,text="IPL WIN PREDICTOR",bg='blue',fg='white')
title.pack()

Target=tk.StringVar()
Score=tk.StringVar()
Overs=tk.StringVar()
Wickets=tk.StringVar()
Target.set(" ")
Score.set(" ")
Overs.set(" ")
Wickets.set(" ")

batting_team_var = tk.StringVar(root)
batting_team_var.set("Select Batting Team")
batting_team_dropdown = tk.OptionMenu(root, batting_team_var, *sorted(teams))
batting_team_dropdown.config(bg="light blue",fg="black")
batting_team_dropdown.pack()


bowling_team_var = tk.StringVar(root)
bowling_team_var.set("Select Bowling Team")
bowling_team_dropdown = tk.OptionMenu(root, bowling_team_var, *sorted(teams))
bowling_team_dropdown.config(bg="light blue",fg="black")
bowling_team_dropdown.pack()

selected_city_var = tk.StringVar(root)
selected_city_var.set("Select City")
selected_city_dropdown = tk.OptionMenu(root, selected_city_var, *sorted(cities))
selected_city_dropdown.config(bg="light blue",fg="black")
selected_city_dropdown.pack()

target_Label = tk.Label(root,text="Enter Target")
target_entry = tk.Entry(root,textvariable=Target)
target_Label.config(bg="light blue",fg="black")
target_Label.pack()
target_entry.pack()

score_Label = tk.Label(root,text="Enter Score")
score_entry = tk.Entry(root,textvariable=Score)
score_Label.config(bg="light blue",fg="black")
score_Label.pack()
score_entry.pack()

overs_Label = tk.Label(root,text="Enter Overs")
overs_entry = tk.Entry(root,textvariable=Overs)
overs_Label.config(bg="light blue",fg="black")
overs_Label.pack()
overs_entry.pack()

wickets_Label = tk.Label(root,text="Enter Wickets")
wickets_entry = tk.Entry(root,textvariable=Wickets)
wickets_Label.config(bg="light blue",fg="black")
wickets_Label.pack()
wickets_entry.pack()

result_label1 = tk.Label(root, text="")
result_label1.pack()
result_label2 = tk.Label(root, text="")
result_label2.pack()

def predict_probability():
    batting_team = batting_team_var.get()
    bowling_team = bowling_team_var.get()
    selected_city = selected_city_var.get()
    target = int(target_entry.get())
    score = int(score_entry.get())
    overs = float(overs_entry.get())
    wickets = int(wickets_entry.get())

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    result_label1.config(text=f"{batting_team} - {round(win*100)}%")
    result_label2.config(text=f"{bowling_team} - {round(loss*100)}%")

predict_button = tk.Button(root, text="Predict Probability", command=predict_probability,bg="orange",fg="black")
predict_button.pack()

root.mainloop()


