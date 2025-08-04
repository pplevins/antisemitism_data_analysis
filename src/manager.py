from data_analyzer import DataAnalyzer
from data_loader import DataLoader
from report_builder import ReportBuilder


class Manager:
    """A manager class for the data analysis program."""

    def __init__(self):
        self.path = '../data/tweets_dataset.csv'
        self.data_loader = DataLoader()
        self.data_analyzer = DataAnalyzer()
        self.report_builder = ReportBuilder()

    def _load_and_clean(self):
        """Loads the data from the csv file, cleans it, and exports it into a csv file."""
        cleaned_data = self.data_analyzer.set_data(self.data_loader.load_from_csv(self.path))
        self.report_builder.export_cleaned_data(cleaned_data)

    def run(self):
        """Running the application."""
        self._load_and_clean()
        self.report_builder.add_result(self.data_analyzer.count_tweets_per_biased())
        self.report_builder.add_result(self.data_analyzer.mean_word_length())
        self.report_builder.add_result(self.data_analyzer.most_common_words())
        self.report_builder.add_result(self.data_analyzer.longest_tweets())
        self.report_builder.add_result(self.data_analyzer.count_uppercase_words())
        self.report_builder.build_report()
