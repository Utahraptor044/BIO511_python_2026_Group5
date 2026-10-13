import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from plotnine import ggplot, aes, geom_point, ggtitle, xlab, ylab, ggsave

data_p = sns.load_dataset("penguins")
# transform the data into a pandas dataframe
# df = pd.DataFrame(data_p) 
clean_df = pd.DataFrame.dropna(data_p)

# create the penguins plot with pyplot (mathplotlib)
def penguins_plt_plot(data):
    plt.scatter(data["flipper_length_mm"], data["body_mass_g"])
    plt.title("Body mass in function of flipper length")
    plt.xlabel("Flipper length (in mm)")
    plt.ylabel("Body mass (in grams)")


#print the plot
#penguins_plt_plot(clean_df)
#plt.show()

# Save the plot
penguins_plt_plot(clean_df)
plt.savefig("plot_louis/plt_plot_peng.png", dpi = 300)

#close the current figure
plt.close()

###
# Create a plot with plotly

def penguins_px_plot(data):
    fig = px.scatter(
        data_frame = data,
        x = "flipper_length_mm",
        y = "body_mass_g",
        title = "Body mass in function of the flipper length",
        labels = {
            "flipper_length_mm" : "Flipper length (mm)",
            "body_mass_g" : "Body mass (in g)"
            }
        )
    return fig

    

fig = penguins_px_plot(clean_df)
#fig.show()
fig.write_html("plot_louis/pinguins_louis.html")

plt.close()

#########################################################################
### seaborn plot

sns_plot = sns.scatterplot(clean_df, 
                           x = "flipper_length_mm", 
                           y = "body_mass_g", 
                           hue = "species", 
                           palette = "Set2")
plt.title("body mass in function of the flipper length")

sns_plot.figure.savefig("plot_louis/pinguins_sns.png", dpi = 300)

plt.close()

#############################################################################################"
# " plot with plotnine

plot1 = (
    ggplot(clean_df, aes(x = "flipper_length_mm", y = "body_mass_g", color = "species"))
    + geom_point()
    + ggtitle("Body mass in function of the flipper length (plotnine)")
)

plot1.save('plot_louis/plotnine_figure_louis.png', width = 8, height = 6, dpi = 300)
#plot.show()

##################################################################

### Histogramme de la distribution de la longueur du bec - bill_length_mm

# x = bill length, y = number of occurences. 

# Create a new figure
plt.figure()

hist_data = clean_df["bill_length_mm"]

plt.hist(hist_data, bins = 20, color = "lightgreen", edgecolor = "black")
plt.title("Bill length distribution")
plt.xlabel("Bill length")
plt.ylabel("Frequencies")
plt.savefig("plot_louis/hist_bill_pen.png", dpi = 300)

###############################################################################""
### Separate the penguins body_mass_g by island

island_data = clean_df[["island", "body_mass_g"]]
isl_group = island_data.groupby(by = "island")
mean_isl = isl_group["body_mass_g"].mean()
print("Mass mean by island (g):\n", mean_isl)
#graphic = 
#isl_group.plot.bar(x = "island", y = "body_mass_g")

sns.violinplot(
    data = island_data,
    x = "island",
    y = "body_mass_g",
    hue = "island",
    palette = "Set2",
)
plt.title("Body mass distribution by island")
plt.xlabel("Island")
plt.ylabel("Body mass (g)")
plt.savefig("plot_louis/violin_mass_pen.png", dpi = 300)
