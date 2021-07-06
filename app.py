import streamlit as st
import pickle
import numpy as np
def random_fn():
    val = 1

model=pickle.load(open('model_pickle.pkl','rb'))


def predict_stroke(gender,age, hypertension, disease, married,
       work, residence, glucose, bmi,
       smoking):
    
    if (gender == "Male"):
        gender_male=1
        gender_female = 0
        gender_other=0
    elif(gender == "Female"):
        gender_male = 0
        gender_female = 1
        gender_other = 0
    elif(gender== "Other"):
        gender_male=0
        gender_other=1
        gender_female = 0
        
        # married
    if(married=="Yes"):
        married_yes = 1
    else:
        married_yes=0

        # work  type
    if(work=='Self-employed'):
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 1
        work_type_children=0
        work_type_govt = 0
    elif(work == 'Private'):
        work_type_Never_worked = 0
        work_type_Private = 1
        work_type_Self_employed = 0
        work_type_children=0
        work_type_govt = 0
    elif(work=="Housewife"):
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=1
        work_type_govt = 0
    elif(work=="Never worked"):
        work_type_Never_worked = 1
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=0
        work_type_govt = 0
    elif(work == "Government"):
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=0
        work_type_govt = 1
        # residence type
    if (residence=="Urban"):
        Residence_type_Urban=1
    else:
        Residence_type_Urban=0

        # smoking sttaus
    if(smoking=='Former'):
        smoking_status_formerly_smoked = 1
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0
    elif(smoking == 'Smoker'):
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 1
    elif(smoking=="Never"):
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 1
        smoking_status_smokes = 0
    else:
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0

    feature = np.array([[gender_female, gender_male, gender_other, work_type_govt, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, 0, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes, age, hypertension, disease, married_yes, Residence_type_Urban, glucose, bmi]], dtype=np.float64)

    prediction = model.predict(feature)[0]
        # print(prediction) 
        # 
    return prediction
        

    

def main():
    st.title("Stroke Prediction")
    html_1 = """ 
    <div>
        <img src="stroke.jpeg" alt="Stroke">
    </div>
    """
    st.markdown(html_1, unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">CVA(Stroke) Prediction Web App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    gender = st.text_input("Gender (Male or Female)","")
    age = st.text_input("Age (In digits)","")
    hypertension = st.text_input("Do you suffer from hypertension? (1 for Yes 0 for No)","") 
    disease = st.text_input("Do you have any genetic heart condition? (1 for Yes 0 for No)","")
    married = st.text_input("Are you married? (Yes or No)","")
    work = st.text_input("Work type? (Private , Government, Self-employed, Housewife, Never Worked)","")
    residence = st.text_input("Residence Type? (Rural or Urban)","")
    glucose = st.text_input("Average Glucose Level? (in mg/dL)","") 
    bmi = st.text_input("BMI","")
    smoking = st.text_input("Do you smoke? (Smoker/Former/Never)","")
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Great! You are less likely to have a Stroke. Take care of yourself.</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Please take the following precautions:-</h2><br>
        1. Exercise a lot - Regular physical activity will help lower your cholesterol and blood pressure, two of the biggest risk factors for stroke.<br>
        2. Stop smoking - Smokers are twice as likely to experience a stroke as nonsmokers. <br>
        3. Eat your vegetables - And beans, whole grains and nuts, too – all of which are staples of a healthy diet. Improving your diet will help lower your cholesterol and blood pressure and help you maintain a healthy weight.<br>
        4. Drink less Alcohol - Alcohol can increase blood pressure and the risk of stroke. Moderation is the key: For men, no more than two drinks a day, and for women, no more than one.<br>
        5. Learn about Afib. - Atrial fibrillation, also known as Afib, is a type of irregular heartbeat. If left untreated, Afib can cause blood clots in the heart that can move to the brain and cause a stroke. Talk to your doctor about Afib if you experience symptoms such as heart palpitations or shortness of breath.<br>
        6. Understand the things you can’t control. - Although improving your diet, ramping up your activity and living a healthy lifestyle can all decrease your risk for stroke, there are some risk factors you cannot control. Things like age, gender and race all play a role in stroke risk, and even though you can’t change those factors, it’s important to understand if you’re more susceptible. <br>
       </div>
    """

    if st.button("Predict"):
        output=predict_stroke(gender,age, hypertension, disease, married,
       work, residence, glucose, bmi,
       smoking)
        st.success('The probability of you getting stroke is VERY HIGH')

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()