'''import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np
import pandas as pd

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}
        for F in (Home,Win_Predictor,Score_Predictor):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Home")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Toss_Predictor",
        command = lambda : controller.show_frame(Toss_Predictor))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Win_Predictor",
        command = lambda : controller.show_frame(Win_Predictor))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Score_Predictor",
        command = lambda : controller.show_frame(Score_Predictor))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)



class Win_Predictor(tk.Frame):
    def __init__(self, parent, controller):
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
        
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Win_Predictor")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Toss_Predictor",
                            command = lambda : controller.show_frame(Toss_Predictor))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Score_Predictor",
        command = lambda : controller.show_frame(Score_Predictor))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        
class Score_Predictor(tk.Frame):
    def __init__(self, parent, controller):
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
        
        
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Score_Predictor")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Toss_Predictor",
                            command = lambda : controller.show_frame(Toss_Predictor))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Win_Predictor",
        command = lambda : controller.show_frame(Win_Predictor))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        
app=tkinterApp()
app.mainloop()'''



import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle

# Load the machine learning model for score prediction
model = pickle.load(open('lr-model.pkl', 'rb'))

# Load the IPL match data
matches_df = pd.read_csv('matches.csv')
deliveries_df = pd.read_csv('deliveries.csv')

def predict_score():
    batting_team = batting_team_entry.get()
    bowling_team = bowling_team_entry.get()
    overs_played = float(overs_played_entry.get())
    wickets_taken = int(wickets_taken_entry.get())
    runs_obtained = int(runs_obtained_entry.get())
    runs_prev_5_overs = int(runs_prev_5_overs_entry.get())
    wickets_prev_5_overs = int(wickets_prev_5_overs_entry.get())

    # Perform data processing and feature engineering
    # ...

    # Predict the score using the machine learning model
    # score_prediction = model.predict(...)
    score_prediction = 250  # Placeholder for demonstration

    messagebox.showinfo('Score Prediction', f'Predicted Score: {score_prediction}')

def perform_analysis():
    # Perform IPL match analysis using matches_df and deliveries_df
    # ...

    messagebox.showinfo('Analysis Results', 'Analysis results go here')

# Create the main window
window = tk.Tk()
window.title('IPL Score Predictor and Analysis')
window.geometry('400x300')

# Create the input fields and labels for score prediction
batting_team_label = tk.Label(window, text='Batting Team:')
batting_team_label.pack()
batting_team_entry = tk.Entry(window)
batting_team_entry.pack()

bowling_team_label = tk.Label(window, text='Bowling Team:')
bowling_team_label.pack()
bowling_team_entry = tk.Entry(window)
bowling_team_entry.pack()

overs_played_label = tk.Label(window, text='Overs Played:')
overs_played_label.pack()
overs_played_entry = tk.Entry(window)
overs_played_entry.pack()

wickets_taken_label = tk.Label(window, text='Wickets Taken:')
wickets_taken_label.pack()
wickets_taken_entry = tk.Entry(window)
wickets_taken_entry.pack()

runs_obtained_label = tk.Label(window, text='Runs Obtained:')
runs_obtained_label.pack()
runs_obtained_entry = tk.Entry(window)
runs_obtained_entry.pack()

runs_prev_5_overs_label = tk.Label(window, text='Runs in Previous 5 Overs:')
runs_prev_5_overs_label.pack()
runs_prev_5_overs_entry = tk.Entry(window)
runs_prev_5_overs_entry.pack()

wickets_prev_5_overs_label = tk.Label(window, text='Wickets in Previous 5 Overs:')
wickets_prev_5_overs_label.pack()
wickets_prev_5_overs_entry = tk.Entry(window)
wickets_prev_5_overs_entry.pack()

predict_button = tk.Button(window, text='Predict Score', command=predict_score)
predict_button.pack()

# Create the button for analysis
analysis_button = tk.Button(window, text='Perform Analysis', command=perform_analysis)
analysis_button.pack()

# Run the Tkinter event loop
window.mainloop()