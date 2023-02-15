import streamlit as st
import pandas as pd

# Define the coordinates for the pin
lat = 37.76
lon = -122.4

# Define the video URL
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# Create a dictionary to store the pin coordinates and video URL
data = {'lat': [lat], 'lon': [lon], 'video_url': [video_url]}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the map with the pin
selected_pin = st.map(df)

# Check if the pin has been clicked
# if selected_pin is not None:
    # If the pin has been clicked, get the video URL
selected_video_url = video_url
    # Display the video
st.video(selected_video_url)
