import pandas, matplotlib.pyplot as plt, seaborn as sns, plotly.express as px 
from plotnine import ggplot, aes, geom_point, ggtitle,labs, geom_histogram, geom_bar


#Load the ‘penguins’ dataset using seaborn. Remove any rows with missing values. Hint: Check out how to use the dropna() function.

""" penguins = sns.load_dataset("penguins")

penguins_clean = pandas.DataFrame.dropna(penguins)


#Plot a scatterplot using matplotlib. 
#The plot should show flipper length on the x-axis and body mass on the y-axis. Add an informative title, xlabel and ylabel. Save the plot.


plt.scatter(data=penguins_clean,x="flipper_length_mm",y="body_mass_g")
plt.title("Flipper length vs Body Mass")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("pyplot.png")
plt.show()

#Create the same plot but using plotly. Save an interactive file (.html).

plotly_fig = px.scatter(
    penguins_clean,
    x="flipper_length_mm",
    y="body_mass_g",
    labels={
        "flipper_length_mm": "Flipper length (mm)",
            "body_mass_g": "Body mass (g)"},
    title="Flipper length vs Body Mass")

plotly_fig.write_html("plotly.express.html")
plotly_fig.show()

#Create and save the same plot using seaborn instead. See if you can set colors based on species.

sns.relplot(data=penguins_clean,x="flipper_length_mm",y="body_mass_g",hue="species")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("snsplot.png")
plt.show()


#Finally, try it out using plotnine. To save the plot you will need to import and use the function ggsave. 
#A good practice is to always import any packages or functions at the top of your script.)



plotnyne = (
    ggplot(penguins_clean, aes(x="flipper_length_mm", y="body_mass_g",color="species"))
    +geom_point()
    +labs(x="Flipper length (mm)",y="Body mass (g)")
    +ggtitle("Flipper length vs Body Mass"))

plotnyne.show() 

plotnyne.save("plotnyne.png")

#Create a histogram to show the distribution of the bill lengths in the data. Use the function you like best.

plotnyne_histo = (
    ggplot(penguins_clean, aes(x="bill_length_mm"))
    +labs(x="Bill length (mm)")
    +geom_histogram(binwidth=2))

plotnyne_histo.show()

#Use the pandas library to group the penguins data by island and calculate the mean value of body mass per island. 
#Save the results to a new variable. Create a bar plot where each bar represents the average body mass of one island.

avg_mass_island = penguins_clean.groupby("island")["body_mass_g"].mean().reset_index() #reset_index to preserve output as DataFrame. Makes it easier for downstream plotting imo

print(avg_mass_island)

island_mass = (
    ggplot(avg_mass_island, aes(x="island",y="body_mass_g",fill="island"))
    +labs(x="Island", y="Body mass (g)", title="Average body mass of penguins per island") 
    +geom_bar(stat="identity"))

island_mass.show()
 
#Optional:

#Create two (or more) plots of your own choosing to visualize the penguins data. Use seaborn and try to subplot them together. 
#Create a palette or use one of seaborn’s pre-existing palettes to separate the data by any factor you think is appropriate. (island, sex, species, etc.. )

fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(12,5))

sns.violinplot(
    data=penguins_clean,
    x="species",
    y="bill_length_mm",
    hue="species",
    palette=sns.color_palette("tab10"),
    ax=ax1
)

sns.boxplot(
    data=penguins_clean,
    x="sex",
    y="body_mass_g",
    hue="sex",
    palette=sns.color_palette("tab10"),
    ax=ax2
)

sns.histplot(
    data=penguins_clean,
    x="island",
    y="species",
    hue="island",
    palette=sns.color_palette("tab10"),
    ax=ax3
)

plt.tight_layout()
plt.show()

# Additional plotting assignment (optional)

# Plot a distribution plot of the penguin flipper length using a histogram.

sns.histplot(
    data=penguins_clean,
    x="flipper_length_mm"
)

# What does this plot show? What are some conclusions you can draw from it?
# ANS:_ 
# What happens if you vary the amount of bins in the plot? Why?
# ANS:
# Add appropriate y and x-labels, as well as a title.

plt.xlabel("Flipper length (mm)")
plt.title("Flipper length distribution")

plt.show()

# Save the plot.

plt.savefig("flipperlngth_histplot.png")
 """

# Read the data CNV_log2_skin_melanoma.csv from the practice dugga (available on Canvas) using pandas.

melanoma = pandas.read_csv("CNV_log2_skin_melanoma.csv")
print(melanoma)

# Create a violinplot (the seaborn package is useful for this) with chromosome on the x-axis and cnv_log2 on the y-axis. Add informative titles and save the plot.

sns.violinplot(
    data=melanoma,
    x="chromosome",
    y="cnv_log2",
)
plt.xlabel("Chromosome")
plt.ylabel("CNV log2")
plt.title("Chrosome vs Copy Number Variation")
plt.show()

# What do you see? Which chromosome(s) has the largest CNV interval? Which chromosome(s) has the smallest interval? Do the intervals add up with the numbers in the dataframe you used for the plot?
# ANS: 
# Check the axes and labels. Is there something that could be changed to improve the plot?
# ANS:
