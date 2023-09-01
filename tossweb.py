import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Function to predict the toss winner
def predict_toss():
    # Read the CSV file
    df = pd.read_csv('matches.csv')

    # Filter the relevant columns
    df = df[['team1', 'team2', 'toss_winner', 'toss_decision']]

    # Drop rows with missing values
    df = df.dropna()

    # Prepare the data
    X = df[['team1', 'team2', 'toss_decision']]
    y = df['toss_winner']
    #print(X)
    # Convert categorical variables to numerical using one-hot encoding
    X_encoded = pd.get_dummies(X, drop_first=True)
    #print(X_encoded.columns)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Create a logistic regression model and fit it to the training data
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make prediction on the provided team combination and toss decision
    team1 = 'Sunrisers Hyderabad'
    team2 = 'Mumbai Indians'
    toss_decision = 'bat'
    
    
    input_data = pd.DataFrame([[team1, team2, toss_decision],], columns=X.columns)
    #print(input_data)
    input_data_encoded = pd.get_dummies(input_data, drop_first=True)
    #print(input_data_encoded)
    prediction = model.predict(input_data_encoded)
    print(prediction)
    # Display the predicted toss winner
    ##prediction_label.config(text=f"The predicted toss winner is: {prediction[0]}")\
        
predict_toss()
'''
# Create the Tkinter window
window = tk.Tk()
window.title('Toss Predictor')

title=tk.Label(window,text="Toss Predictor",bg='blue',fg='white')
title.pack()
'''
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
'''
# Create team input labels and entry fields
team1_label = tk.Label(window, text='Team 1:')
team1_label.pack()
team1_var=tk.StringVar(window)
team1_var.set("Select Team1")
team_1_dropdown=tk.OptionMenu(window,team1_var,*sorted(teams))
team_1_dropdown.config(bg="light blue",fg="black")
team_1_dropdown.pack()

team2_label = tk.Label(window, text='Team 2:')
team2_label.pack()
team2_var=tk.StringVar(window)
team2_var.set("Select Team2")
team_2_dropdown=tk.OptionMenu(window,team2_var,*sorted(teams))
team_2_dropdown.config(bg="light blue",fg="black")
team_2_dropdown.pack()

# Create toss decision radio buttons
toss_decision_label = tk.Label(window, text='Toss Decision:')
toss_decision_label.pack()

toss_decision_var = tk.StringVar()
toss_decision_var.set('Bat') 

toss_decision_bat = tk.Radiobutton(window, text='Bat', variable=toss_decision_var, value='bat')
toss_decision_bat.pack()

toss_decision_field = tk.Radiobutton(window, text='Field', variable=toss_decision_var, value='field')
toss_decision_field.pack()

# Create predict button
predict_button = tk.Button(window, text='Predict', command=predict_toss)
predict_button.pack()

# Create label for displaying the prediction
prediction_label = tk.Label(window, text="")

prediction_label.pack()

# Run the Tkinter event loop
window.mainloop()
'''