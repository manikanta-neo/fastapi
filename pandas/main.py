import pandas as pd

df = pd.DataFrame(

    {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss. Elizabeth",

        ],

        "Age": [22, 35, 58],

        "Sex": ["male", "male", "female"],

        "college": ["a", "b", "c"],

        "city": ['x', 'Y', 'Z'],

        "mobile":[24324, 12342, 178764]

    }

)

print(df)
print(df["Age"])
ages = pd.Series([22, 35, 58], name="Age")
print(ages)
print(df["Age"].max())
print(df["Age"].min())
print(df)
print(df.describe())

titanic = pd.read_csv("titanic.csv")
print(titanic)