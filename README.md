# Phonepe_Datavisualization
The aim of this project will be a live geo visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. The dashboard will have at least 10 different dropdown options for users to select different facts and figures to display. The data will be stored in a MySQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data.

# Approach
1. Data Extraction
2. Data Transformation
3. Insert data into MYSQL database
4. Data Retrival and Deployment on Streamlit application

# Data Extraction:
Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON. Install the package "gitpython" in your local system to perform the cloning task. After the installization take the clone from the Phonepe github repository and store the JSON file in your local file system.

Phonepe repositary link: https://github.com/PhonePe/pulse/tree/master/data

# Data Transformation:
By using a libraries such as Pandas, os, json and sqlalchemy to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization. The JSON file such as aggregate transaction, aggregate users, map transaction, map users, top transaction and top users are used for the transformation.

# Insertion:
After all the transformation part Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
df.to_sql(name='Agg_Trans', con=engine, if_exists='replace', index=False)

This command is used to connect your SQL database with username and password and then transfer the dataframe to SQL database

# Visualization:
By using the Streamlit libraries develop the application for the data visualization displays the detailed information on Phonepe. For visualization process the plotly.express package plays major role.

Selecting the year to display the total usercount and total transaction for all state by using geojson:

![Screenshot (131)](https://github.com/mouleesh14/Phonepe_Datavisualization/assets/113981901/c647923e-ddbc-477d-bfab-884d205112c3)

Types of Transaction for all years:

![Screenshot (133)](https://github.com/mouleesh14/Phonepe_Datavisualization/assets/113981901/143f6481-fcab-4c9d-b911-d3fc6cb3faf0)

# Tools Used:
1. Python
2. MYSQL workbench
3. Streamlit
4. Spyder

# Packages:
1. gitpython
2. pandas
3. mysql.connector
4. sqlalchemy
5. os
6. streamlit
7. plotly.express
