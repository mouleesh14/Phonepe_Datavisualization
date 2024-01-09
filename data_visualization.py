import streamlit as st #It is used to create the streamlit application
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector
import plotly.express as px

st.set_page_config(layout='wide',page_title="Phone Pe")

connect= mysql.connector.connect(host="localhost",user="root",password="Moulee009",autocommit=True)
mycursor=connect.cursor()
mycursor.execute("use phonepe")
#table1
query="""select * from agg_trans"""
mycursor.execute(query)
agg_trans=mycursor.fetchall()
agg_trans=pd.DataFrame(data=agg_trans,columns=["State","Year","Quater","Tranaction_Type","Transaction_Count","Transaction_Amount"])
#table2
query="""select * from agg_user"""
mycursor.execute(query)
agg_user=mycursor.fetchall()
agg_user=pd.DataFrame(data=agg_user,columns=["State","Year","Quater","Brand_name","Brand_Count","Brand_Amount"])
#table3
query="""select * from map_trans"""
mycursor.execute(query)
map_trans=mycursor.fetchall()
map_trans=pd.DataFrame(data=map_trans,columns=["State","Year","Quater","District_name","Count","Amount"])
#table4
query="""select * from map_users"""
mycursor.execute(query)
map_user=mycursor.fetchall()
map_user=pd.DataFrame(data=map_user,columns=["State","Year","Quater","District_name","Registered_user","AppOpens"])
#table5
query="""select * from top_trans"""
mycursor.execute(query)
top_trans=mycursor.fetchall()
top_trans=pd.DataFrame(data=top_trans,columns=["State","Year","Quater","District_name","Count","Amount"])
#table6
query="""select * from top_user"""
mycursor.execute(query)
top_user=mycursor.fetchall()
top_user=pd.DataFrame(data=top_user,columns=["State","Year","Quater","District_name","Registered_user"])

st.markdown("<h2><FONT COLOR='#800080'>PhonePe</h2>",unsafe_allow_html=True)
select = option_menu(None,["About","Map","Charts"],orientation="horizontal")

if(select=="About"):
    st.markdown("<h4><FONT COLOR='#BF40BF'>History</h4>",unsafe_allow_html=True)
    st.write("""PhonePe was incorporated in December 2015. In April 2016, the company was acquired by Flipkart and as part of the 
             acquisition, the FxMart license was transferred to PhonePe and rebranded as the PhonePe wallet. PhonePe's founder Sameer Nigam was appointed as the CEO of the company. In August 2016, the company partnered with Yes Bank 
             to launch a UPI-based mobile payment app, based on the government-backed UPI platform.""")
    st.write("""In 2018, PhonePe became the fastest Indian payment app to get a five crore badge on the Google Play Store. The PhonePe app overtook BHIM to become the market leader in UPI transactions in August 2017.
             In 2022, PhonePe became the first UPI TPAP (Third Party Application Providers) App to allow UPI activation through Aadhaar. """)
    st.markdown("<h4><FONT COLOR='#BF40BF'>Ownership</h4>",unsafe_allow_html=True)
    st.write("""In December 2020, Flipkart and PhonePe declared a partial split, with Walmart maintaining its majority ownership in PhonePe and the two entities now functioning independently. 
             In April 2021, PhonePe Wealth Broking Private Limited, a subsidiary of PhonePe, registered with the Securities Exchange Board of India (SEBI) as a Stock Broker and Depository Participant. 
             It holds an ARN from the Association of Mutual Funds of India, enabling the distribution of Mutual Funds.""")
    st.write("""In March 2022, it  was also registered as a Bharat Bill Payment Operating Unit (BBPOU) with the Reserve Bank of India (RBI) under the Bharat Bill Payment Systems (BBPS). 
             In January 2023, PhonePe Technology Services Private Limited, a subsidiary of PhonePe, obtained regulatory approval from the Reserve Bank of India (RBI) to operate as an Account Aggregator.""")
    st.markdown("<h4><FONT COLOR='#BF40BF'>Awards</h4>",unsafe_allow_html=True)
    st.write("""In 2018: Won the UPI Digital Innovation Award from NPCI in 2018.""")
    st.write("""2019: Awarded the 'Best Digital Wallet' initiative at the 8th Annual Indian Retail & eRetail Awards 2019 organised by Zee Business and The Economic Times """)
    st.write("""2021: Won two awards at IAMAI India Digital Awards- Gold for Excellence in Wealth Management (for Mutual Funds category) and Silver for Unstoppable India video""")
    st.write("""2021: Won the ‘Excellence in Insurtech’ award at Assocham's Fintech & Digital Payments Awards 2021""")
    st.write("""2022: PhonePe won ‘Fintech of the Year’ award at BW Festival of Fintech Awards 2022""")
    st.write("""2023: PhonePe won ‘Best Product/Service Innovation - 'End-to-end digital journey for Motor insurance' at ET BFSI Excellence Awards 2022""")
    st.markdown("<h3><FONT COLOR='#BF40BF'>About Project</h4>",unsafe_allow_html=True)
    st.markdown("""<h6>Data extraction:</h6>  <p>Clone the Github using scripting to fetch the data from the
             Phonepe pulse Github repository and store it in a suitable format such as CSV
             or JSON.</p>""",unsafe_allow_html=True)
    st.markdown("""<h6>Data transformation:</h6>  <p>Use a scripting language such as Python, along with
             libraries such as Pandas, to manipulate and pre-process the data. This may
             include cleaning the data, handling missing values, and transforming the data
             into a format suitable for analysis and visualization.</p>""",unsafe_allow_html=True)
    st.markdown("""<h6>Database insertion:</h6> <p>Use the "mysql-connector-python" library in Python to
             connect to a MySQL database and insert the transformed data using SQL
             commands.</p>""",unsafe_allow_html=True)
    st.markdown("""<h6>Deployment:</h6>  <p>The solution is secure, efficient, and user-friendly. Test
             the solution thoroughly and deploy the dashboard publicly, making it
             accessible to users.</p>""",unsafe_allow_html=True)
             
if(select=="Map"):
    st.markdown("<h4><FONT COLOR='#BF40BF'>PhonePe in India</h4>",unsafe_allow_html=True)
    st.write("""PhonePe is a popular digital payment platform in India that enables users to make seamless and secure transactions through their smartphones. Launched in 2015, PhonePe offers a range of services, including peer-to-peer money transfers, bill payments, mobile recharges, and online shopping. The platform operates on the Unified Payments Interface (UPI), allowing users to link their bank accounts for quick and convenient transactions.""")
    state=['Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
    year=list(agg_trans['Year'].unique())
    states=list(agg_trans['State'].unique())
    st.write("")
    c1,c2=st.columns(2)
    with c1:
        st.markdown("<h5><FONT COLOR='#BF40BF'>Total Transaction amount</h4>",unsafe_allow_html=True)
        st.write("""Display total transaction amount by India map for all years and also displays States and total amount """)
        s=st.multiselect("Select the years: ",year,key="select1")
    with c2:
        st.markdown("<h5><FONT COLOR='#BF40BF'>Total User count</h4>",unsafe_allow_html=True)
        st.write("""Display total users count by India map for all years and also displays States and total user count""")
        se=st.multiselect("Select the years: ",year,key="select2")
    if st.button("Submit",key="btn1"):
        for i in s:
            if(i=='2018'):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2018']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='earth'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in- 2018</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2018: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)
                
            if(i=='2019'):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2019']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='blugrn'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in - 2019</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2019: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)

            if(i=='2020'):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2020']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='bluyl'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in - 2020</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2020: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)

                
            if(i=='2021'):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2021']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='balance'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in - 2021</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2021: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)   
            if(i=='2022'):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2022']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='bluered'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in - 2022</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2022: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)
                
            if(i=='2023'):
                c1,c22,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2023']
                    amount=[]
                    for i in states:
                        dgc=d1[d1['State']==i]
                        amount.append(dgc['Transaction_Amount'].sum())
                    dic={'State':state,"Total_Amount":amount}
                    df=pd.DataFrame(data=dic)
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='Total_Amount',
                        color_continuous_scale='reds'
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Amount in - 2023</h4>",unsafe_allow_html=True)
                    st.write(fig)
                    st.write("Total transaction amount in 2023: ",round(df['Total_Amount'].sum(),2))
                with c2:
                    st.write("")
                with c3:
                    df=df.sort_values(by="Total_Amount",ascending=False)
                    st.dataframe(df,hide_index=True)
    
        for i in se:
             if(i=='2018'):
                 c1,c2,c3=st.columns(3)
                 with c1:
                     d1=agg_user[agg_user['Year']=='2018']
                     count=[]
                     for i in states:
                         dgc=d1[d1['State']==i]
                         count.append(dgc['Brand_Count'].sum())
                     dic={'State':state,"Total_Count":count}
                     df=pd.DataFrame(data=dic)
                     fig = px.choropleth(
                         df,
                         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                         featureidkey='properties.ST_NM',
                         locations='State',
                         color='Total_Count',
                         color_continuous_scale='earth'
                     )
                     fig.update_geos(fitbounds="locations", visible=False)
                     st.markdown("<h4><FONT COLOR='#BF40BF'>Total Count in - 2018</h4>",unsafe_allow_html=True)
                     st.write(fig)
                     st.write("Total Users Count in 2018: ",df['Total_Count'].sum())
                 with c2:
                    st.write("")
                 with c3:
                    df=df.sort_values(by="Total_Count",ascending=False)
                    st.dataframe(df,hide_index=True)
             if(i=='2019'):
                 c1,c2,c3=st.columns(3)
                 with c1:
                     d1=agg_user[agg_user['Year']=='2019']
                     count=[]
                     for i in states:
                         dgc=d1[d1['State']==i]
                         count.append(dgc['Brand_Count'].sum())
                     dic={'State':state,"Total_Count":count}
                     df=pd.DataFrame(data=dic)
                     fig = px.choropleth(
                         df,
                         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                         featureidkey='properties.ST_NM',
                         locations='State',
                         color='Total_Count',
                         color_continuous_scale='blugrn'
                     )
                     fig.update_geos(fitbounds="locations", visible=False)
                     st.markdown("<h4><FONT COLOR='#BF40BF'>Total Count in - 2019</h4>",unsafe_allow_html=True)
                     st.write(fig)
                     st.write("Total Users Count in 2019: ",df['Total_Count'].sum())
                 with c2:
                        st.write("")
                 with c3:
                        df=df.sort_values(by="Total_Count",ascending=False)
                        st.dataframe(df,hide_index=True)
             if(i=='2020'):
                 c1,c2,c3=st.columns(3)
                 with c1:
                     d1=agg_user[agg_user['Year']=='2020']
                     count=[]
                     for i in states:
                         dgc=d1[d1['State']==i]
                         count.append(dgc['Brand_Count'].sum())
                     dic={'State':state,"Total_Count":count}
                     df=pd.DataFrame(data=dic)
                     fig = px.choropleth(
                         df,
                         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                         featureidkey='properties.ST_NM',
                         locations='State',
                         color='Total_Count',
                         color_continuous_scale='bluyl'
                     )
                     fig.update_geos(fitbounds="locations", visible=False)
                     st.markdown("<h4><FONT COLOR='#BF40BF'>Total Count in - 2020</h4>",unsafe_allow_html=True)
                     st.write(fig)
                     st.write("Total Users Count in 2020: ",df['Total_Count'].sum())
                 with c2:
                    st.write("")
                 with c3:
                    df=df.sort_values(by="Total_Count",ascending=False)
                    st.dataframe(df,hide_index=True)
             if(i=='2021'):
                 c1,c2,c3=st.columns(3)
                 with c1:
                     d1=agg_user[agg_user['Year']=='2021']
                     count=[]
                     for i in states:
                         dgc=d1[d1['State']==i]
                         count.append(dgc['Brand_Count'].sum())
                     dic={'State':state,"Total_Count":count}
                     df=pd.DataFrame(data=dic)
                     fig = px.choropleth(
                         df,
                         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                         featureidkey='properties.ST_NM',
                         locations='State',
                         color='Total_Count',
                         color_continuous_scale='Reds'
                     )
                     fig.update_geos(fitbounds="locations", visible=False)
                     st.markdown("<h4><FONT COLOR='#BF40BF'>Total Count in - 2021</h4>",unsafe_allow_html=True)
                     st.write(fig)
                     st.write("Total Users Count in 2021: ",df['Total_Count'].sum())
                 with c2:
                     st.write("")
                 with c3:
                     df=df.sort_values(by="Total_Count",ascending=False)
                     st.dataframe(df,hide_index=True)
             if(i=='2022'):
                 st.markdown("<h4><FONT COLOR='#DC143C'>Sorry!! there is no data for the year 2022 </h4>",unsafe_allow_html=True)
             if(i=='2023'):
                 st.markdown("<h4><FONT COLOR='#DC143C'>Sorry!! there is no data for the year 2023</h4>",unsafe_allow_html=True)
                 
if(select=="Charts"):
    types=list(agg_trans['Tranaction_Type'].unique())
    year=list(agg_trans['Year'].unique())
    
    st.markdown("<h4><FONT COLOR='#BF40BF'>Types of transactions:</h4>",unsafe_allow_html=True)
    st.markdown("<p>1.<b> Recharge and Bill Payments:</b> Users can recharge their mobile phones or pay bills from the comfort of their homes or on the go. Online platforms offer a variety of payment methods, providing flexibility to users.  Recharges and bill payments are processed quickly, ensuring that services are not interrupted.</p>",unsafe_allow_html=True)
    st.markdown("<p>2.<b> Peer-to-peer payments:</b> Peer-to-peer (P2P) payments refer to the transfer of funds between individuals using electronic platforms or mobile applications, without the involvement of traditional banking institutions. This method of transferring money has become increasingly popular due to its convenience and speed.</p>",unsafe_allow_html=True)
    st.markdown("<p>3.<b> Merchant Payments:</b> Merchant payments refer to transactions where customers make payments to businesses or merchants for goods and services. These transactions involve the exchange of money in return for products or services provided by the merchant.</p>",unsafe_allow_html=True)
    st.markdown("<p>4. <b>Financial Payments:</b> Financial payments encompass a wide range of transactions involving the transfer of money between individuals, businesses, and financial institutions. These transactions are crucial for the functioning of economies, and various methods are used to facilitate financial payments. </p>",unsafe_allow_html=True)
    st.markdown("<p>5. <b>Others</b> </p>",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        st.markdown("<h4><FONT COLOR='#BF40BF'>Total transaction amount for each type</h4>",unsafe_allow_html=True)
        st.write("""Displays 5 types of payments and it's total amount for every year by pie chart format. """)
        s1=st.multiselect("Select the years: ",year,key="type1")
    with c2:
        st.markdown("<h4><FONT COLOR='#BF40BF'>Total transaction count for each type</h4>",unsafe_allow_html=True)
        st.write("""Displays 5 types of payments and it's total user's count for every year by pie chart format. """)
        s2=st.multiselect("Select the years: ",year,key="type2")
    if st.button("Submit",key="btn1"):
        for i in s1:
            if(i=="2018"):
                c1,c2,c3=st.columns(3)
                with c1:
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2018</h4>",unsafe_allow_html=True)
                    d1=agg_trans[agg_trans['Year']=='2018']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
            if(i=="2019"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2019']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2019</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
            if(i=="2020"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2020']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2020</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
            if(i=="2021"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2021']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2021</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
            if(i=="2022"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2022']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2022</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
            if(i=="2023"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2023']
                    fig = px.pie(d1, values='Transaction_Amount', names='Tranaction_Type',hole=.5,)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction amount in Year- 2023</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=d1.groupby("Tranaction_Type")['Transaction_Amount'].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values("Transaction_Amount",ascending=False)
                    st.dataframe(dh)
        for i in s2:
            if(i=="2018"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2018']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2018</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
            if(i=="2019"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2019']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2019</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
            if(i=="2020"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2020']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2020</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
            if(i=="2021"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2021']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2021</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
            if(i=="2022"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2022']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2022</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
            if(i=="2023"):
                c1,c2,c3=st.columns(3)
                with c1:
                    d1=agg_trans[agg_trans['Year']=='2023']
                    fig = px.pie(d1, values='Transaction_Count', names='Tranaction_Type',hole=.5)
                    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Total User count in Year- 2023</h4>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    da=d1.groupby("Tranaction_Type")['Transaction_Count'].sum()
                    da=pd.DataFrame(da)
                    da=da.sort_values("Transaction_Count",ascending=False)
                    st.dataframe(da)
    st.markdown("<h4><FONT COLOR='#BF40BF'>Mobile Brands</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Displays the Brand name and their number of users for every year. You can select any years</h5>",unsafe_allow_html=True)
    s3=st.multiselect("Select the year: ",year,key="sel3")
    if st.button("Submit",key="btn4"):
        for i in s3:
            if i=="2018":
                c1,c2,c3=st.columns(3)
                with c1:
                    de=agg_user[agg_user['Year']=='2018']
                    fig=px.histogram(de,x="Brand_name",y="Brand_Count",color="Brand_name")
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Year- 2018</h4>",unsafe_allow_html=True)
                    st.write(fig,unsafe_allow_html=True)
                with c2:
                    st.write("")
                with c3:
                    de=de.groupby(["Brand_name","Quater"])['Brand_Count'].sum()
                    de=pd.DataFrame(de)
                    de=de.sort_values("Brand_Count",ascending=False)
                    st.dataframe(de)
            if i=="2019":
                c1,c2,c3=st.columns(3)
                with c1:
                    de=agg_user[agg_user['Year']=='2019']
                    fig=px.histogram(de,x="Brand_name",y="Brand_Count",color="Brand_name")
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Year- 2019</h4>",unsafe_allow_html=True)
                    st.write(fig,unsafe_allow_html=True)
                with c2:
                    st.write("")
                with c3:
                    de=de.groupby(["Brand_name","Quater"])['Brand_Count'].sum()
                    de=pd.DataFrame(de)
                    de=de.sort_values("Brand_Count",ascending=False)
                    st.dataframe(de)
            if i=="2020":
                c1,c2,c3=st.columns(3)
                with c1:
                    de=agg_user[agg_user['Year']=='2020']
                    fig=px.histogram(de,x="Brand_name",y="Brand_Count",color="Brand_name")
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Year- 2020</h4>",unsafe_allow_html=True)
                    st.write(fig,unsafe_allow_html=True)
                with c2:
                    st.write("")
                with c3:
                    de=de.groupby(["Brand_name","Quater"])['Brand_Count'].sum()
                    de=pd.DataFrame(de)
                    de=de.sort_values("Brand_Count",ascending=False)
                    st.dataframe(de)
            if i=="2021":
                c1,c2,c3=st.columns(3)
                with c1:
                    de=agg_user[agg_user['Year']=='2021']
                    fig=px.histogram(de,x="Brand_name",y="Brand_Count",color="Brand_name")
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Year- 2021</h4>",unsafe_allow_html=True)
                    st.write(fig,unsafe_allow_html=True)
                with c2:
                    st.write("")
                with c3:
                    de=de.groupby(["Brand_name","Quater"])['Brand_Count'].sum()
                    de=pd.DataFrame(de)
                    de=de.sort_values("Brand_Count",ascending=False)
                    st.dataframe(de)
            if i=="2022":
                c1,c2,c3=st.columns(3)
                with c1:
                    de=agg_user[agg_user['Year']=='2022']
                    fig=px.histogram(de,x="Brand_name",y="Brand_Count",color="Brand_name")
                    st.markdown("<h4><FONT COLOR='#BF40BF'>Year- 2022</h4>",unsafe_allow_html=True)
                    st.write(fig,unsafe_allow_html=True)
                with c2:
                    st.write("")
                with c3:
                    de=de.groupby(["Brand_name","Quater"])['Brand_Count'].sum()
                    de=pd.DataFrame(de)
                    de=de.sort_values("Brand_Count",ascending=False)
                    st.dataframe(de)
            if i=="2023":
                st.markdown("<h5>Sorry There is no data for the year 2023</h5>",unsafe_allow_html=True)
                
    st.markdown("<h4><FONT COLOR='#BF40BF'>District wise Details</h4>",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        st.markdown("<h4><FONT COLOR='#BF40BF'>Total Transaction</h4>",unsafe_allow_html=True)
        st.markdown("""<h6>Displays total transaction amount for all District in a selected state for all years from 2018 to 2023 in Bar chart format</h6>""",unsafe_allow_html=True)
        stat=list(map_trans['State'].unique())
        s3=st.multiselect("Select any states ",stat,key="sta1")
    with c2:
        st.markdown("<h4><FONT COLOR='#BF40BF'>User Count</h4>",unsafe_allow_html=True)
        st.markdown("""<h6>Displays total Users count for all District in a selected state for all years from 2018 to 2023 in Bar chart format</h6>""",unsafe_allow_html=True)
        stat2=list(map_user['State'].unique())
        s4=st.multiselect("Select any states ",stat2,key="sta12")
    if st.button("Submit",key="btn3"):
        for i in s3:
            if(i=="andaman-&-nicobar-islands"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="andaman-&-nicobar-islands"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Andaman & Nicobar</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="andhra-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="andhra-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Andhra Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="arunachal-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="arunachal-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Arunachal Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="assam"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="assam"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Assam</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="bihar"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="bihar"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Bihar</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="chandigarh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="chandigarh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Chandigarh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="chhattisgarh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="chhattisgarh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Chhattisgarh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="dadra-&-nagar-haveli-&-daman-&-diu"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="dadra-&-nagar-haveli-&-daman-&-diu"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Dadra-&-Nagar-Haveli-&-daman-&-diu</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="delhi"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="delhi"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Delhi</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="goa"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="goa"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Goa</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="gujarat"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="gujarat"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Gujarat</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="haryana"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="haryana"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Haryana</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="himachal-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="himachal-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Himachal-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="jammu-&-kashmir"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="jammu-&-kashmir"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Jammu-&-Kashmir</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="jharkhand"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="jharkhand"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Jharkhand</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="karnataka"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="karnataka"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Karnataka</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="kerala"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="kerala"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Kerala</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="ladakh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="ladakh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Ladakh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="lakshadweep"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="lakshadweep"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Lakshadweep</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="madhya-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="madhya-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Madhya-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write('')
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="maharashtra"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="maharashtra"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Maharashtra</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write('')
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="manipur"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="manipur"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Manipur</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="meghalaya"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="meghalaya"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Meghalaya</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="mizoram"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="mizoram"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Mizoram</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="nagaland"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="nagaland"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Nagaland</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="odisha"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="odisha"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Odisha</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="puducherry"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="puducherry"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Puducherry</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="punjab"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="punjab"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Punjab</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="rajasthan"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="rajasthan"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Rajasthan</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="sikkim"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="sikkim"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Sikkim</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write('')
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="tamil-nadu"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="tamil-nadu"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Tamil-Nadu</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="telangana"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="telangana"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Telangana</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="tripura"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="tripura"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Tripura</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="uttar-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="uttar-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Uttar-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="uttarakhand"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="uttarakhand"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Uttarakhand</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(i=="west-bengal"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_trans[map_trans['State']=="west-bengal"]
                    fig=px.histogram(ds,x="District_name",y="Amount",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- West-Bengal</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Amount"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Amount"],ascending=False)
                    st.markdown("<h6>Displays transaction amount in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
        for j in s4:
            if(j=="andaman-&-nicobar-islands"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="andaman-&-nicobar-islands"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Andaman & Nicobar</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="andhra-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="andhra-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Andhra Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="arunachal-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="arunachal-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Arunachal Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="assam"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="assam"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h5><FONT COLOR='#BF40BF'>State- Assam</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="bihar"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="bihar"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Bihar</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="chandigarh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="chandigarh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Chandigarh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="chhattisgarh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="chhattisgarh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Chhattisgarh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="dadra-&-nagar-haveli-&-daman-&-diu"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="dadra-&-nagar-haveli-&-daman-&-diu"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Dadra-&-Nagar-Haveli-&-Daman-&-Diu</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="delhi"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="delhi"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Delhi</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="goa"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="goa"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Goa</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="gujarat"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="gujarat"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Gujarat</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="haryana"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="haryana"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Haryana</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="himachal-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="himachal-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Himachal-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="jammu-&-kashmir"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="jammu-&-kashmir"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Jammu-&-Kashmir</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="jharkhand"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="jharkhand"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Jharkhand</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="karnataka"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="karnataka"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Karnataka</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="kerala"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="kerala"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Kerala</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="ladakh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="ladakh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Ladakh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="lakshadweep"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="lakshadweep"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Lakshadweep</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="madhya-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="madhya-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Madhya-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="maharashtra"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="maharashtra"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Maharashtra</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="manipur"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="manipur"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Manipur</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="meghalaya"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="meghalaya"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Meghalaya</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="mizoram"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="mizoram"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Mizoram</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="nagaland"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="nagaland"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Nagaland</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="odisha"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="odisha"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Odisha</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="puducherry"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="puducherry"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Puducherry</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="rajasthan"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="rajasthan"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Rajasthan</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="sikkim"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="sikkim"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Sikkim</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="tamil-nadu"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="tamil-nadu"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Tamil Nadu</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="telangana"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="telangana"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Telangana</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="tripura"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="tripura"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Tripura</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="uttar-pradesh"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="uttar-pradesh"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Uttar-Pradesh</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="uttarakhand"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="uttarakhand"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- Uttarakhand</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
            if(j=="west-bengal"):
                c1,c2,c3=st.columns(3)
                with c1:
                    ds=map_user[map_user['State']=="west-bengal"]
                    fig=px.histogram(ds,x="District_name",y="Registered_user",color="District_name")
                    st.markdown("<h6><FONT COLOR='#BF40BF'>State- West-Bengal</h6>",unsafe_allow_html=True)
                    st.write(fig,use_container_width=True)
                with c2:
                    st.write("")
                with c3:
                    dh=ds.groupby(["Year","Quater","District_name"])["Registered_user"].sum()
                    dh=pd.DataFrame(dh)
                    dh=dh.sort_values(by=["Registered_user"],ascending=False)
                    st.markdown("<h6>Displays user count in year wise from Highest transction amount to lowest transaction amount</h6>",unsafe_allow_html=True)
                    st.dataframe(dh)
 