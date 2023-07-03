
import streamlit as st
import pickle
import pandas as pd

loaded_model=pickle.load(open('E:/python_programs/campusplacement2/trained_model.sav','rb'))

def placement(input_data):
    prediction = loaded_model.predict(input_data)
    if prediction[0]==0:
        return 'Student will not be placed'
    else:
        return 'Student will be placed'

def main():

    st.title('Campus Placement Prediction')

    gender = st.selectbox('Gender', ['M', 'F'])
    ssc_p = st.number_input('senior secondary percentage scored', min_value=0.000000, max_value=100.000000, step=0.1)
    ssc_b = st.selectbox('senior secondary board', ['Others', 'Central'])
    hsc_p = st.number_input('higher secondary percentage scored', min_value=0.000000, max_value=100.000000, step=0.1)
    hsc_b = st.selectbox('higher secondary board', ['Others', 'Central'])
    hsc_s = st.selectbox('higher secondary subject', ['Science', 'Commerce','Arts'])
    degree_p = st.number_input('percentage scored in degree/graduation', min_value=0.000000, max_value=100.000000, step=0.1)
    degree_t = st.selectbox('degree technology', ['Sci&Tech', 'Comm&Mgmt','Others'])
    etest_p = st.number_input('entrance test percentage scored', min_value=0.000000, max_value=100.000000, step=0.1)
    mba_p = st.number_input('mba percentage scored', min_value=0.000000, max_value=100.000000, step=0.1)
    specialisation = st.selectbox('mba specialization', ['Mkt&HR', 'Mkt&Fin'])
    workex = st.selectbox('work experience', ['Yes', 'No'])

    Gender=0 if gender=='M' else 1
    Ssc_b= 0 if ssc_p=='Central' else 1
    Hsc_b = 0 if ssc_p == 'Central' else 1
    Hsc_s = 0 if hsc_s =='Arts' else 1 if hsc_s=='Commerce' else 2
    Degree_t = 0 if degree_t=='Comm&Mgmt' else 1 if degree_t=='Others' else 2
    Specialisation = 0 if specialisation=='Mkt&HR' else 1
    Workex = 0 if workex=='No' else 1

    input_data = {'gender':Gender,'ssc_p':ssc_p,'ssc_b':Ssc_b,'hsc_p':hsc_p,'hsc_b':Hsc_b,'hsc_s':Hsc_s,'degree_p':degree_p,
                  'degree_t':Degree_t,'etest_p':etest_p,'mba_p':mba_p,'specialisation':Specialisation,'workex':Workex}

    input_df=pd.DataFrame([input_data])
    placement_status = ''

    if st.button('Placement Status'):
        placement_status = placement(input_df)

    st.success(placement_status)


if __name__ == '__main__':
    main()







