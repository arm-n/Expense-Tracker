# Expense Tracker

## Description
The Expense Tracker is a simple Tkinter-based GUI application that allows users to log and manage their daily expenses efficiently. It provides a user-friendly interface to input expense details, categorize them, and track spending over time. The application ensures data persistence using a JSON file, allowing users to retrieve and review their expenses anytime.

## Features
- **Add Expenses**: Users can input the expense amount, description, and category.
- **Expense Validation**: Prevents invalid inputs by handling exceptions (e.g., non-numeric amounts).
- **View Expenses**: Displays all recorded expenses with timestamps.
- **Search Expenses**: Users can search for specific expenses by category or keyword.
- **Data Storage**: Stores expenses in a JSON file for future reference.
- **Clear Expenses**: Allows users to delete all recorded expenses.

## Technologies Used
- Python
- Tkinter (for GUI)
- JSON (for data storage)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/arm-n/Expense-Tracker
   ```
2. Navigate to the project directory:
   ```sh
   cd Expense-Tracker
   ```
3. Install dependencies (if any):
   ```sh
   pip install tk
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## Usage
1. Launch the application.
2. Enter the expense details (amount, category, description) and click **Add Expense**.
3. View all recorded expenses in the display area.
4. Use the **Search** function to filter expenses by category or keyword.
5. Click **Clear Expenses** to reset the expense log.

## Exception Handling
- Ensures that only numeric values are accepted for the expense amount.
- Handles missing or corrupt JSON files gracefully.
- Provides user-friendly error messages when invalid inputs are entered.

## Future Enhancements
- **Monthly Expense Reports**: Generate reports to analyze spending trends.
- **Graphical Insights**: Integrate charts to visualize expense distribution.
- **Export Data**: Allow users to export expense records as CSV or PDF.
- **Cloud Sync**: Option to store expenses in cloud-based databases.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features!

## License
This project is licensed under the MIT License.

