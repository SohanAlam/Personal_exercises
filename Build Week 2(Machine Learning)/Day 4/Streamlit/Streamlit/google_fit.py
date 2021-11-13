import streamlit as st
from PIL import Image
import pandas as pd
import csv



def main():
    #Logo and page

    img = Image.open('Google_Fit_icon.jpg')
    st.set_page_config(page_title='Google Fit',page_icon=img,layout="centered")

    #begininng logo
    #img1 = Image.open('fit-removebg.png')
    #load_img1 = st.image(img1,use_column_width=True)  

    # Sidebar

    option_header = st.sidebar.header('Menu')
    option = st.sidebar.selectbox('Navigate to',('Start Page','Personalization','Activities'))
    st.sidebar.write('\n')
    st.sidebar.write('\n')

    if option == 'Start Page':
        st.write('\n')
        st.write('\n')
        st.write('\n')
        img1 = Image.open('Google_Fit_icon_1.jpg')
        load_img1 = st.image(img1,use_column_width=True)
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')

        if(st.sidebar.button("About us")):
            st.sidebar.text("""      V1.00 \n Developer: Team Google Fit \n Pablo, Sohan & Shahiq""")
 
    if option == 'Personalization':

        img_small = Image.open('fit.png')
        load_img_0 = st.image(img_small,use_column_width=True)
   
        user_name = st.text_input("Full Name")
        #menu_main = st.selectbox('Menu',('Personalization','Entry of day activities','Model'))
        col1,col2,col3 = st.columns((2.5,1,2.5))
 
        with col1:
            user_age = col1.slider('Age (in years)', min_value=0, max_value=100, step=1)
            user_gender1 = st.selectbox('Gender',('Male', 'Female'))

        with col3:
            weight = st.number_input("Weight (in kg)",step=0.5,help=f"To convert lbs to kg refer to the conversion calculator in sidebar")
            if (weight <= 0):
                st.markdown("<h6 style=' text-align: right;color: red;'>Enter the value of weight</h1>",unsafe_allow_html=True)

            height_cm = st.number_input("Height (in cm)",step=0.1,help=f"To convert m or ft to cm refer to the conversion calculator in sidebar")
            if (height_cm <= 0):
                st.markdown("<h6 style=' text-align: right;color: red;'>Select the appropriate height in cm</h1>",unsafe_allow_html=True)
            

    # to push the proceed button down
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')        
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')        
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')
        col2.write('\n')

        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')



        ct_cb = st.sidebar.checkbox("Conversion Calculator")

        if ct_cb == True:
            st.sidebar.header("Conversion Calculators")
            st.sidebar.write('\n')
        
            st.sidebar.header("Weight Calculator - lb to kg")

            weight_lbstokgs = st.sidebar.number_input("Enter your weight (in lb)",step=0.5)
            weight_inkg = (weight_lbstokgs/2.205)


            if(st.sidebar.button('Calculate Weight')):
            
            # print weight in kg
                st.sidebar.markdown('{} kg'.format(round(weight_inkg,1)))

            st.sidebar.write('\n')
            st.sidebar.write('\n')
            st.sidebar.write('\n')
            st.sidebar.write('\n')


        # TAKE HEIGHT INPUT
            st.sidebar.header("Height Calculator - m/ft to cm")
            status = st.sidebar.radio(label= 'Select your height format: ',options = ['Meters', 'Feet']) 

            st.sidebar.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

            if(status == 'Meters'):
                # take height input in centimeters 
                height_inm = st.sidebar.number_input('Enter your height (in Metres)')
                height_incm = (height_inm*100)
            
                if(st.sidebar.button('Calculate Height')):
                    st.sidebar.markdown('{} cm'.format(round(height_incm,1)))
            else:
                height_inft = st.sidebar.number_input('Enter your height (in Feets)')
                height_fincm = (height_inft*30.48)
            
                if(st.sidebar.button('Calculate Height')):
                    st.sidebar.markdown('{} cm'.format(round(height_fincm,1)))
        
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')        
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')        
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')        
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')


        if(st.sidebar.button("About us")):
            st.sidebar.text("""      V1.00 \n Developer: Team Google Fit \n Pablo, Sohan & Shahiq""")
        
        if col2.button('Proceed'):
                    # print the BMI INDEX
            
            bmi = weight / ((height_cm/100) **2)
            st.markdown("BMI Index = {}".format(round(bmi,2)))
            
            # give the interpretation of BMI index
            if(bmi < 16):
                st.error("Extremely Underweight!")
            elif(bmi >= 16 and bmi < 18.5):
                st.warning("Underweight!")
            elif(bmi >= 18.5 and bmi < 25):
                st.success("Healthy")       
            elif(bmi >= 25 and bmi < 30):
                st.warning("Overweight")
            elif(bmi >= 30):
                st.error("Extremely Overweight")
            st.write('\n')
            st.write('\n')

            daily_calories_male = (1.2*(88.362 + (13.397*weight)+(4.799*height_cm)-(5.677*user_age)))
            daily_calories_female = (1.2*(447.593 +(9.247*weight)+(3.098*height_cm)-(4.330*user_age)))

            if user_gender1 == 'Male':
                text_male = '<p style="font-family:Times New Roman; color:Blue; font-size: 18px;">Average Calories intake = {} Cal/day</p>'
                st.markdown(text_male.format(round(daily_calories_male,0)),unsafe_allow_html=True)
            else:
                text_female = '<p style="font-family:Times New Roman; color:Blue; font-size: 18px;">Average Calories intake = {} Cal/day</p>'
                st.markdown(text_female.format(round(daily_calories_female,0)),unsafe_allow_html=True)

    # myfile = open('dummy.csv','w+')
    # #my_file = open('dummy1.csv','a')

    # myfile.write("\rFull Name: "+user_name+"\r")
    # myfile.write("Age: "+str(user_age)+" \r")
        
    # myfile.write("Gender: "+user_gender1+" \r")
    # myfile.write("Weight: "+str(weight)+" \r")
    # myfile.write("Height: "+str(height_cm)+"\r")
    # myfile.write("BMI: "+str(bmi)+"\r")

            list_1 = ['Full Name','Age','Gender','Weight','Height','BMI']
            list_2 = [user_name,user_age,user_gender1,weight,height_cm,bmi]
            myfile = open('dummy.csv','w+')
            writer = csv.writer(myfile)
            writer.writerows(map(lambda x:x,([list_1,list_2])))
    #writer.writerow(map(lambda x:x,(list_2)))
    #writer.writerows(map(lambda x:x,[list_2]))
            myfile.close()

        
    if option == 'Activities':

        img_small_new = Image.open('fit.png')
        load_img_4 = st.image(img_small_new,use_column_width=True)
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')
        st.sidebar.write('\n')

        if(st.sidebar.button("About us")):
            st.sidebar.text("""      V1.00 \n Developer: Team Google Fit \n Pablo, Sohan & Shahiq""")

        url = 'C:/Users/shahi/Desktop/For_Streamlit/Streamlit/dummy.csv'
        df = pd.read_csv(url)
        df_bmi = df['BMI'].values
        #st.markdown(df_bmi)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        if df_bmi >= 30:
            text_bmi30 = '- Start using bi-cycle for commuting within city. \n - Try avoiding sitting still for long hours, stretch yourself after every 40 minutes. \n - Reduce stress. '

            st.error('**HIRE  A  TRAINER  &  IT IS EASY !**')
            st.write(text_bmi30,unsafe_allow_html=True)        

        elif df_bmi >= 25 and df_bmi < 30:
            text_bmi25 = '- Develop interest in an outdoor sport. \n - Cut down carbs. '

            st.warning('**HMM, IT CAN BE REDUCED !**')
            st.write(text_bmi25,unsafe_allow_html=True)   

        elif df_bmi >=18.5 and df_bmi < 25:
            text_bmi185 = '- A little walk can help to remain the same. \n - Eat in limited amounts. '

            st.success('**HURRAY !**')
            st.write(text_bmi185,unsafe_allow_html=True)   

        elif df_bmi >= 16 and df_bmi < 18.5:
            text_bmi16 = '- Try some new recipes. \n - Adequate proportions of meal to be taken. '

            st.warning('**TIME TO EAT SOMETHING MORE !**')
            st.write(text_bmi16,unsafe_allow_html=True)

        elif df_bmi < 16:
            text_bmi_extund = '- EAT, EAT & EAT. \n - Try different flavours of shake and ice-cream. '

            st.warning('**EAT SLEEP REPEAT !**')
            st.write(text_bmi_extund,unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')

        text_shape = '<p style="font-family:Times New Roman; color:Blue; font-size: 30px;">To get into a perfect shape, scan the code below and download the app. </p>'
        st.write((text_shape),unsafe_allow_html=True)
        
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')




        st.header("Scan QR Code")
        img_qrcode = Image.open('QRCode.png')
        qr_code = st.image(img_qrcode,use_column_width=True)

 
    # hrs and min to mins calculator
    # st.sidebar.header("Time Calculator - hr/min to min")
    # hrs = st.sidebar.number_input("Enter your time (in hrs)",step=0.5)
    # mins = st.sidebar.number_input("Enter your time (in mins)",step=0.5)

    # timeinmins = ((hrs*60)+mins)


    # if(st.sidebar.button('Calculate Time')):
        
    #     # print time in mins
    #     st.sidebar.markdown('{} mins'.format(round(timeinmins)))

    # st.sidebar.write('\n')
    # st.sidebar.write('\n')
    # st.sidebar.write('\n')
    # st.sidebar.write('\n')

    
    
        # st.markdown("Daily time spent in different transportation modes")
        # st.write('\n')

        # col4,col5,col6= st.columns((2.5,2.5,4))

        

        # with col4:
        #     st.number_input("Car (in min)",step=1,help=f"to convert hrs to min refer to the calculator in sidebar")
        #     st.write('\n')
        #     st.number_input("Bus (in min)",step=1,help=f"to convert hrs to min refer to the calculator in sidebar")
        #     st.write('\n')
        #     st.number_input("Train (in min)",step=1,help=f"to convert hrs to min refer to the calculator in sidebar")
        #     st.write('\n')
            

        # with col5:
        #     st.write('\n')
        #     st.write('\n')
        #     st.write('\n')
        #     st.number_input("Walking (in min)",step=1,help=f"to convert hrs to min refer to the calculator in sidebar")
        #     st.write('\n')
        #     st.write('\n')
        #     st.number_input("Still (in min)",step=1,help=f"to convert hrs to min refer to the calculator in sidebar")

        # with col6:
        #     st.write("**COLUMN FOR THE GRAPHS**")
       





if __name__ == '__main__':
    main()
    
    
    
