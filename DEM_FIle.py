import requests
import pandas as pd
import streamlit as st

st.title("Extracting DEM for Use")
st.text("define box:http://bboxfinder.com/")
container = st.container()
with st.sidebar:
    south_input = st.text_input('South Bound (e.g 50)', 'South Coordinates')
    north_input = st.text_input('North Bound (e.g 51.5)', 'North Coordinates')
    west_input = st.text_input('West Bound (e.g -91)', 'West Coordinates')
    east_input = st.text_input('East Bound (e.g -90)', 'East Coordinates')

    if st.button('Show Bounds'):
        south = float(south_input)
        north = float(north_input)
        west = float(west_input)
        east = float(east_input)
        xbounds = [south,south,north,north] #creating extent of map
        ybounds = [east,west,east,west]
        df = pd.DataFrame(data={'lat':xbounds,'lon':ybounds})
        container.map(df) # create a world map using the points
    
    if st.button('Download DEM'):
        url = 'https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&south='+south_input+'&north='+north_input+'&west='+west_input+'&east='+east_input+'&outputFormat=GTiff&API_Key=31e0bfd3cfe809e96ce34e28377a2165'
        response = requests.get(url)
        open('raster.tif','wb').write(response.content)
        st.write("Downloaded Successful")