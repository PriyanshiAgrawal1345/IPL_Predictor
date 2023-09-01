import tkinter as tk
import pickle
import numpy as np

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

# Load the model
pipe = pickle.load(open('lr-model.pkl', 'rb'))

# Create the Tkinter window
root = tk.Tk()
root.title('IPL Score Predictor')

title=tk.Label(root,text="IPL Score Predictor",bg='blue',fg='white')
title.pack()

# Function to predict the score
def predict_score():
    batting_team = batting_team_var.get()
    bowling_team = bowling_team_var.get()
    overs = float(overs_entry.get())
    wickets = int(wickets_entry.get())
    runs = int(runs_entry.get())
    runs_in_prev_5 = int(runs_in_prev_5_entry.get())
    wickets_in_prev_5 = int(wickets_in_prev_5_entry.get())

    # Create a list for the input features
    temp_array = []

    # Batting Team
    if batting_team == 'Chennai Super Kings':
      temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'Delhi Daredevils':
      temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'Kings XI Punjab':
      temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'Kolkata Knight Riders':
      temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'Mumbai Indians':
      temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'Rajasthan Royals':
      temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'Royal Challengers Bangalore':
      temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'Sunrisers Hyderabad':
      temp_array = temp_array + [0,0,0,0,0,0,0,1]

    # Bowling Team
    if bowling_team == 'Chennai Super Kings':
      temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'Delhi Daredevils':
      temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'Kings XI Punjab':
      temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'Kolkata Knight Riders':
      temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'Mumbai Indians':
      temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'Rajasthan Royals':
      temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'Royal Challengers Bangalore':
      temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'Sunrisers Hyderabad':
      temp_array = temp_array + [0,0,0,0,0,0,0,1]

    
    temp_array.extend([overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5])

    # Convert the list into a numpy array
    input_array = np.array([temp_array])

    # Perform the prediction using the loaded model
    score_prediction = int(pipe.predict(input_array)[0])
    
    
    # Display the predicted score
    result_label.config(text=f"The predicted score is: {score_prediction}")

# Create labels and entry fields for user input
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

overs_label = tk.Label(root, text="Overs played:")
overs_label.pack()
overs_entry = tk.Entry(root)
overs_label.config(bg="light blue",fg="black")
overs_entry.pack()

wickets_label = tk.Label(root, text="Wickets done:")
wickets_label.pack()
wickets_entry = tk.Entry(root)
wickets_label.config(bg="light blue",fg="black")
wickets_entry.pack()

runs_label = tk.Label(root, text="Runs obtained:")
runs_label.pack()
runs_entry = tk.Entry(root)
runs_label.config(bg="light blue",fg="black")
runs_entry.pack()

runs_in_prev_5_label = tk.Label(root, text="Runs in Previous 5 Overs:")
runs_in_prev_5_label.pack()
runs_in_prev_5_entry = tk.Entry(root)
runs_in_prev_5_label.config(bg="light blue",fg="black")
runs_in_prev_5_entry.pack()

wickets_in_prev_5_label = tk.Label(root, text="Wickets in Previous 5 Overs:")
wickets_in_prev_5_label.pack()
wickets_in_prev_5_entry = tk.Entry(root)
wickets_in_prev_5_label.config(bg="light blue",fg="black")
wickets_in_prev_5_entry.pack()

predict_button = tk.Button(root, text="Predict Score", command=predict_score,bg="orange",fg="black")
predict_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()