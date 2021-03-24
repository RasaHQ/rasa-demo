import uuid

from gspread.models import Spreadsheet

from actions.api.gdrive_service import GDriveService


def test_append_row(gdrive):
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
        gdrive_client.SPREADSHEET_NAME, gdrive_client.WORKSHEET_NAME, row_values
    )

    assert worksheet.row_values(2) == row_values


def test_request_spreadsheet():
    gdrive_client = GDriveService()
    spreadsheet = gdrive_client.request_spreadsheet(gdrive_client.SPREADSHEET_NAME)
    assert isinstance(spreadsheet, Spreadsheet)
