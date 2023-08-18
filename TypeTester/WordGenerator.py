import time
import requests
import json

from helpers import display_value, record_keystrokes, record_to_word
from constants import (
    RAPID_API_HOST,
    RAPID_API_KEY,
    RAPID_API_URL,
    RAPID_API_HOST_HEADER,
    RAPID_API_KEY_HEADER,
    WORD,
    PRONUNCIATION,
    DEFINITION,
    AVG_TIME_TYPING,
    AVG_HOVER_TIME,
    KEY_BACKSAPCE,
    KEY_ENTER,
    HTTP_200_OK
)


class WordGenerator:
    """
    This class retrieves a random word with its definition and pronunciation from an API
    and provides methods for conducting a typing test and calculating scores.

    Attributes:
        word (str): The randomly generated word.
        definition (str): The definition of the word.
        pronunciation (str): The pronunciation of the word.
    """

    def __init__(self):
        url = RAPID_API_URL

        headers = {
            RAPID_API_KEY_HEADER: RAPID_API_KEY,
            RAPID_API_HOST_HEADER: RAPID_API_HOST,
        }

        response = requests.get(url, headers=headers)

        if response.status_code == HTTP_200_OK:
            response_data = json.loads(response.text)
        self.word_data = response_data[0]

    def calculate_acc_score(self, penalty_count, user_input):
        """
        Calculate the accuracy score based on the user's input.

        Args:
            penalty_count (int): Number of backspaces used by the user.
            user_input (str): The user's input string.

        Returns:
            float: The calculated accuracy score.
        """
        letter_score = 100 / len(self.word)

        score = -letter_score * penalty_count

        for user_char, correct_char in zip(self.word_data[WORD], user_input):
            if user_char == correct_char:
                score += letter_score
            else:
                score -= letter_score

        return max(score, 0)

    def calculate_time_score(self, time_taken):
        """
        Calculate the time score based on the time taken to complete the test.

        Args:
            time_taken (float): Time taken to complete the test.

        Returns:
            float: The calculated time score.
        """

        raw_time_score = (time_taken / AVG_HOVER_TIME) + (
            AVG_TIME_TYPING * (len(self.word_data[WORD]) + 1)
        )

        if raw_time_score < 1:
            final_time_score = 100
        else:
            final_time_score = 100 / raw_time_score

        return max(final_time_score, 0)

    def display_test_results(self):
        display_value("Word", self.word)
        display_value("No of Letters", len(self.word_data[WORD]))
        display_value("User typed", "".join(self.user_input))
        display_value("Time taken", self.time_taken)
        display_value("Accuracy Score", self.acc_score)
        display_value("Time Score", self.time_score)
        display_value("Total Score", (self.acc_score + self.time_score) / 2)
        display_value("Definition", self.word_data[DEFINITION])
        display_value("Pronunciation", self.word_data[PRONUNCIATION])

    def start_test(self):
        """
        Start the typing test, record user input, calculate scores, and display results.
        """
        display_value("Word", self.word)
        print("Test Started. Press '", KEY_ENTER, "' to submit.")
        start_time = time.time()
        key_record = record_keystrokes()
        end_time = time.time()
        self.time_taken = end_time - start_time
        self.user_input = record_to_word(key_record)
        self.acc_score = self.calculate_acc_score(
            key_record.count(KEY_BACKSAPCE), self.user_input
        )
        self.time_score = self.calculate_time_score(end_time - start_time)
