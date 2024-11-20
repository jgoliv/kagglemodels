
train_copy = train.copy()

# first glance at the data
train_copy.head()
train_copy.info()

# barplot for categorical variables
def barplot(df, variable):
    var = df[variable]

    plt.figure(figsize=(9, 3))
    sns.countplot(x=var)
    plt.xticks(rotation=60)
    plt.ylabel("Frequency")
    plt.title(variable)

    plt.show()

# looking at the names, we can notice that some of them have titles
name = train_copy.Name # extracting titles from the names
train_copy["Title"] = [n.split(".")[0].split(",")[1].strip() for n in name]

barplot(train_copy, "Title")
