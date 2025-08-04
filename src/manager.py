from src.data_analyzer import DataAnalyzer
from src.data_loader import DataLoader
from src.report_builder import ReportBuilder


class Manager:
    def __init__(self):
        self.path = '../data/tweets_dataset.csv'
        self.data_loader = DataLoader()
        self.data_analyzer = DataAnalyzer()
        self.report_builder = ReportBuilder()

    def run(self):
        self.report_builder.export_cleaned_data(self.data_analyzer.set_data(self.data_loader.load_from_csv(self.path)))
        self.report_builder.add_result(self.data_analyzer.count_tweets_per_biased())
        self.report_builder.add_result(self.data_analyzer.mean_word_length())
        self.report_builder.add_result(self.data_analyzer.most_common_words())
        self.report_builder.add_result(self.data_analyzer.longest_tweets())
        self.report_builder.add_result(self.data_analyzer.count_uppercase_words())
        self.report_builder.build_report()
