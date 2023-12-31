import pandas as pd
import numpy as np
import streamlit as st
#linear regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet, Lasso
#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
#random forest
from sklearn.ensemble import RandomForestRegressor
#svr
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR#quadratic running time,  
#hard to scale to datasets with more than a couple of 10000 samples
from sklearn.linear_model import SGDRegressor#Stochastic Gradient Descent
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import math
from PIL import Image

st.header('Predicting Hourly Ridership')
tab1, tab2=st.tabs(['Models','Station Predictions'])

with tab1:
    image = Image.open('visualizations/station_ml_scores/model_performance.png')
    st.image(image, caption='ML Model Performance')
    st.markdown("""
                1. Data Complexity (6086184,43):
                - Our hourly subway ridership data has **6086184** rows in total.
                - Hour, Weekdays, and Month are categorical variables, which requires **dummy coding and dropping first**.
                - After dummy coding and combining with weather data, we have 43 columns.
                2. Model Selection
                - There are 425 stations; on average, each station has 14320 data points.
                - Due to the data complexity, we decided to fit a regression model on each station to predict hourly ridership.
                - Model considered: Linear regression, Ridge, Lasso, Polynomial regression, Random Forest Regressor, Gradient Boosting Regressor, ~SVR~, ~KNN~
                3. Model Performance
                - Linear Regression (even with regularization terms) perform badly in predicting hourly ridership, with an average r^2 of 0.64 on testing data.
                - Random Forest Regressor and Gradient Boosting Regression have better performance than linear regression, with an average r^2 of 0.7 on testing data.
                - Quadratic Regressor has the best performance, with r^2 of 0.77 on testing data.""")
                
with tab2:
    st.caption("Data from DATA.NY.GOV; generated by _Matplotlib_")
    selected_station=st.selectbox(label="Please select a station:",
                                  options=['1 Av (L)', '103 St (1)', '103 St (6)', '103 St (B,C)',
       '103 St-Corona Plaza (7)', '104 St (A)', '104 St (J,Z)',
       '110 St (6)', '111 St (7)', '111 St (A)', '111 St (J)',
       '116 St (2,3)', '116 St (6)', '116 St (B,C)',
       '116 St-Columbia University (1)', '121 St (J,Z)', '125 St (1)',
       '125 St (2,3)', '125 St (4,5,6)', '125 St (A,B,C,D)',
       '135 St (2,3)', '135 St (B,C)', '137 St-City College (1)',
       '138 St-Grand Concourse (4,5)', '14 St (A,C,E)/8 Av (L)',
       '14 St (F,M,1,2,3)/6 Av (L)', '14 St-Union Sq (L,N,Q,R,W,4,5,6)',
       '145 St (1)', '145 St (3)', '145 St (A,B,C,D)',
       '149 St-Grand Concourse (2,4,5)', '15 St-Prospect Park (F,G)',
       '155 St (B,D)', '155 St (C)', '157 St (1)',
       '161 St-Yankee Stadium (B,D,4)', '163 St-Amsterdam Av (C)',
       '167 St (4)', '167 St (B,D)', '168 St (A,C,1)', '169 St (F)',
       '170 St (4)', '170 St (B,D)', '174 St (2,5)', '174-175 Sts (B,D)',
       '175 St (A)', '176 St (4)', '18 Av (D)', '18 Av (F)', '18 Av (N)',
       '18 St (1)', '181 St (1)', '181 St (A)', '182-183 Sts (B,D)',
       '183 St (4)', '190 St (A)', '191 St (1)', '2 Av (F)', '20 Av (D)',
       '20 Av (N)', '207 St (1)', '21 St (G)', '21 St-Queensbridge (F)',
       '215 St (1)', '219 St (2,5)', '225 St (2,5)', '23 St (1)',
       '23 St (6)', '23 St (C,E)', '23 St (F,M)', '23 St (R,W)',
       '231 St (1)', '233 St (2,5)', '238 St (1)', '25 Av (D)',
       '25 St (R)', '28 St (1)', '28 St (6)', '28 St (R,W)', '3 Av (L)',
       '3 Av-138 St (6)', '3 Av-149 St (2,5)', '30 Av (N,W)', '33 St (6)',
       '33 St-Rawson St (7)', '34 St-Herald Sq (B,D,F,M,N,Q,R,W)',
       '34 St-Hudson Yards (7)', '34 St-Penn Station (1,2,3)',
       '34 St-Penn Station (A,C,E)', '36 Av (N,W)', '36 St (D,N,R)',
       '36 St (M,R)', '39 Av (N,W)', '4 Av (F,G)/9 St (R)',
       '40 St-Lowery St (7)', '45 St (R)', '46 St (M,R)',
       '46 St-Bliss St (7)', '47-50 Sts-Rockefeller Center (B,D,F,M)',
       '49 St (N,R,W)', '5 Av-53 St (E,M)', '5 Av-59 St (N,R,W)',
       '50 St (1)', '50 St (C,E)', '50 St (D)', '52 St (7)', '53 St (R)',
       '55 St (D)', '57 St (F)', '57 St-7 Av (N,Q,R,W)', '59 St (N,R)',
       '59 St-Columbus Circle (A,B,C,D,1)', '63 Dr-Rego Park (M,R)',
       '65 St (M,R)', '66 St-Lincoln Center (1)', '67 Av (M,R)',
       '68 St-Hunter College (6)', '69 St (7)', '7 Av (B,D,E)',
       '7 Av (B,Q)', '7 Av (F,G)', '71 St (D)', '72 St (1,2,3)',
       '72 St (B,C)', '72 St (Q)',
       '74-Broadway (7)/Jackson Hts-Roosevelt Av (E,F,M,R)',
       '75 Av (E,F)', '75 St-Elderts Ln (J,Z)', '77 St (6)', '77 St (R)',
       '79 St (1)', '79 St (D)', '8 Av (N)',
       '8 St-New York University (R,W)', '80 St (A)',
       '81 St-Museum of Natural History (B,C)', '82 St-Jackson Hts (7)',
       '85 St-Forest Pkwy (J)', '86 St (1)', '86 St (4,5,6)',
       '86 St (B,C)', '86 St (N)', '86 St (Q)', '86 St (R)', '88 St (A)',
       '9 Av (D)', '90 St-Elmhurst Av (7)', '96 St (1,2,3)', '96 St (6)',
       '96 St (B,C)', '96 St (Q)', 'Alabama Av (J)', 'Allerton Av (2,5)',
       'Aqueduct Racetrack (A)', 'Aqueduct-North Conduit Av (A)',
       'Astor Place (6)', 'Astoria Blvd (N,W)',
       'Astoria-Ditmars Blvd (N,W)', 'Atlantic Av (L)',
       'Atlantic Av-Barclays Ctr (B,D,N,Q,R,2,3,4,5)', 'Avenue H (Q)',
       'Avenue I (F)', 'Avenue J (Q)', 'Avenue M (Q)', 'Avenue N (F)',
       'Avenue P (F)', 'Avenue U (F)', 'Avenue U (N)', 'Avenue U (Q)',
       'Avenue X (F)', 'Bay 50 St (D)', 'Bay Pkwy (D)', 'Bay Pkwy (F)',
       'Bay Pkwy (N)', 'Bay Ridge Av (R)', 'Bay Ridge-95 St (R)',
       'Baychester Av (5)', 'Beach 105 St (A,S)', 'Beach 25 St (A)',
       'Beach 36 St (A)', 'Beach 44 St (A)', 'Beach 60 St (A)',
       'Beach 67 St-Arverne By The Sea (A)', 'Beach 90 St (A,S)',
       'Beach 98 St (A,S)', 'Bedford Av (L)', 'Bedford Park Blvd (B,D)',
       'Bedford Park Blvd-Lehman College (4)', 'Bedford-Nostrand Avs (G)',
       'Bergen St (2,3)', 'Bergen St (F,G)', 'Beverley Rd (Q)',
       'Beverly Rd (2,5)', 'Bowery (J,Z)', 'Bowling Green (4,5)',
       'Briarwood-Van Wyck Blvd (E,F)', 'Brighton Beach (B,Q)',
       'Broad Channel (A,S)', 'Broad St (J,Z)', 'Broadway (G)',
       'Broadway (N,W)', 'Broadway Junction (A,C,J,L,Z)',
       'Broadway-Lafayette St (B,D,F,M)/Bleecker St (6)',
       'Bronx Park East (2,5)', 'Brook Av (6)',
       'Brooklyn Bridge-City Hall (4,5,6)/Chambers St (J,Z)',
       'Buhre Av (6)', 'Burke Av (2,5)', 'Burnside Av (4)',
       'Bushwick Av-Aberdeen St (L)', 'Canal St (1)', 'Canal St (A,C,E)',
       'Canal St (J,N,Q,R,W,Z,6)', 'Canarsie-Rockaway Pkwy (L)',
       'Carroll St (F,G)', 'Castle Hill Av (6)',
       'Cathedral Pkwy-110 St (1)', 'Cathedral Pkwy-110 St (B,C)',
       'Central Av (M)', 'Central Park North-110 St (2,3)',
       'Chambers St (1,2,3)',
       'Chambers St (A,C)/WTC (E)/Park Pl (2,3)/Cortlandt (R,W)',
       'Chauncey St (J,Z)', 'Christopher St-Sheridan Sq (1)',
       'Church Av (2,5)', 'Church Av (B,Q)', 'Church Av (F,G)',
       'City Hall (R,W)', 'Clark St (2,3)', 'Classon Av (G)',
       'Cleveland St (J)', 'Clinton-Washington Avs (C)',
       'Clinton-Washington Avs (G)',
       'Coney Island-Stillwell Av (D,F,N,Q)', 'Cortelyou Rd (Q)',
       'Court Sq (E,G,M,7)', 'Court St (R)/Borough Hall (2,3,4,5)',
       'Crescent St (J,Z)', 'Crown Heights-Utica Av (3,4)',
       'Cypress Av (6)', 'Cypress Hills (J)', 'DeKalb Av (B,Q,R)',
       'DeKalb Av (L)', 'Delancey St (F)/Essex St (J,M,Z)',
       'Ditmas Av (F)', 'Dyckman St (1)', 'Dyckman St (A)',
       'East 105 St (L)', "East 143 St-St Mary's St (6)",
       'East 149 St (6)', 'East 180 St (2,5)', 'East Broadway (F)',
       'Eastchester-Dyre Av (5)', 'Eastern Pkwy-Brooklyn Museum (2,3)',
       'Elder Av (6)', 'Elmhurst Av (M,R)', 'Euclid Av (A,C)',
       'Far Rockaway-Mott Av (A)', 'Flatbush Av-Brooklyn College (2,5)',
       'Flushing Av (G)', 'Flushing Av (J,M)', 'Flushing-Main St (7)',
       'Fordham Rd (4)', 'Fordham Rd (B,D)', 'Forest Av (M)',
       'Forest Hills-71 Av (E,F,M,R)', 'Fort Hamilton Pkwy (D)',
       'Fort Hamilton Pkwy (F,G)', 'Fort Hamilton Pkwy (N)',
       'Franklin Av (2,3,4,5)/Botanic Garden (S)', 'Franklin Av (C,S)',
       'Franklin St (1)', 'Freeman St (2,5)', 'Fresh Pond Rd (M)',
       'Fulton St (A,C,J,Z,2,3,4,5)', 'Fulton St (G)', 'Gates Av (J,Z)',
       'Graham Av (L)', 'Grand Army Plaza (2,3)',
       'Grand Av-Newtown (M,R)', 'Grand Central-42 St (S,4,5,6,7)',
       'Grand St (B,D)', 'Grand St (L)', 'Grant Av (A)',
       'Greenpoint Av (G)', 'Gun Hill Rd (2,5)', 'Gun Hill Rd (5)',
       'Halsey St (J)', 'Halsey St (L)', 'Harlem-148 St (3)',
       'Hewes St (J,M)', 'High St (A,C)', 'Houston St (1)',
       'Howard Beach-JFK Airport (A)', 'Hoyt St (2,3)',
       'Hoyt-Schermerhorn Sts (A,C,G)', 'Hunters Point Av (7)',
       'Hunts Point Av (6)', 'Intervale Av (2,5)', 'Inwood-207 St (A)',
       'Jackson Av (2,5)', 'Jamaica Center-Parsons-Archer (E,J,Z)',
       'Jamaica-179 St (F)', 'Jamaica-Van Wyck (E)',
       'Jay St-MetroTech (A,C,F,R)', 'Jefferson St (L)',
       'Junction Blvd (7)', 'Junius St (3)',
       'Kew Gardens-Union Turnpike (E,F)', 'Kings Hwy (B,Q)',
       'Kings Hwy (F)', 'Kings Hwy (N)', 'Kingsbridge Rd (4)',
       'Kingsbridge Rd (B,D)', 'Kingston Av (3)',
       'Kingston-Throop Avs (C)', 'Knickerbocker Av (M)',
       'Kosciuszko St (J)', 'Lafayette Av (C)',
       'Lexington Av (N,R,W)/59 St (4,5,6)',
       'Lexington Av-53 St (E,M)/51 St (6)', 'Lexington Av-63 St (F,Q)',
       'Liberty Av (C)', 'Livonia Av (L)', 'Longwood Av (6)',
       'Lorimer St (J,M)', 'Lorimer St (L)/Metropolitan Av (G)',
       'Marble Hill-225 St (1)', 'Marcy Av (J,M,Z)',
       'Mets-Willets Point (7)', 'Middle Village-Metropolitan Av (M)',
       'Middletown Rd (6)', 'Montrose Av (L)', 'Morgan Av (L)',
       'Morris Park (5)', 'Morrison Av-Soundview (6)', 'Mosholu Pkwy (4)',
       'Mt Eden Av (4)', 'Myrtle Av (J,M,Z)', 'Myrtle-Willoughby Avs (G)',
       'Myrtle-Wyckoff Avs (L,M)', 'Nassau Av (G)', 'Neck Rd (Q)',
       'Neptune Av (F)', 'Nereid Av (2,5)', 'Nevins St (2,3,4,5)',
       'New Lots Av (3)', 'New Lots Av (L)',
       'New Utrecht Av (N)/62 St (D)', 'Newkirk Av (2,5)',
       'Newkirk Plaza (B,Q)', 'Northern Blvd (M,R)', 'Norwood Av (J,Z)',
       'Norwood-205 St (D)', 'Nostrand Av (3)', 'Nostrand Av (A,C)',
       'Ocean Pkwy (Q)', 'Ozone Park-Lefferts Blvd (A)', 'Park Pl (S)',
       'Parkchester (6)', 'Parkside Av (Q)', 'Parsons Blvd (F)',
       'Pelham Bay Park (6)', 'Pelham Pkwy (2,5)', 'Pelham Pkwy (5)',
       'Pennsylvania Av (3)', 'President St (2,5)', 'Prince St (R,W)',
       'Prospect Av (2,5)', 'Prospect Av (R)', 'Prospect Park (B,Q,S)',
       'Queens Plaza (E,M,R)', 'Queensboro Plaza (N,W,7)', 'Ralph Av (C)',
       'Rector St (1)', 'Rector St (R,W)', 'Rockaway Av (3)',
       'Rockaway Av (C)', 'Rockaway Blvd (A)',
       'Rockaway Park-Beach 116 St (A,S)', 'Roosevelt Island (F)',
       'Saratoga Av (3)', 'Seneca Av (M)', 'Sheepshead Bay (B,Q)',
       'Shepherd Av (C)', 'Simpson St (2,5)', 'Smith-9 Sts (F,G)',
       'South Ferry (1)/Whitehall St (R,W)', 'Spring St (6)',
       'Spring St (C,E)', 'St George', 'St Lawrence Av (6)',
       'Steinway St (M,R)', 'Sterling St (2,5)', 'Sutphin Blvd (F)',
       'Sutphin Blvd-Archer Av-JFK Airport (E,J,Z)', 'Sutter Av (L)',
       'Sutter Av-Rutland Rd (3)',
       'Times Sq-42 St (N,Q,R,W,S,1,2,3,7)/42 St (A,C,E)/Bryant Pk (B,D,F,M)/5 Av (7)',
       'Tompkinsville', 'Tremont Av (B,D)', 'Union St (R)',
       'Utica Av (A,C)', 'Van Cortlandt Park-242 St (1)',
       'Van Siclen Av (3)', 'Van Siclen Av (C)', 'Van Siclen Av (J,Z)',
       'Vernon Blvd-Jackson Av (7)', 'WTC Cortlandt (1)',
       'Wakefield-241 St (2)', 'Wall St (2,3)', 'Wall St (4,5)',
       'West 4 St-Washington Sq (A,B,C,D,E,F,M)',
       'West 8 St-New York Aquarium (F,Q)',
       'West Farms Sq-East Tremont Av (2,5)',
       'Westchester Sq-East Tremont Av (6)', 'Whitlock Av (6)',
       'Wilson Av (L)', 'Winthrop St (2,5)', 'Woodhaven Blvd (J,Z)',
       'Woodhaven Blvd (M,R)', 'Woodlawn (4)', 'Woodside-61 St (7)',
       'York St (F)', 'Zerega Av (6)'],
       index=14
       )
    # st.write('You selected:', selected_station)
    @st.cache_data
    def read_csv1(path='Data/ML_data/'+selected_station.split('/')[0]+'.csv'):
        return pd.read_csv(path)
    station_data=read_csv1()
    station_data.drop(columns=['Unnamed: 0'],axis=0,inplace=True)
    y=station_data['ridership']
    x=station_data[[i for i in station_data.columns if i!='ridership']]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42)
    models=[]
    r2_scores_test=[]
    mses_test=[]
    r2_scores_train=[]
    mses_train=[]
    plt.rcParams["figure.figsize"] = (20,10)
    fig, axs = plt.subplots(2, 3,sharey=True,sharex=True)
    
    linear_regression=LinearRegression()
    linear_regression.fit(X_train,y_train)
    y_pred1=linear_regression.predict(X_test)
    models.append('Linear Regression')
    r2_scores_test.append(r2_score(y_test,y_pred1))#r^2 score test for model1
    mses_test.append(mean_squared_error(y_test,y_pred1))#mse test for model1
    y_train_pred=linear_regression.predict(X_train)
    r2_scores_train.append(r2_score(y_train,y_train_pred))
    mses_train.append(mean_squared_error(y_train,y_train_pred))

    axs[0,0].scatter(y_train_pred,y_train_pred-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[0,0].scatter(y_pred1,y_pred1-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[0,0].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[0,0].set_ylabel("Residuals")
    axs[0,0].legend(loc='upper left')
    axs[0,0].set_title("Linear Regression")
    
    ridge_regression=Ridge()
    ridge_regression.fit(X_train,y_train)
    y_pred2=ridge_regression.predict(X_test)
    models.append('Ridge Regression')
    r2_scores_test.append(r2_score(y_test,y_pred2))
    mses_test.append(mean_squared_error(y_test,y_pred2))
    y_train_pred2=ridge_regression.predict(X_train)
    r2_scores_train.append(r2_score(y_train,y_train_pred2))
    mses_train.append(mean_squared_error(y_train,y_train_pred2))
    
    axs[0,1].scatter(y_train_pred2,y_train_pred2-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[0,1].scatter(y_pred2,y_pred2-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[0,1].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[0,1].legend(loc='upper left')
    axs[0,1].set_title("Ridge Regression")
    
    lasso=Lasso()
    lasso.fit(X_train,y_train)
    y_pred3=lasso.predict(X_test)
    models.append('LASSO Regression')
    r2_scores_test.append(r2_score(y_test,y_pred3))
    mses_test.append(mean_squared_error(y_test,y_pred3))
    y_train_pred3=lasso.predict(X_train)
    r2_scores_train.append(r2_score(y_train,y_train_pred3))
    mses_train.append(mean_squared_error(y_train,y_train_pred3))
    axs[0,2].scatter(y_train_pred3,y_train_pred3-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[0,2].scatter(y_pred3,y_pred3-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[0,2].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[0,2].legend(loc='upper left')
    axs[0,2].set_title("Lasso Regression")
    
    poly_regression=LinearRegression()
    poly=PolynomialFeatures(degree=2)
    X_train_modified=poly.fit_transform(X_train)
    poly_regression.fit(X_train_modified,y_train)
    y_pred4=poly_regression.predict(poly.fit_transform(X_test))
    models.append('Quadratic Regression')
    r2_scores_test.append(r2_score(y_test,y_pred4))
    mses_test.append(mean_squared_error(y_test,y_pred4))
    y_train_pred4=poly_regression.predict(poly.fit_transform(X_train))
    r2_scores_train.append(r2_score(y_train,y_train_pred4))
    mses_train.append(mean_squared_error(y_train,y_train_pred4))
    axs[1,0].scatter(y_train_pred4,y_train_pred4-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[1,0].scatter(y_pred4,y_pred4-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[1,0].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[1,0].set_ylabel("Residuals")
    axs[1,0].legend(loc='upper left')
    axs[1,0].set_title("Quadratic Regression")
    
    forest = RandomForestRegressor(n_estimators=100,
                                  random_state=0)
    forest.fit(X_train,y_train)
    y_pred5=forest.predict(X_test)
    models.append('Random Forest Regression')
    r2_scores_test.append(r2_score(y_test,y_pred5))
    mses_test.append(mean_squared_error(y_test,y_pred5))
    y_train_pred5=forest.predict(X_train)
    r2_scores_train.append(r2_score(y_train,y_train_pred5))
    mses_train.append(mean_squared_error(y_train,y_train_pred5))
    axs[1,1].scatter(y_train_pred5,y_train_pred5-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[1,1].scatter(y_pred5,y_pred5-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[1,1].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[1,1].set_xlabel("Predicted values")
    axs[1,1].legend(loc='upper left')
    axs[1,1].set_title("Random Forest Regression")
    
    boosting_r=GradientBoostingRegressor(random_state=0)
    boosting_r.fit(X_train,y_train)
    y_pred6=boosting_r.predict(X_test)
    models.append('Gradient Boosting Regression')
    r2_scores_test.append(r2_score(y_test,y_pred6))
    mses_test.append(mean_squared_error(y_test,y_pred6))
    y_train_pred6=forest.predict(X_train)
    r2_scores_train.append(r2_score(y_train,y_train_pred6))
    mses_train.append(mean_squared_error(y_train,y_train_pred6))
    axs[1,2].scatter(y_train_pred6,y_train_pred6-y_train,
           c="steelblue",edgecolor='white',marker='o',s=35,alpha=0.9,label="Training data")
    axs[1,2].scatter(y_pred6,y_pred6-y_test,
               c="limegreen",edgecolor='white',marker='s',s=35,alpha=0.9,label="Test data")
    axs[1,2].hlines(y=0,xmin=0,xmax=max(y_test))
    axs[1,2].legend(loc='upper left')
    axs[1,2].set_title("Gradient Boosting Regression")
    fig.suptitle("ML models for "+selected_station)
    st.pyplot(fig)

    c1,c2=st.columns(2)
    with c1:
        model_performance_r2=pd.DataFrame(np.zeros((6,2)),index=['Linear Regression', 'Ridge Regression', 'LASSO Regression',
       'Quadratic Regression', 'Random Forest Regression',
       'Gradient Boosting Regression'],columns=['r2_training','r2_testing'])
        model_performance_r2['r2_training']=r2_scores_train
        model_performance_r2['r2_testing']=r2_scores_test
        st.dataframe(model_performance_r2.style.highlight_max(axis=0))
    with c2:
        model_performance_mse=pd.DataFrame(np.zeros((6,2)),index=['Linear Regression', 'Ridge Regression', 'LASSO Regression',
       'Quadratic Regression', 'Random Forest Regression',
       'Gradient Boosting Regression'],columns=['MSE_training','MSE_testing'])
        model_performance_mse['MSE_training']=mses_train
        model_performance_mse['MSE_testing']=mses_test
        st.dataframe(model_performance_mse.style.highlight_min(axis=0))
    

    with st.form('my_form'):
        col1,col2=st.columns(2)
        with col1:
            hr=st.slider("Enter the hour:",min_value=0,max_value=23,step=1,value=7,key='hour')
            month=st.slider("Enter the month:",min_value=1,max_value=12,step=1,value=11,key='month')
            weekdays=st.select_slider("Enter the weekday:",options=[
                'Mon','Tue','Wed','Thr','Fri','Sat','Sun'
            ],value='Fri',key='weekdays')
        with col2:
            temp=st.number_input('Enter the temperature in F',value=40,key='temp')
            prcp=st.number_input("Enter the precipitation in inches",value=0,key='prcp')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Hour: ", hr, " ; Month: ", month, " ; Weekdays: ",weekdays, " ; Temperature: ",temp, " ; Precipitation: ",prcp)
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    def calculate_dynamic_fare_with_sigmoid(input_data, base_fare, max_capacity):
        traffic_factor=1
        cluster_factor=1
        event_factor=1

        sigmoid_midpoint = max_capacity / 2  # Midpoint of the sigmoid function
        sigmoid_steepness = 0.0001  # Controls how steep the sigmoid curve small for more gradual increase.

        predicted_ridership=round(poly_regression.predict(poly.fit_transform(input_data.values))[0],2)
        
        # Normalize ridership value for sigmoid function
        print(predicted_ridership)
        normalized_ridership = (predicted_ridership - sigmoid_midpoint) * sigmoid_steepness
        print(normalized_ridership)
        sigmoid_adjustment = sigmoid(normalized_ridership)

        dynamic_fare = base_fare * (1 + sigmoid_adjustment) * event_factor * traffic_factor * cluster_factor

        return np.clip(dynamic_fare, 0,30)
    
    base_fare = 2.9  # Base fare
    max_capacity = 2000 #https://www.nycsubway.org/wiki/Loading_Speed_A_Major_Factor_in_Design_of_New_York_Subway_Cars_(1931)
    input_data=pd.DataFrame(np.zeros((1,42)),
                    columns=['PRCP', 'avg_T', 'hour_1', 'hour_2', 'hour_3', 'hour_4', 'hour_5',
    'hour_6', 'hour_7', 'hour_8', 'hour_9', 'hour_10', 'hour_11', 'hour_12',
    'hour_13', 'hour_14', 'hour_15', 'hour_16', 'hour_17', 'hour_18',
    'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23', 'month_2',
    'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8',
    'month_9', 'month_10', 'month_11', 'month_12', 'weekdays_1',
    'weekdays_2', 'weekdays_3', 'weekdays_4', 'weekdays_5', 'weekdays_6'])
    input_data.loc[0,'PRCP']=prcp
    input_data.loc[0,'avg_T']=temp
    if 'hour_'+str(hr) in input_data.columns:
        input_data.loc[0,'hour_'+str(hr)]=1
    if 'month_'+str(month) in input_data.columns:
        input_data.loc[0,'month_'+str(month)]=1
    if 'weekdays_'+str(weekdays) in input_data.columns:
        input_data.loc[0,'weekdays_'+str(weekdays)]=1
    # poly_regression.predict(input_data.values)
    #forest.predict(input_data.values)
    #boosting_r.predict(input_data.values)
    st.write('Ridership prediction with Polynomial Regressor(degree2)',round(poly_regression.predict(poly.fit_transform(input_data.values))[0],2))
    st.write('Ridership prediction with Random Forest Regressor',round(forest.predict(input_data.values)[0],2))
    st.write('Ridership prediction with Gradient Boosting Regressor',round(boosting_r.predict(input_data.values)[0],2))
    fare = calculate_dynamic_fare_with_sigmoid(input_data, base_fare, max_capacity)
    st.write("Expected fare: $",round(fare,2))