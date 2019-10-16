import pandas as pd

df = pd.read_csv('cleaned_insta.csv')
print(df.head(20))
all_posts = {}
museum_likes = {}
museum_associated = {}
# museum,museum_likes,user,post_likes
for index, row in df.iterrows():
  try:
    all_posts[row['user']].append(row['post_likes'])
  except:
    all_posts[row['user']] = [row['post_likes']]
    museum_likes[row['user']] = row['museum_likes']
    museum_associated[row['user']] = row['museum']

museum_diffs = {}
for user in list(all_posts):
  try:
    museum_diffs[museum_associated[user]].append((museum_likes[user] - (sum(all_posts[user]) / len(all_posts[user]))))
  except:
    museum_diffs[museum_associated[user]] = [museum_likes[user] - (sum(all_posts[user]) / len(all_posts[user]))]

print(museum_diffs)
museum_avgs = {}
for museum in list(museum_diffs):
  museum_avgs[museum] = (sum(museum_diffs[museum]) / len(museum_diffs[museum]))

print(museum_avgs)

output_df = pd.DataFrame.from_dict(museum_avgs, orient='index')
output_df.index.name = 'museum'
output_df.columns = ['diff']
output_df = output_df.sort_values(by=['diff'], ascending=True)
output_df.reset_index(level=0, inplace=True)

output_df.to_csv('insta_scores.csv', index=False)