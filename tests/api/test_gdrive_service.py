import uuid
from typing import Tuple

from gspread.models import Spreadsheet, Worksheet

from actions.api.gdrive_service import GDriveService


def test_append_row(gdrive: Tuple[GDriveService, Worksheet]):
    # by using a random name we can verify that the line written to the spreadsheet is the one the test wrote
    name = uuid.uuid1().hex
    gdrive_client = gdrive[0]
    worksheet = gdrive[1]
    row_values = [
        "company",
        "use_case",
        "budget",
        "date",
        name,
        "job_function",
        "email",
    ]
    gdrive_client.append_row(
        gdrive_client.SALES_SPREADSHEET_NAME,
        gdrive_client.SALES_WORKSHEET_NAME,
        row_values,
    )

    assert worksheet.row_values(2) == row_values


def test_request_spreadsheet(gdrive: Tuple[GDriveService, Worksheet]):
    gdrive_client = gdrive[0]
    spreadsheet = gdrive_client.request_spreadsheet(
        gdrive_client.SALES_SPREADSHEET_NAME
    )
    assert isinstance(spreadsheet, Spreadsheet)
