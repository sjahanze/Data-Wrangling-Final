# Data Wrangling Final Project


``` python
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
```

``` python
instagram_data = pd.read_csv("C:/Users/USER/Downloads/Instagram_Analytics.csv")
instagram_data.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | post_id | upload_date | media_type | likes | comments | shares | saves | reach | impressions | caption_length | hashtags_count | followers_gained | traffic_source | engagement_rate | content_category |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | IG0000001 | 2024-11-30 09:25:22.954916 | Reel | 31627 | 7559 | 4530 | 6393 | 615036 | 1007750 | 1340 | 3 | 899 | Home Feed | 4.97 | Technology |
| 1 | IG0000002 | 2025-08-15 09:25:22.954916 | Photo | 63206 | 3490 | 1680 | 6809 | 1237071 | 1345900 | 1351 | 20 | 805 | Hashtags | 5.59 | Fitness |
| 2 | IG0000003 | 2025-09-11 09:25:22.954916 | Reel | 94373 | 3727 | 1761 | 8367 | 1127470 | 1305369 | 242 | 24 | 758 | Reels Feed | 8.29 | Beauty |
| 3 | IG0000004 | 2025-09-18 09:25:22.954916 | Reel | 172053 | 7222 | 2875 | 9290 | 764030 | 897874 | 446 | 11 | 402 | External | 21.32 | Music |
| 4 | IG0000005 | 2025-03-21 09:25:22.954916 | Video | 99646 | 2703 | 4444 | 9746 | 7004 | 495406 | 1905 | 8 | 155 | Profile | 23.52 | Technology |

</div>

``` python
category_mean = instagram_data.groupby("content_category")['engagement_rate'].mean()
instagram_data_merged = instagram_data.merge(category_mean, on="content_category", how="inner")
```

This code calculates the average engagement rate for each content
category and then merges that information back into the main dataset.
First, the data is grouped by content_category and the mean engagement
rate is computed. Then the result is converted into a proper DataFrame
and the column is renamed for clarity. Finally, the mean engagement rate
for each category is merged back into the original dataset so every post
now has access to:

- its own engagement rate

- the average engagement rate of its category

This allows for deeper analysis, such as comparing individual post
performance relative to the typical performance of its category.

Q. Which Content Categories Generate the Highest Engagement?

``` python
plt.figure(figsize=(10,6))
sns.barplot(
    data=instagram_data_merged,
    x="content_category",
    y="engagement_rate_y"
)

plt.xlabel("Content Category")
plt.ylabel("Mean Engagement Rate")
plt.title("Average Engagement Rate by Content Category")

plt.show()
```

![](Final%20Project%20-%20Shahziab%20Jahanzeb_files/figure-commonmark/cell-5-output-1.png)

This bar chart shows the average engagement rate for each content
category in the dataset. Beauty, Lifestyle, and Photography content
stand out as the highest-performing categories, reaching engagement
rates above 14–15%. In contrast, Fitness, Travel, and Food posts show
noticeably lower engagement averages.

This pattern suggests that content theme plays a major role in driving
engagement. Visually appealing or lifestyle-oriented topics generate
stronger audience interaction, while other categories attract less
engagement on average.

``` python
media_followers = instagram_data_merged.groupby('media_type')[['followers_gained']].mean().reset_index()
instagram_data_merged1 = instagram_data_merged.merge(media_followers, on="media_type", how="inner")
```

This code calculates the average number of followers gained for each
media type (Reel, Photo, Video, Carousel) and merges that information
back into the main dataset.

First, the data is grouped by media_type, and the mean followers_gained
is computed and reset into a clean DataFrame. Next, this aggregated
information is merged into the original dataset so each post now
includes:

- its own number of followers gained

- the average followers gained for its media type

This allows for easy comparison between individual posts and the typical
performance of their respective media format.

Q. Do different media types attract different amounts of followers?

``` python
sns.barplot(data = instagram_data_merged1, x = 'media_type', y ='followers_gained_y')

plt.xlabel("Media Type")
plt.ylabel("Followers Gained")
plt.title("Followers Gained by Media Type")
```

    Text(0.5, 1.0, 'Followers Gained by Media Type')

![](Final%20Project%20-%20Shahziab%20Jahanzeb_files/figure-commonmark/cell-7-output-2.png)

This bar chart compares the average number of followers gained across
different media types: Reels, Photos, Videos, and Carousels. The heights
of the bars are nearly identical, showing that all formats generate a
very similar level of follower growth.

Media type does not have a meaningful impact on how many followers a
post gains. This suggests that follower growth in this dataset depends
more on content quality, topic, and distribution, rather than whether
the post is a Reel, Photo, Video, or Carousel.

``` python
instagram_data_merged['upload_date'] = pd.to_datetime(instagram_data_merged['upload_date'])
instagram_data_merged['upload_day'] = instagram_data_merged['upload_date'].dt.day_name()

instagram_data_merged
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|  | post_id | upload_date | media_type | likes | comments | shares | saves | reach | impressions | caption_length | hashtags_count | followers_gained | traffic_source | engagement_rate_x | content_category | engagement_rate_y | upload_day |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | IG0000001 | 2024-11-30 09:25:22.954916 | Reel | 31627 | 7559 | 4530 | 6393 | 615036 | 1007750 | 1340 | 3 | 899 | Home Feed | 4.97 | Technology | 13.927650 | Saturday |
| 1 | IG0000002 | 2025-08-15 09:25:22.954916 | Photo | 63206 | 3490 | 1680 | 6809 | 1237071 | 1345900 | 1351 | 20 | 805 | Hashtags | 5.59 | Fitness | 13.948752 | Friday |
| 2 | IG0000003 | 2025-09-11 09:25:22.954916 | Reel | 94373 | 3727 | 1761 | 8367 | 1127470 | 1305369 | 242 | 24 | 758 | Reels Feed | 8.29 | Beauty | 15.664385 | Thursday |
| 3 | IG0000004 | 2025-09-18 09:25:22.954916 | Reel | 172053 | 7222 | 2875 | 9290 | 764030 | 897874 | 446 | 11 | 402 | External | 21.32 | Music | 14.488062 | Thursday |
| 4 | IG0000005 | 2025-03-21 09:25:22.954916 | Video | 99646 | 2703 | 4444 | 9746 | 7004 | 495406 | 1905 | 8 | 155 | Profile | 23.52 | Technology | 13.927650 | Friday |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 29994 | IG0029995 | 2024-12-18 09:25:22.954916 | Video | 46046 | 8354 | 3847 | 11095 | 597992 | 820688 | 1254 | 18 | 124 | Reels Feed | 8.45 | Travel | 13.757692 | Wednesday |
| 29995 | IG0029996 | 2025-05-05 09:25:22.954916 | Carousel | 67711 | 3266 | 458 | 12380 | 1908094 | 2218288 | 1427 | 4 | 310 | Hashtags | 3.78 | Beauty | 15.664385 | Monday |
| 29996 | IG0029997 | 2025-05-26 09:25:22.954916 | Photo | 52326 | 7328 | 3687 | 7619 | 1984066 | 2447893 | 713 | 4 | 223 | Explore | 2.90 | Photography | 14.816511 | Monday |
| 29997 | IG0029998 | 2025-08-02 09:25:22.954916 | Carousel | 158113 | 5890 | 2573 | 6329 | 1984709 | 2001092 | 1341 | 22 | 978 | Explore | 8.64 | Technology | 13.927650 | Saturday |
| 29998 | IG0029999 | 2025-04-15 09:25:22.954916 | Photo | 76368 | 7115 | 4603 | 11715 | 1867888 | 1987738 | 122 | 27 | 272 | Explore | 5.02 | Technology | 13.927650 | Tuesday |

<p>29999 rows × 17 columns</p>
</div>

This code converts the upload_date column into a proper datetime format
and extracts the day of the week for each post. Converting the date
ensures that pandas recognizes it as a valid datetime object, which
allows us to safely apply .dt functions. The new column, upload_day,
contains the weekday name (e.g., Monday, Tuesday), making it easy to
analyze engagement patterns across different days of the week.

This step is essential for answering the question “Does the day of the
week influence engagement?”, and enables visualizations and group-by
summaries based on posting day.

``` python
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

instagram_data_merged['upload_day'] = pd.Categorical(
    instagram_data_merged['upload_day'],
    categories=day_order,
    ordered=True
)
```

This code defines the correct order of the days of the week and converts
the upload_day column into an ordered categorical variable. By
specifying the order from Monday to Sunday, we ensure that plots and
group-by summaries follow a logical, chronological sequence rather than
sorting alphabetically.

Q. Does the day of the week influence engagement rate?

``` python
sns.lineplot(data = instagram_data_merged, x = 'upload_day', y = 'engagement_rate_x')
plt.xlabel('Upload Day')
plt.ylabel("Mean Engagement Rate")
plt.title("Mean Engagement Rate per Day")
```

    Text(0.5, 1.0, 'Mean Engagement Rate per Day')

![](Final%20Project%20-%20Shahziab%20Jahanzeb_files/figure-commonmark/cell-10-output-2.png)

This line chart displays the average engagement rate for each day of the
week. The engagement pattern is not uniform—there is a clear midweek
spike. Wednesday shows the highest engagement, while Tuesday has one of
the lowest values. Engagement begins to rise again toward the weekend,
peaking moderately on Saturday before declining slightly on Sunday.

The confidence band around the line represents variability within each
day, showing how consistent or inconsistent engagement is on different
days. Overall, this visualization suggests that posting midweek leads to
stronger engagement, making Wednesday the most effective day for
audience interaction.

Q. What factors have the strongest influence on engagement?

``` python
model1 = smf.ols(
    formula='engagement_rate_x ~ caption_length + hashtags_count + reach + impressions + shares + saves',
    data=instagram_data_merged
).fit()

print(model1.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:      engagement_rate_x   R-squared:                       0.139
    Model:                            OLS   Adj. R-squared:                  0.139
    Method:                 Least Squares   F-statistic:                     806.5
    Date:                Wed, 10 Dec 2025   Prob (F-statistic):               0.00
    Time:                        23:08:43   Log-Likelihood:            -1.4201e+05
    No. Observations:               29999   AIC:                         2.840e+05
    Df Residuals:                   29992   BIC:                         2.841e+05
    Df Model:                           6                                         
    Covariance Type:            nonrobust                                         
    ==================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------
    Intercept         38.4351      0.686     56.015      0.000      37.090      39.780
    caption_length     0.0005      0.000      1.909      0.056   -1.28e-05       0.001
    hashtags_count    -0.0033      0.018     -0.189      0.850      -0.038       0.031
    reach           1.446e-05   1.14e-06     12.731      0.000    1.22e-05    1.67e-05
    impressions    -3.176e-05    1.1e-06    -28.897      0.000   -3.39e-05   -2.96e-05
    shares           6.55e-05      0.000      0.597      0.551      -0.000       0.000
    saves           7.021e-05   3.65e-05      1.923      0.055   -1.37e-06       0.000
    ==============================================================================
    Omnibus:                   101424.745   Durbin-Watson:                   1.999
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):      52420184788.548
    Skew:                          61.039   Prob(JB):                         0.00
    Kurtosis:                    6477.770   Cond. No.                     7.75e+06
    ==============================================================================

    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 7.75e+06. This might indicate that there are
    strong multicollinearity or other numerical problems.

This regression model examines how different post-level features
influence engagement rate. Overall, the model explains about 14% of the
variation in engagement, which is reasonable given the unpredictable
nature of social media interactions.

Among the predictors, reach is by far the strongest positive driver of
engagement. Posts that reach more unique users show significantly higher
engagement rates. In contrast, impressions have a strong negative
effect, indicating that repeated views by the same users do not
translate into higher engagement.

The effects of saves and caption length are very small and only
borderline significant, suggesting they have limited practical impact.
Meanwhile, shares and hashtags_count do not significantly predict
engagement in this dataset once reach and impressions are accounted for.

These results highlight that audience distribution (reach) is more
important than content mechanics (hashtags, caption length, or shares)
when it comes to driving engagement on Instagram.
