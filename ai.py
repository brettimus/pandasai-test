# NOTE - to load this script in the repl: 
#          `exec(open("ai.py").read())`

import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from load_data import load_dataframe
import os
from dotenv import load_dotenv

# Get api key for openai 
load_dotenv()
api_token = os.environ.get('OPENAI_API_KEY')

llm = OpenAI(api_token=api_token)

df = load_dataframe()
print("Loaded dataframe")

# EXAMPLE - Only get panda api data
panda_data = df[df["metric"] == "app.panda"]

# NOTE - can pivot the dataframe to support multiple metrics
# df_pivot = df.pivot(index='timestamp', columns='metric', values='value')

print("Creating smart dataframe and asking question")
df = SmartDataframe(df, config={"llm": llm})
result = df.chat('Which metrics have the highest values?')



# # === pandasai sample === #
#
# df = pd.DataFrame({
#     "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
#     "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
#     "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
# })

# from pandasai.llm import OpenAI
# llm = OpenAI(api_token="sk-123")

# df = SmartDataframe(df, config={"llm": llm})
# df.chat('Which are the 5 happiest countries?')