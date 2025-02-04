"""Calculates the three smallest and the largest salaries."""


def company_departament(
    departments: dict[str, dict],
    min_salary: float | None = None,
) -> tuple[list, list]:
    """
    Extract minimum and maximum three salaries.

    Args:
        min_salary: float | None = None - minimum salary, which is compared with each department.
        departments: dict[str, dict] - dict of department names and values.

    Returns:
        tuple[list] - tuple for highest and lowest salaries.
    """
    salaries = []

    for department, employees in departments.items():
        if not employees:
            continue
        if min_salary:
            dept_salaries = [salary for salary in employees.values() if salary >= min_salary]
        else:
            dept_salaries = list(employees.values())
        all_salary = sum(dept_salaries)
        average_salary = all_salary / max(len(dept_salaries), 1)
        salaries.append([average_salary, department])
    salaries.sort(key=lambda salary: salary[0])
    min_max_department = [salary[1] for salary in salaries]
    return min_max_department[:3], min_max_department[:-4:-1]
