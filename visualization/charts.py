import os
from datetime import datetime
import matplotlib.pyplot as plt

# Create charts folder if it doesn't exist
CHART_FOLDER = "charts"
os.makedirs(CHART_FOLDER, exist_ok=True)


def _get_chart_path(chart_name):
    """
    Generate a unique filename for the chart.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(CHART_FOLDER, f"{chart_name}_{timestamp}.png")


def _add_value_labels(bars):
    """
    Display values on top of each bar.
    """
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )


def department_chart(data):
    """
    Generates a Department-wise Employee Count Bar Chart.

    Expected data:
    [
        {"department_name": "HR", "employee_count": 12},
        {"department_name": "IT", "employee_count": 25},
        {"department_name": "Finance", "employee_count": 8}
    ]
    """

    if not data:
        raise ValueError("No department data available.")

    departments = [row["department_name"] for row in data]
    employee_counts = [row["employee_count"] for row in data]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        departments,
        employee_counts,
        edgecolor="black",
        linewidth=1
    )

    _add_value_labels(bars)

    plt.title(
        "Employees by Department",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Department", fontsize=12)
    plt.ylabel("Employee Count", fontsize=12)

    plt.xticks(rotation=25)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    file_path = _get_chart_path("department_chart")

    plt.savefig(file_path, dpi=300)

    plt.close()

    return {
        "message": "Department chart generated successfully",
        "chart_path": file_path
    }


if __name__ == "__main__":

    sample_data = [
        {"department_name": "HR", "employee_count": 10},
        {"department_name": "IT", "employee_count": 24},
        {"department_name": "Finance", "employee_count": 15},
        {"department_name": "Marketing", "employee_count": 12},
        {"department_name": "Sales", "employee_count": 20},
    ]

    result = department_chart(sample_data)

    print(result)

def attendance_chart(data):

    status = [row["status"] for row in data]
    count = [row["count"] for row in data]

    plt.figure(figsize=(8,5))

    plt.plot(
        status,
        count,
        marker="o",
        linewidth=3,
        markersize=8
    )

    for x, y in zip(status, count):
        plt.text(x, y, str(y), ha="center", va="bottom")

    plt.title("Attendance Status")
    plt.xlabel("Status")
    plt.ylabel("Employees")
    plt.grid(True, linestyle="--", alpha=0.5)

    file_path = _get_chart_path("attendance_chart")

    plt.tight_layout()
    plt.savefig(file_path, dpi=300)
    plt.close()

    return {
        "message":"Attendance chart generated",
        "chart_path":file_path
    }

def project_chart(data):

    status = [row["status"] for row in data]
    count = [row["count"] for row in data]

    plt.figure(figsize=(8,5))

    bars = plt.barh(
        status,
        count,
        edgecolor="black"
    )

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height()/2,
            str(int(width)),
            va="center"
        )

    plt.title("Projects by Status")
    plt.xlabel("Projects")

    file_path = _get_chart_path("project_chart")

    plt.tight_layout()
    plt.savefig(file_path, dpi=300)
    plt.close()

    return {
        "message":"Project chart generated",
        "chart_path":file_path
    }

def leave_chart(data):

    labels = [row["status"] for row in data]
    values = [row["count"] for row in data]

    plt.figure(figsize=(7,7))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops=dict(width=0.45)
    )

    plt.title("Leave Request Status")

    file_path = _get_chart_path("leave_chart")

    plt.savefig(file_path, dpi=300)
    plt.close()

    return {
        "message":"Leave chart generated",
        "chart_path":file_path
    }

def salary_distribution_chart(data):

    departments = [row["department_name"] for row in data]
    salary = [row["total_salary"] for row in data]

    plt.figure(figsize=(10,6))

    bars = plt.barh(
        departments,
        salary,
        edgecolor="black"
    )

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y()+bar.get_height()/2,
            f"{width:.0f}",
            va="center"
        )

    plt.title("Department-wise Salary Distribution")
    plt.xlabel("Total Salary")

    file_path = _get_chart_path("salary_distribution")

    plt.tight_layout()
    plt.savefig(file_path,dpi=300)
    plt.close()

    return {
        "message":"Salary chart generated",
        "chart_path":file_path
    }

def top_paid_chart(data):

    names = [
        row["employee_name"]
        for row in data
    ]

    salary = [
        row["net_salary"]
        for row in data
    ]

    plt.figure(figsize=(12,6))

    bars = plt.barh(
        names,
        salary
    )

    plt.title("Top 10 Highest Paid Employees")

    plt.tight_layout()

    file_path = _get_chart_path(
        "top_paid"
    )

    plt.savefig(file_path,dpi=300)

    plt.close()

    return {
        "message":"Top paid chart generated",
        "chart_path":file_path
    }