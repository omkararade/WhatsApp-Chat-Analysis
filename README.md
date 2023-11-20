# WhatsApp-Chat-Analysis
This WhatsApp chat analysis program takes a chat export file and generates visualizations. It calculates user activity metrics, analyzes temporal and content patterns, and creates visualizations using various libraries. The interactive web application allows users to select specific users and customize visualizations.


This is a Python program that analyzes and visualizes WhatsApp chat data. It can be used to track individual user activity, identify trends, and generate word clouds.

The program takes a WhatsApp chat export file as input and generates a number of visualizations, including:

A bar chart shows the total number of messages, words, media messages, and links shared by each user.
A heatmap shows the most active days and times for each user.
A word cloud shows the most common words used by each user.
A pie chart showing the most common emojis used by each user
A line chart shows the number of messages sent by each user over time.
A heatmap showing the activity levels of all users throughout the week
The program is written in Python and uses the following libraries:

Streamlit is a Python library for creating interactive web applications.
Matplotlib is a Python library for plotting data.
Seaborn: A Python library for statistical data visualization
Preprocessor: A custom Python library for cleaning and preprocessing WhatsApp chat data.
Helper: A custom Python library for generating visualizations from WhatsApp chat data.
To use the program, follow these steps:

Install the required libraries.
Download the WhatsApp chat export file.
Run the program.
Select the WhatsApp chat export file.
Select the user you want to analyze.
Click the "Show Analysis" button.
View the visualizations.


Data Acquisition:
User Input: The program starts by prompting the user to select a WhatsApp chat export file.
File Upload: The user uploads the selected chat export file.
File Processing: The program reads the chat export file and extracts the relevant data, including message timestamps, sender names, message content, media content, and links.

Data Preprocessing:
Data Cleaning: The program cleans the extracted data by removing irrelevant characters, converting timestamps to appropriate formats, and handling emojis correctly.
Data Structuring: The cleaned data is structured into a Pandas data frame for efficient analysis and manipulation.

Data Analysis:
User Activity: The program calculates various user activity metrics, such as total messages sent, total words used, number of media messages, and number of links shared.
Temporal Analysis: The program analyzes the temporal distribution of messages, identifying peak activity periods and trends over time.
Content Analysis: The program analyzes the content of messages, identifying common words, emojis, and patterns in language usage.

Visualization:
Top Statistics: The program generates a summary of key user activity statistics using bar charts and labels.
Activity Maps: The program generates heat maps to visualize user activity patterns across different days and weeks.
Word Clouds: The program generates word clouds to visualize the most frequently used words by each user.
Emoji Analysis: The program visualizes the most common emojis used by each user using pie charts and tables.
Timelines: The program generates line charts to visualize the number of messages sent by each user over time, providing insights into their messaging patterns.
Weekly Activity Heatmap: The program generates a heatmap to visualize the overall activity levels of all users throughout the week.

User Interaction:
Streamlit Interface: The program utilizes the Streamlit library to create an interactive web application, allowing users to select the user they want to analyze and view the corresponding visualizations.
Visualization Controls: The program provides interactive elements, such as filters and drop-down menus, to enable users to customize their analysis and focus on specific aspects of the data.
