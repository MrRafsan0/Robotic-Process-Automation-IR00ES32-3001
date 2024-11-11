
Md Rafsan Jany Shad

Shefa Das

# Report on Manual Automation Process in UiPath Studio

## Introduction
This report explains how I created a manual automation process in UiPath Studio to search for resources on the HAMK library website.

## Steps to Create the Automation

1. **Create a New Project:**  
   I opened UiPath Studio and created a new project.

2. **Select Manual Trigger:**  
   I chose a manual trigger so that I can start the automation whenever I want.

3. **Add "Use Browser New Tab" Activity:**  
   I added the "Use Browser New Tab" activity to open a new tab in the web browser.

4. **Set the URL:**  
   In the activity properties, I entered the URL:  
   **URL:** `https://hamk.finna.fi`  
   This takes me to the HAMK library's search page.

5. **Click the Input Field:**  
   I added a click action to select the search input field, identified as **searchForm_lookfor**.

6. **Type the Search Query:**  
   I used the "Type Into" action to enter the search term:  
   **Search Query:** `"Python for dummies"`  
   This simulates typing in the search box.

7. **Add a Delay:**  
   Finally, I added a 5-second delay to allow the search results to load after typing.

This simple automation process helps me quickly search for resources on the HAMK library website. By following these steps, I made the task easier and more efficient.
