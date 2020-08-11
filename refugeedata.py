import pandas as pd
refugee_data = pd.read_csv("/Users/juliasherr/Desktop/Refugee/Data/asylum_seekers.csv")
# print (refugee_data.head(5))
total_pending_start_year = refugee_data ["Tota pending start-year"]
refugee_data.sort_values(by=["Origin"])
origin = refugee_data ["Origin"]
print (origin)
total_pending_start_year = total_pending_start_year.replace ("*", 0)
import matplotlib.pyplot as plt
plt.plot (total_pending_start_year)
plt.ylabel ("Total Pending Start Year")
plt.show ()
