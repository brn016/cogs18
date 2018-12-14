"""A collection of functions for doing my project."""

#Loading and viewing data -- confirming it matches template 
def load_data_template():
    print("Please ensure your data matches template format")
    
    #Cue user to check template to compare data loaded using panda
    confirm = input("Does your data match the template folder? (Y/N): ")
    if confirm == "Y":
        True
    elif confirm == "N":
        print("Please review the template and make changes before visualization attempt")
    else:
        print("Invalid reponse. Please review template. Program will attempt mapping.")



def sum_violence_day(analyze_day):
    
    #load_data_template()
    #Uncomment above line if you want to interact with program. 
    #Was told that admins didn't want to have to input value during grading. 
    #Program will run without this check just fine.
    
    #sums the violence for a particular day across the US
    locations = gun_csv.groupby("state").first()    
    locations = locations.loc[:, ["lat_incident","lng_incident","city"]]
    sum_day = gun_csv[gun_csv["day"] == analyze_day]
    
    #counts incidents on specific day and classifies it to location
    incidents_total =  sum_day.groupby("state").count()
    incidents_total = incidents_total.iloc[:,[0]]
    incidents_total.columns= ["Incidents Today"]

    #Return number of cases at location
    no_cases = incidents_total.join(locations)
    return no_cases



def visual_incidents(no_cases):
    #making US map and adding points to plot violence
    folium_map = folium.Map(location=[40, -97],
                            zoom_start=4,
                            tiles='Mapbox Control Room')
    
    #point map creation and marking
    for x, row in no_cases.iterrows():
        gun_violence = (row["Incidents Today"]) #total violence
        
        #Elements of the interact ive map
        popup_text = "{}<br> total incidents: {}"        
        popup_text = popup_text.format(row["city"], gun_violence)
        
        radius = gun_violence*10
        
        # choose the color of the marker
        if gun_violence>0:
            color="#E37222"
        else:           
            color="#0A8A9F"
        
        # add marker to the map
        folium.CircleMarker(location=(row["lat_incident"],
                                      row["lng_incident"]),
                            radius=radius,
                            color=color,
                            popup=popup_text,
                            fill=True).add_to(folium_map)
    return folium_map
