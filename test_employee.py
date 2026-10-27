from employee import employee_details

def test_employee_details():
    result = employee_details("Darshan", "420", "IT", "15000")
    expected = "Name: Darshan\nEmployee ID: 420\nDepartment: IT\nSalary: 15000"

    assert result == expected