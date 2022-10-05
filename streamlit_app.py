import streamlit

streamlit.title('My New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('Kale, Spinach & Rocket Smoothie 🥗 ')
streamlit.text('Hard-Boiled & Free-Range Eggs 🐔')
streamlit.text('Avocado Toast 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Pick list to pick the fruit / ending chooses specific item

streamlit.multiselect( "Pick your fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'] )

#Display

streamlit.dataframe(my_fruit_list)
