import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import ggplot, aes, geom_point, labs

#Load the ‘penguins’ dataset using seaborn. Remove any rows with missing values.
penguins = sns.load_dataset("penguins").dropna()

#Plot a scatterplot using matplotlib. The plot should show flipper length on the x-axis and body mass on the y-axis. Add an informative title, xlabel and ylabel. Save the plot.
x = penguins["flipper_length_mm"]
y = penguins["body_mass_g"]
plt.scatter(x, y)
plt.title("Flipper length vs body mass in penguins")
plt.xlabel("Flipper length, mm")
plt.ylabel("Body mass, g")
plt.savefig("Flipper_vs_weight_matplotlib.png")

#Create the same plot but using plotly. Save an interactive file (.html).
fig_plotly = px.scatter(
    penguins, 
    x="flipper_length_mm", 
    y="body_mass_g", 
    title="Flipper length vs body mass in penguins")

fig_plotly.write_html("Flipper_vs_weight_plotly.html")

#Create and save the same plot using seaborn instead. See if you can set colors based on species.
fig_sns = sns.relplot(data=penguins,
            kind="scatter",
            x="flipper_length_mm", 
            y="body_mass_g", 
            hue="species")
fig_sns.set(title = "Flipper length vs body mass in penguins")
plt.tight_layout()
plt.savefig("Flipper_vs_weight_sns.png")

#Finally, try it out using plotnine. To save the plot you will need to import and use the function ggsave
fig_plotnine = (ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g", color= "species"))
                + geom_point())

fig_plotnine = fig_plotnine + labs(
    title="Flipper length vs body mass in penguins",
    x="Flipper length, mm",
    y="Body mass, g"
)

fig_plotnine.save("Flipper_vs_weight_plotnine.png")

#Create a histogram to show the distribution of the bill lengths in the data. Use the function you like best.
hist_sns = sns.displot(data=penguins, x="bill_length_mm")
hist_sns.set(title = "Bill length distribution")
plt.tight_layout()
plt.savefig("bill_length_hist_sns.png")

#Use the pandas library to group the penguins data by island and calculate the mean value of body mass per island.
#Save the results to a new variable. Create a bar plot where each bar represents the average body mass of one island.
new = penguins[["body_mass_g"]].groupby(penguins["island"]).mean()
print(type(new))
mass_bar=sns.catplot(data=new, x="island", y="body_mass_g", kind="bar", hue="island")
mass_bar.set(title = "Mean body weight of penguins on different islands")
plt.tight_layout()
plt.savefig("mean_mass_bar_sns.png")

#Create two (or more) plots of your own choosing to visualize the penguins data. 
#Use seaborn and try to subplot them together. 
#Create a palette or use one of seaborn’s pre-existing palettes to separate the data by any factor you think is appropriate.
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 8), sharex = True, sharey = False)
sns.set_palette(palette="Set2")
sns.boxplot(data=penguins, x="species", y="body_mass_g", hue="sex", ax=axes[0])
sns.boxplot(data=penguins, x="species", y="bill_depth_mm", hue="sex", ax=axes[1])
sns.boxplot(data=penguins, x="species", y="bill_length_mm", hue="sex", ax=axes[2])
sns.boxplot(data=penguins, x="species", y="flipper_length_mm", hue="sex", ax=axes[3])
fig.suptitle("Physical chracteristics of penguins depending on their species and sex", fontsize=20)
plt.savefig("everything.png")

#relationship between bill depth and length by specie and island
h = sns.FacetGrid(penguins, col="island", hue="species", palette="Set2")
h.map(sns.scatterplot, "bill_length_mm", "bill_depth_mm")
h.add_legend()
plt.savefig("bill_depth_length.jpg")
