import pickle
import numpy as np
import pandas as pd

class HealthInsurance():
    def __init__(self):

        #local API test needs abs home_path
        self.home_path='/Users/home/repos/pa004_health_insurance_cross_sell/health_insurance_cross-sell/health_insurance_app_local/'
        self.health_annual_paid_scaler        = pickle.load( open( self.home_path + 'features/health_annual_paid_scaler.pkl', 'rb'))
        self.age_scaler                       = pickle.load( open( self.home_path + 'features/age_scaler.pkl', 'rb'))
        self.days_assoc_scaler                = pickle.load( open( self.home_path + 'features/days_assoc_scaler.pkl', 'rb'))
        self.gender_target_encoder            = pickle.load( open( self.home_path + 'features/gender_target_encoder.pkl', 'rb'))
        self.region_code_target_encoder       = pickle.load( open( self.home_path + 'features/region_code_target_encoder.pkl', 'rb'))
        self.policy_sales_freq_encoder        = pickle.load( open( self.home_path + 'features/policy_sales_freq_encoder.pkl', 'rb'))

    def data_cleaning(self, df1):

        # Rename Columns
        cols_new = ['id', 'gender', 'age', 'region_code','policy_sales_channel','driving_license',
                        'vehicle_age', 'vehicle_damage', 'vehicle_prev_insured', 'health_annual_paid', 'days_associated']

        df1.columns = cols_new

        return df1


    def feature_engineering (self, df2):

        # vehicle damage
        dict_vehicle_damage = {'Yes': 1, 'No': 0}
        df2['vehicle_damage'] = df2['vehicle_damage'].map(dict_vehicle_damage)

        # vehicle_age
        dict_vehicle_age = {'> 2 Years':'over_2_years', '1-2 Year':'between_1_2_years', '< 1 Year': 'below_1_year' }
        df2['vehicle_age'] = df2['vehicle_age'].map(dict_vehicle_age)

        return df2


    def data_preparation (self, df3):

        # transformations
        df3['health_annual_paid'] = self.health_annual_paid_scaler.transform( df3[['health_annual_paid']].values )
        df3['age'] = self.age_scaler.transform( df3[['age']].values )
        df3['days_associated'] = self.days_assoc_scaler.transform( df3[['days_associated']].values )
        #df3.loc[:,'gender'] = df3['gender'].map(self.gender_target_encoder) #was not selected
        df3.loc[:,'region_code'] = df3['region_code'].map(self.region_code_target_encoder)
        df3.loc[:,'policy_sales_channel'] = df3['policy_sales_channel'].map(self.policy_sales_freq_encoder)
        #vars 'vehicle_damage' and 'vehicle_prev_insured' didn't have trasnformations.

        # feature Selection
        cols_selected = ['days_associated','health_annual_paid','age','region_code',
                            'vehicle_damage','policy_sales_channel', 'vehicle_prev_insured']
        #cols 'id', 'gender', 'driving_license' and 'vehicle_age' were features not selected.

        return df3[cols_selected]


    def get_prediction( self, model, original_data, test_data ):

        #model prediction
        pred = model.predict_proba( test_data )

        #join prediction into original data and sort
        original_data['score'] = pred[:, 1].tolist()
        original_data = original_data.sort_values('score', ascending=False)

        return original_data.to_json( orient= 'records', date_format = 'iso' )
