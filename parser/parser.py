import docx  # To handle .docx files
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from decimal import Decimal


class FinancialTerms(BaseModel):
    Counterparty: str = Field(alias="Party A")
    Initial_Valuation_Date: str = Field(alias="Initial Valuation Date")
    Notional: str = Field(alias="Notional Amount (N)")
    Valuation_Date: str = Field(alias="Valuation Date")
    Maturity: str = Field(alias="Termination Date")
    Underlying: str = Field(alias="Underlying")
    Coupon: str = Field(alias="Coupon (C)")
    Barrier: str = Field(alias="Barrier (B)")
    Calendar: str = Field(alias="Business Day")

    # validate coupon to be pourcentage %
    @field_validator("Coupon")
    def parse_coupon(cls, value):
        """
        Parse coupon value to a Decimal if it is a percentage
        """
        if "%" not in value:
            raise ValueError("Coupon should be a percentage")
        return Decimal(value.replace("%", ""))

    @field_validator("Initial_Valuation_Date", "Valuation_Date", "Maturity")
    def parse_date(cls, value):
        """
        Parse date in the format 'day month year' to a datetime object.
        """
        try:
            return datetime.strptime(value, "%d %B %Y")
        except ValueError:
            raise ValueError(
                "Invalid date format. Should be in the format 'day month year'"
            )


def extract_table_key_value_pairs(docx_path):
    """
    This function extracts key-value pairs from tables in a .docx file.
    This requires knowing the structure of the tables in the document to be
    a simple two-column table with the key in the first column and the
    value in the second column.
    """
    document = docx.Document(docx_path)
    table_data = {}
    try:
        for table in document.tables:
            for row in table.rows:
                # Skip rows with fewer than 2 cells
                if len(row.cells) < 2:
                    continue

                key = row.cells[0].text.strip()
                value = row.cells[1].text.strip()

                # Only add non-empty key
                if key:
                    table_data[key] = value

        return table_data

    except Exception as e:
        print(f"Error processing table: {str(e)}")
        return {}


def extract_entities(table_data: dict) -> FinancialTerms:
    """
    Extract and validate financial terms from table data.
    - Only extract fields defined in FinancialTerms (using aliases)
    - Ignore any extra fields not defined in the model
    - Apply field validators (like parse_coupon)
    - Raise ValidationError if required fields are missing
    """
    try:
        return FinancialTerms.model_validate(table_data)
    except Exception as e:
        raise ValueError(f"Invalid financial terms data: {str(e)}")


if __name__ == "__main__":
    docx_path = "ADOR - Data/ZF4894_ALV_07Aug2026_physical.docx"
    print(extract_entities(extract_table_key_value_pairs(docx_path)))
