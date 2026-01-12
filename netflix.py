# import pandas as pd
# import matplotlib.pyplot as plt
# file_path = 'mARCqc (1).csv'
# data = pd.read_csv(file_path)
# type_distribution = data['type'].value_counts()
# plt.figure(figsize=(8, 6))
# type_distribution.plot(kind='bar', color=['black', 'crimson'], title='Distribution of Movies vs TV Shows')
# plt.ylabel('Count')
# plt.xlabel('Type')
# plt.xticks(rotation=0)
# plt.show()

##-----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('mARCqc (1).csv')
# df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')
# yearly_trends = df.groupby(df['release_year'].dt.year).size()
# print(yearly_trends)
# yearly_trends.plot(kind='line', marker='o', color='crimson')
# plt.title('Number of Releases Over the Years')
# plt.xlabel('Year')
# plt.ylabel('Number of Releases')
# plt.grid(True)
# plt.show()

##-----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('mARCqc (1).csv')
# country_counts = df['country'].value_counts()
# print(country_counts)
# country_counts.plot(kind='bar', color='black')
# plt.title('Content by Country')
# plt.xlabel('Country')
# plt.ylabel('Number of Releases')
# plt.xticks(rotation=90)
# plt.show()

##-----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('mARCqc (1).csv')
# rating_counts = df['rating'].value_counts()
# print(rating_counts)
# rating_counts.plot(kind='bar', color='crimson')
# plt.title('Distribution of Ratings')
# plt.xlabel('Rating')
# plt.ylabel('Number of Releases')
# plt.xticks(rotation=45)
# plt.show()

##-----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('mARCqc (1).csv')
# movies = df[df['type'] == 'Movie'].copy()
# tv_shows = df[df['type'] == 'TV Show'].copy()
# movies['duration'] = movies['duration'].str.extract(r'(\d+)').astype(float)
# tv_shows['seasons'] = tv_shows['duration'].str.extract(r'(\d+)').astype(float)
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# movies['duration'].plot(kind='hist', bins=20, color='crimson', edgecolor='white')
# plt.title('Movie Durations')
# plt.xlabel('Duration (minutes)')
# plt.subplot(1, 2, 2)
# tv_shows['seasons'].plot(kind='hist', bins=20, color='black', edgecolor='white')
# plt.title('Number of Seasons for TV Shows')
# plt.xlabel('Seasons')
# plt.tight_layout()
# plt.show()

##-----------------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('mARCqc (1).csv')
# top_directors = df['director'].value_counts().head(10)
# print(top_directors)
# top_directors.plot(kind='bar', color='crimson')
# plt.title('Top Directors')
# plt.xlabel('Director')
# plt.ylabel('Number of Releases')
# plt.xticks(rotation=45)
# plt.show()

##-----------------------------------------------------------------------------------------------------------
