from pathlib import Path

from sales_report.sales import (
    Sale,
    calculate_product_revenue,
    calculate_total_quantity,
    calculate_total_revenue,
    generate_report,
    read_sales,
)


def test_sale_total():
    sale = Sale(
        product="Laptop",
        quantity=2,
        price=15000000,
    )

    assert sale.total == 30000000


def test_calculate_total_revenue():
    sales = [
        Sale("Laptop", 2, 15000000),
        Sale("Mouse", 5, 250000),
    ]

    assert calculate_total_revenue(sales) == 31250000


def test_calculate_total_quantity():
    sales = [
        Sale("Laptop", 2, 15000000),
        Sale("Mouse", 5, 250000),
    ]

    assert calculate_total_quantity(sales) == 7


def test_calculate_product_revenue():
    sales = [
        Sale("Laptop", 2, 15000000),
        Sale("Mouse", 5, 250000),
        Sale("Laptop", 1, 15000000),
    ]

    result = calculate_product_revenue(sales)

    assert result == {
        "Laptop": 45000000,
        "Mouse": 1250000,
    }


def test_read_sales(tmp_path: Path):
    file_path = tmp_path / "sales.csv"

    file_path.write_text(
        "product,quantity,price\n"
        "Laptop,2,15000000\n"
        "Mouse,5,250000\n",
        encoding="utf-8",
    )

    sales = read_sales(file_path)

    assert len(sales) == 2
    assert sales[0].product == "Laptop"
    assert sales[0].quantity == 2
    assert sales[0].price == 15000000


def test_skip_invalid_row(tmp_path: Path):
    file_path = tmp_path / "sales.csv"

    file_path.write_text(
        "product,quantity,price\n"
        "Laptop,2,15000000\n"
        "Mouse,abc,250000\n"
        "Keyboard,3,500000\n",
        encoding="utf-8",
    )

    sales = read_sales(file_path)

    assert len(sales) == 2


def test_skip_negative_quantity(tmp_path: Path):
    file_path = tmp_path / "sales.csv"

    file_path.write_text(
        "product,quantity,price\n"
        "Laptop,-2,15000000\n"
        "Mouse,5,250000\n",
        encoding="utf-8",
    )

    sales = read_sales(file_path)

    assert len(sales) == 1
    assert sales[0].product == "Mouse"


def test_generate_report():
    sales = [
        Sale("Laptop", 2, 15000000),
        Sale("Mouse", 5, 250000),
    ]

    report = generate_report(sales)

    assert "Tổng số dòng bán hàng: 2" in report
    assert "Tổng số sản phẩm bán: 7" in report
    assert "31,250,000 VND" in report
    assert "Laptop: 30,000,000 VND" in report
