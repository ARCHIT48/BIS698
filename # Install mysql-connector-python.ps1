# Install mysql-connector-python
pip install mysql-connector-python

# Optionally, you can specify the Python interpreter
# python -m pip install mysql-connector-python

# List installed pip packages to verify installation
pip list

# Check if mysql-connector-python is installed (simple check)
$pipList = pip list
if ($pipList -like "*mysql-connector-python*") {
    Write-Host "mysql-connector-python is installed."
} else {
    Write-Host "mysql-connector-python is not installed. Please check your Python environment and pip path."
}
