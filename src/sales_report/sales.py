import csv
import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class Sale:
    product: str
    quantity: int
    price: float

    @property
    def total(self) -> float:
        return self.quantity * self.price


def read_sales(path: Path) -> list[Sale]:
    sales: list[Sale] = []

    try:
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {"product", "quantity", "price"}

            if not reader.fieldnames or not required_columns.issubset(
                set(reader.fieldnames)
            ):
                raise ValueError(
                    "CSV phải có các cột: product, quantity, price"
                )

            for row in reader:
                try:
                    product = row["product"].strip()
                    quantity = int(row["quantity"])
                    price = float(row["price"])

                    if not product:
                        raise ValueError("Tên sản phẩm không được trống")

                    if quantity < 0 or price < 0:
                        raise ValueError(
                            "Số lượng và giá không được âm"
                        )

                    sale = Sale(
                        product=product,
                        quantity=quantity,
                        price=price,
                    )

                    sales.append(sale)

                except (KeyError, ValueError) as error:
                    logger.warning(
                        "Bỏ qua dòng dữ liệu lỗi: %s | Lỗi: %s",
                        row,
                        error,
                    )

    except FileNotFoundError:
        logger.error("Không tìm thấy file: %s", path)
        raise

    return sales


def calculate_total_revenue(sales: list[Sale]) -> float:
    return sum(sale.total for sale in sales)


def calculate_total_quantity(sales: list[Sale]) -> int:
    return sum(sale.quantity for sale in sales)


def calculate_product_revenue(sales: list[Sale]) -> dict[str, float]:
    revenue: dict[str, float] = {}

    for sale in sales:
        if sale.product not in revenue:
            revenue[sale.product] = 0

        revenue[sale.product] += sale.total

    return revenue


def generate_report(sales: list[Sale]) -> str:
    total_revenue = calculate_total_revenue(sales)
    total_quantity = calculate_total_quantity(sales)
    product_revenue = calculate_product_revenue(sales)

    lines = [
        "========== SALES REPORT ==========",
        f"Tổng số dòng bán hàng: {len(sales)}",
        f"Tổng số sản phẩm bán: {total_quantity}",
        f"Tổng doanh thu: {total_revenue:,.0f} VND",
        "",
        "Doanh thu theo sản phẩm:",
    ]

    for product, revenue in product_revenue.items():
        lines.append(f"- {product}: {revenue:,.0f} VND")

    lines.append("===============================")

    return "\n".join(lines)
