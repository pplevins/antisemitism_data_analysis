import pandas as pd


class DataAnalyzer:
    def __init__(self):
        self.raw_data = None
        self.cleaned_data = None

    def set_data(self, raw_data):
        self.raw_data = raw_data
        self.cleaned_data = raw_data[['Biased', 'Text']].copy()
        self.cleaned_data['Text'] = (self.cleaned_data['Text']
                                     .str.replace(r'[^\w\s]+', '', regex=True)
                                     .str.lower())
        self.cleaned_data.dropna(subset=['Biased'], inplace=True)
        return self.cleaned_data

    def count_tweets_per_biased(self):
        count_dict = self.cleaned_data['Biased'].value_counts().to_dict()
        return {'total_tweets':
            {
                'antisemitic': count_dict[1],
                'non_antisemitic': count_dict[0],
                'total': int(self.raw_data['Biased'].count()),
                'unspecified': int(self.raw_data['Biased'].isnull().sum())
            }}

    def mean_word_length(self):
        words_df = self.cleaned_data.copy()
        words_df['Text'] = words_df['Text'].str.split(r'\s+')
        words_df['WordsNum'] = words_df['Text'].apply(len)
        words_dict = words_df.groupby(by='Biased')['WordsNum'].mean().to_dict()
        return {'average_length':
            {
                'antisemitic': words_dict[1],
                'non_antisemitic': words_dict[0],
                'total': float(words_df['WordsNum'].mean())
            }}

    def most_common_words(self):
        words_df = self.cleaned_data.copy()
        words_df['Text'] = words_df['Text'].str.split(r'\s+')
        return {'common_words':
            {
                'antisemitic':
                    pd.Series(words_df[words_df['Biased'] == 1]['Text'].sum())
                    .value_counts()[:11].to_dict(),
                'non_antisemitic':
                    pd.Series(words_df[words_df['Biased'] == 0]['Text'].sum())
                    .value_counts()[:11].to_dict(),
                'total':
                    pd.Series(words_df['Text'].sum()).value_counts()[:11].to_dict()
            }}

    def longest_tweets(self):
        return {'longest_3_tweets':
            {
                'antisemitic':
                    self.raw_data[self.raw_data['Biased'] == 1]['Text']
                    .sort_values(key=lambda x: x.str.len(), ascending=False).head(3).to_list(),
                'non_antisemitic':
                    self.raw_data[self.raw_data['Biased'] == 0]['Text']
                    .sort_values(key=lambda x: x.str.len(), ascending=False).head(3).to_list()
            }}

    def count_uppercase_words(self):
        upper_df = self.raw_data[['Biased', 'Text']].copy()
        upper_df['Text'] = (upper_df['Text']
                            .str.replace(r'[^\w\s]+', '', regex=True)
                            .str.split(r'\s+')
                            .apply(lambda x: [item for item in x if item.isupper()]))
        upper_dict = upper_df.groupby(by='Biased')['Text'].sum().apply(len).to_dict()
        return {'uppercase_words':
            {
                'antisemitic': upper_dict[1],
                'non_antisemitic': upper_dict[0],
                'total': len(upper_df['Text'].sum())
            }}
