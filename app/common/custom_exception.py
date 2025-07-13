import sys
import traceback

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.message = message
        self.error_detail = error_detail
        self.error_message = self.get_detailed_error_message()
        super().__init__(self.error_message)

    def get_detailed_error_message(self):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return (
            f"{self.message} | Error: {repr(self.error_detail)} | "
            f"File: {file_name} | Line: {line_number}"
        )

    def __str__(self):
        return self.error_message
