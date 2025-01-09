#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the Python script and output binary name
SCRIPT_NAME="src/pdfscaler.py"
OUTPUT_NAME="pdfscaler"

mkdir -p build

# Create a temporary virtual environment
echo "Creating virtual environment..."
python3 -m venv build/venv
source build/venv/bin/activate

# Install PyInstaller in the virtual environment
echo "Installing requirements..."
pip install pyinstaller
pip install -r requirements.txt

# Compile the Python script into a standalone binary
echo "Building standalone binary..."
pyinstaller --onefile --name "$OUTPUT_NAME" "$SCRIPT_NAME"


# Clean up build files and virtual environment
echo "Cleaning up..."
deactivate
rm -rf build *.spec

echo "Build completed. Binary available as './dist/$OUTPUT_NAME'."
