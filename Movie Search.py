import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = 'http://www.omdbapi.com/?i=tt3896198&apikey=2e13d8ce'

#Function to fetch movie data
def fetch_movie_data():
    movie = movie_title_entry.get().strip()
    year = year_entry.get().strip()

    if not movie:
        messagebox.showerror("Error", "Please enter a movie title.")
        return


    # Prepare API Request Paramaters
    params = {'t': movie}
    if year:
        if year.isdigit():
            params['y'] = year
        else:
            messagebox.showerror("Error", "Invalid year entered. Please enter a valid year.")
            return

    # Make the API Request
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            # Display the movie details
            result_text.set(
                f"Title: {data['Title']}\n"
                f"Year: {data['Year']}\n"
                f"Genre: {data['Genre']}\n"
                f"IMDB Rating: {data['imdbRating']}\n"
                f"Plot: {data['Plot']}"
            )
        else:
            result_text.set("Movie not found. Please check the title and year")

#GUI Setup
root = tk.Tk()
root.title("Movie Info")

#Labels and Entry Fields
tk.Label(root, text="Movie Title:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
movie_title_entry = tk.Entry(root, width=30)
movie_title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Year:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(root, width=10)
year_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#Search Button
search_button = tk.Button(root, text="Search", command=fetch_movie_data)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

#Result Display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", wraplength=400)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

#Run the GUI
root.mainloop()

