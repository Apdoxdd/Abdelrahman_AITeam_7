import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def titanic():
# 1) Loading the data
 raw_data=pd.read_csv("titanic.csv",sep=",")
 print(raw_data.info())
 print(raw_data.head())
 is_valid = raw_data["Sex"].isin(["male", "female"]).all()
 print(is_valid)
 # we check if the sex has only male and female

 # 2) cleaning data:
 #    check where it is NULL
 print(raw_data.isnull().sum())
 #    we see that there are 177 nulls and 687 nulls in cabin
 #    so there's about 20% of ages that are null and 78% of cabins that are null
 #    Since age is an intuitevly important factor in survival and not much is missing 
 #    I will fill the nulls of age with mean value but drop the cabin data column since 
 #    most of it is missing
 raw_data["Age"] = raw_data["Age"].fillna(raw_data["Age"].mean())
 df = raw_data.copy() # to copy the data before anymore changes
 df = df.drop(columns=["Cabin"])
 print(df.info())
 print(df.isnull().sum())
 #    we see now that the age column has no nulls and the cabin column has dropped
 # 3) Exploratory Data Analysis (EDA)
 #    First we check which classes survived the most as different classes often have
 #    different postions on the ship like the front or the back and so on
 #print(df[["Survived", "Pclass"]])
 print((df["Pclass"]==1).sum() ) 
 #    we have around 216 people in first class
 print(df[(df["Survived"]>0)& (df["Pclass"]==1)].sum()) # 133
 #    out of 216 in first class, 133 people survived which is about 62% survival rate
 print((df["Pclass"]==2).sum() ) # 184
 print(df[(df["Survived"]>0)& (df["Pclass"]==2)].sum()) # 82
 #   out of 184 in second class, 82 people survied which is 44% survival rate
 print((df["Pclass"]==3).sum() ) # 491
 print(df[(df["Survived"]>0)& (df["Pclass"]==3)].sum()) #117
 #   out of 491 in third class, only 119 people survived which is about 24% survival rate
 #   as we can see that being higher class, thus being in the middle of the ship when the
 #   when the crash happened, helped much
 #  next we look at mean the of the ages that survived in men and women
 print(df[(df["Sex"]=="male")& (df["Survived"]==1)].sum()) # 109 male survied
 print(df[(df["Sex"]=="female")& (df["Survived"]==1)].sum()) #223
 #   The total number of males survied is 109 out of 332 survivors
 #   The total number of males survied is 109 out of 332 survivors
 mean_male_age = df[(df["Sex"] == "male")]["Age"].mean()
 print(mean_male_age)
 mean_female_age = df[(df["Sex"] == "male")]["Age"].mean()
 print(mean_female_age)
 mean_age_male_survivors = df[(df["Sex"] == "male") & (df["Survived"] == 1)]["Age"].mean()
 print(mean_age_male_survivors)
 mean_age_male_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]["Age"].mean()
 print(mean_age_male_survivors)
 #   as we can see that even tho the number of survivors is different between sexes but still
 #   the average age that survived reamained young 
 #----------------------------------------------------------
 #  4) Visualisations
 survivors_per_class = df.groupby("Pclass")["Survived"].sum()
 survivors_per_class.plot(kind="bar", color="#981012")

 plt.title("Total Survivors per Class")
 plt.xlabel("Passenger Class")
 plt.ylabel("Number of Survivors")
 plt.xticks(rotation=0) 
 plt.tight_layout()
 plt.show()









 #   since we see that the there are a few null age values we can insert
 #   the mean of all ages in them which would't really affect results



if __name__ == "__main__":
    titanic()




