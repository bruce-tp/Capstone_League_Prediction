from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)

loaded_model = pickle.load(open("rf.pickle","rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result',methods = ['POST'])
def result():
    prediction=''
    if request.method == 'POST':
        
        to_predict_list = request.form.to_dict()
        print(request.form)
        input_list = []
        for i in to_predict_list.values():
            input_list.append(i)
#         df = pd.DataFrame()
        
#         import pickle
#         with open("test.txt", "rb") as fp:   # Unpickling
            
            
    
#             b = pickle.load(fp)
#         for i in b:
#             df [str(b)] = [0]



        df1 = pd.read_csv("out.csv")
        df1 = df1.drop(['Unnamed: 0'], axis=1)
        df1
        df2 = pd.DataFrame()
        df2['Rteam_TOP'] = [input_list[5]]
        df2['Bteam_TOP'] = [input_list[0]]
        df2['Rteam_MIDDLE'] = [input_list[6]]
        df2['Bteam_MIDDLE'] = [input_list[1]]
        df2['Rteam_BOTTOM'] = [input_list[7]]
        df2['Bteam_BOTTOM'] = [input_list[2]]
        df2['Rteam_SUPPORT'] = [input_list[8]]
        df2['Bteam_SUPPORT'] = [input_list[3]]
        df2['Rteam_JUNGLE'] = [input_list[9]]
        df2['Bteam_JUNGLE'] = [input_list[4]]
        frames = [df1, df2]

        result = pd.concat(frames)
        df = pd.get_dummies(result)
        # loaded_model.predict_proba(df)
        # prediction = str (loaded_model.predict_proba(df.tail(1)))
        prediction = loaded_model.predict_proba(df.tail(1))
        return render_template('result.html', prediction=prediction)


        #yoyoyyoyoyo--------------------------

        PEOPLE_FOLDER = os.path.join('static', 'champion_images')
        #full_filename1 = os.path.join(PEOPLE_FOLDER, 'Aatrox.png')

        filename_list = []
        for i in to_predict_list.values():
            print(PEOPLE_FOLDER)
            full_filename = os.path.join(PEOPLE_FOLDER, str(i)+'.png')
            print(full_filename)
            filename_list.append(full_filename)
        return render_template("result.html",prediction= list(prediction),images=filename_list )




if __name__ == "__main__":
    app.run()