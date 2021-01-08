import requests
import json
import pandas as pd

def launch_info():
    x = input('> ')
    url = 'https://api.spacex.land/graphql/'
    query = """{
    launch(id: """ + '"'+ x + '"' + """) {
        rocket {
        rocket_name
        rocket_type
        }
        launch_date_utc
        launch_year
        launch_site {
        site_name
        }
        launch_success
        details
    }
    }"""


    res = requests.post(url, json={'query' : query})
    data = json.loads(res.text)
    #fdata stands for Formated Data, it requires less input, etc I don't really know the terminology for this
    fdata = data['data']['launch']

    rocket = fdata['rocket']['rocket_name']
    launch_date = fdata['launch_date_utc']
    launch_site = fdata['launch_site']['site_name']
    launch_success = fdata['launch_success']
    details = fdata['details']

    return f"""
Rocket: {rocket}
Launch Date: {launch_date}
Launch Site: {launch_site}
Launch Success: {launch_success}

Details:
    
    {details} """


def launch_info_var():
    x = input('> ')
    url = 'https://api.spacex.land/graphql/'
    query = """{
    launch(id: """ + '"'+ x + '"' + """) {
        rocket {
        rocket_name
        rocket_type
        }
        launch_date_utc
        launch_year
        launch_site {
        site_name
        }
        launch_success
        details
    }
    }"""


    res = requests.post(url, json={'query' : query})
    data = json.loads(res.text)
    #fdata stands for Formated Data, it requires less input, etc I don't really know the terminology for this
    fdata = data['data']['launch']

    rocket = fdata['rocket']['rocket_name']
    launch_date = fdata['launch_date_utc']
    launch_site = fdata['launch_site']['site_name']
    launch_success = fdata['launch_success']
    details = fdata['details']

    return rocket, launch_date, launch_site, launch_success, details