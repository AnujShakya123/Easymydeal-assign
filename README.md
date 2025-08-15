1.) Install Python
Make sure you have Python 3.12 or higher installed.
Check with:
python --version


2.)Install Dependencies
Open a terminal in the project folder and run:
pip install selenium
Download the ChromeDriver executable that matches your Google Chrome version and add it to your system PATH.

3.)Run the Test
From the project root, execute:

This will:
Launch Chrome.
Log into the site(https://www.automationexercise.com/).
Search for a product.
Add it to the cart.
Verify the product name and price.
View Results

PASS → All assertions were successful.

FAIL → The console will show the reason (e.g., “Name mismatch”).
