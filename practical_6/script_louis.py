import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
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
penguins_plt_plot(clean_df)
#plt.show()

# Save the plot
penguins_plt_plot(clean_df)
plt.savefig("plot_louis/plt_plot_peng.png", dpi = 300)

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

#########################################################################
### seaborn plot

sns_plot = sns.scatterplot(clean_df, 
                           x = "flipper_length_mm", 
                           y = "body_mass_g", 
                           hue = "species", 
                           palette = "Set2")
plt.title("body mass in function of the flipper length")

sns_plot.figure.savefig("plot_louis/pinguins_sns.png", dpi = 300)

#############################################################################################"
# " plot with plotnine

plot1 = (
    ggplot(clean_df, aes(x = "flipper_length_mm", y = "body_mass_g", color = "species"))
    + geom_point()
    + ggtitle("Body mass in function of the flipper length (plotnine)")
)

plot1.save('plot_louis/plotnine_figure_louis.png', width = 8, height = 6, dpi = 300)
#plot.show()