# Hospital Bed Prediction System


The Hospital Bed Prediction System is a web-based application developed using Python Flask and powered by a machine learning model built with the Random Forest algorithm. This system aims to assist healthcare facilities in predicting the number of hospital beds required based on historical data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Machine Learning Model](#machine-learning-model)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In today's healthcare landscape, efficient allocation of hospital beds is crucial to provide timely medical care to patients. The Hospital Bed Prediction System offers a solution by leveraging historical bed usage data to forecast the number of beds that will be required in the near future. This prediction helps hospitals and healthcare administrators make informed decisions about resource allocation and staffing.

## Features

- **User-Friendly Interface:** The web interface allows users to input details of beds used over a month, which are then stored and used for predictions.

- **Accurate Predictions:** The machine learning model, based on the Random Forest algorithm, has been trained on historical data to provide accurate predictions of future bed requirements.


## Installation

Follow these steps to set up the Hospital Bed Prediction System:

1. Clone this repository:
   ```bash
   git clone https://github.com/vyshakhgnair/hospital-bed-prediction.git
   cd hospital-bed-prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Run the Flask app:
   ```bash
   flask run
   ```

4. Access the app by opening a web browser and navigating to `http://localhost:5000`.

## Usage

1. Open the web browser and go to the system's URL.

2. Enter the details of bed usage for the past month.

3. Click the "Predict" button to get the predicted number of beds required.

4. View the prediction results and data visualizations on the dashboard.

## Data Collection

The system collects data on bed usage, including factors such as the number of occupied beds, medical specialties, and any special events affecting bed demand. This data is essential for training the machine learning model and making accurate predictions.

## Machine Learning Model

The prediction model is built using the Random Forest algorithm, which has been chosen for its ability to handle complex relationships within the data. The model is trained on historical bed usage data and takes into account various features to generate predictions.

## Database

The system utilizes a database to store historical bed usage data. SQLite has been chosen for its simplicity and compatibility with Flask applications.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-new-feature
   ```

3. Make your changes and commit them.

4. Push your changes to your fork:
   ```bash
   git push origin feature-new-feature
   ```

5. Open a pull request describing your changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify this README to suit your repository's specific details. Good luck with your Hospital Bed Prediction System! If you have any questions or need further assistance, don't hesitate to reach out.
