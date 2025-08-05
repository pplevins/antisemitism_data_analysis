from typing import Any

import pandas as pd


class DataAnalyzer:
    """A class to analyze the data"""

    def __init__(self):
        """Initialize the data analyzer"""
        self.raw_data = None
        self.cleaned_data = None

    def set_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        """
        Set raw data, and return it as a clean dataframe

        Args:
            raw_data (pd.DataFrame): Raw data from CSV file.

        Returns:
            pd.DataFrame: Cleaned data from CSV file.
        """
        self.raw_data = raw_data
        self.cleaned_data = raw_data[['Biased', 'Text']].copy()
        self.cleaned_data['Text'] = (self.cleaned_data['Text']
                                     .str.replace(r'[^\w\s]+', '', regex=True)
                                     .str.lower())
        self.cleaned_data.dropna(subset=['Biased'], inplace=True)
        return self.cleaned_data

    def count_tweets_per_biased(self) -> dict[str, dict[str, int]]:
        """
        Count the number of tweets per biased

        Returns:
             dict[str, dict[str, int]]: A detailed dictionary of tweets per biased.
        """
        count_dict = self.cleaned_data['Biased'].value_counts().to_dict()
        return {'total_tweets':
            {
                'antisemitic': count_dict[1],
                'non_antisemitic': count_dict[0],
                'total': int(self.raw_data['Biased'].count()),
                'unspecified': int(self.raw_data['Biased'].isnull().sum())
            }}

    def mean_word_length(self) -> dict[str, dict[str, float]]:
        """
        Calculate the mean word length per biased.

        Returns:
            dict[str, dict[str, float]]: A detailed dictionary of mean word length per biased.
        """
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

    def most_common_words(self) -> dict[str, dict[str, dict[str, int]]]:
        """
        Count the most common words per biased.

        Returns:
            dict[str, dict[str, dict[str, int]]]: Detailed dictionary of most common words per biased.
        """
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

    def longest_tweets(self) -> dict[str, dict[str, list[str] | Any]]:
        """
        Count the longest 3 tweets per biased.

        Returns:
            dict[str, dict[str, list[str] | Any]]: Detailed dictionary of longest 3 tweets per biased.
        """
        return {'longest_3_tweets':
            {
                'antisemitic':
                    self.raw_data[self.raw_data['Biased'] == 1]['Text']
                    .sort_values(key=lambda x: x.str.len(), ascending=False).head(3).to_list(),
                'non_antisemitic':
                    self.raw_data[self.raw_data['Biased'] == 0]['Text']
                    .sort_values(key=lambda x: x.str.len(), ascending=False).head(3).to_list()
            }}

    def count_uppercase_words(self) -> dict[str, dict[str, int | Any]]:
        """
        Count the number of uppercase words per biased.

        Returns:
            dict[str, dict[str, int | Any]]: Detailed dictionary of count of uppercase words per biased.
        """
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
