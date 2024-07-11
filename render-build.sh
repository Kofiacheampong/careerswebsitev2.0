#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install necessary tools
apt-get update && apt-get install -y curl gnupg

# Add the Microsoft repository key and repository
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists
apt-get update

# Install the ODBC driver for SQL Server
ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev

# Verify the driver installation
if ! command -v odbcinst &> /dev/null
then
    echo "odbcinst could not be found"
    exit 1
fi

# Verify the driver installation
odbcinst -q -d -n "ODBC Driver 18 for SQL Server"