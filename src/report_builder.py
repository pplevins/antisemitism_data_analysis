import json
import os

import pandas as pd


class ReportBuilder:
    """A class responsible for creating report files of the analysed data."""

    def __init__(self):
        """Initialize the report builder."""
        self.result_dict = {}
        self.file_path = '../result/result.json'
        self._ensure_file_exists()

    def add_result(self, result_dict: dict):
        """Adds result to the result json file

        Args:
            result_dict (dict): Result dictionary to add.
        """
        self.result_dict.update(result_dict)

    def _ensure_file_exists(self):
        """Ensures the json file exists, creating it if necessary."""

        # Make sure the directory 'result' exists, else creating it.
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({}, file)

    @staticmethod
    def export_cleaned_data(cleaned_data: pd.DataFrame, file_path='../result/tweets_dataset_cleaned.csv'):
        """
        Exports the cleaned data into a csv file.

        Args:
            :param cleaned_data : Cleaned dataset.
            :param file_path: File path.
        """
        cleaned_data.to_csv(file_path, index=False)

    def build_report(self) -> None:
        """Writes the result data to the file in a structured format."""
        if not self.result_dict:
            return  # No result to write

        # Loading the json file into a dictionary.
        with open(self.file_path, "r", encoding="utf-8") as file:
            result = json.load(file)
        result.update(self.result_dict)  # Merging the two dictionaries into one.

        # Updating the json file with the new data.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
