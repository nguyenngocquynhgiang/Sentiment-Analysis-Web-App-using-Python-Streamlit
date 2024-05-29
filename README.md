# Sentiment Analysis 
Welcome to the Sentiment Analysis Dashboard repository! This project provides an interactive web application for performing sentiment analysis on text data. The dashboard is built using Streamlit and leverages TextBlob for sentiment analysis and cleantext for text preprocessing. It supports both individual text analysis and bulk analysis of text data from CSV or Excel files.

![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/a6c83c4d-33fc-424e-ad31-741168ebee82)



## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Future Considerations](#future-considerations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Individual Text Analysis:** Analyze the sentiment of individual text inputs, displaying polarity, subjectivity, and a sentiment icon.
- **Text Cleaning:** Clean text inputs by removing extra spaces, stopwords, punctuation, and converting text to lowercase.
- **CSV/Excel File Analysis:** Upload CSV or Excel files containing text data for bulk sentiment analysis.
- **Visualization:** View sentiment distribution through an interactive pie chart.
- **Download Results:** Download the analyzed data as a CSV file.

## Installation

To run this project locally, you'll need to have Python and pip installed. Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-dashboard.git
   cd sentiment-analysis-dashboard
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, open your web browser and go to `http://localhost:8501`. You will see the Sentiment Analysis Dashboard with the following sections:

1. **Analyze Text:**
   - Enter text in the provided text area to analyze its sentiment.
   - View the polarity, subjectivity, and sentiment icon for the entered text.
   - Optionally, clean the text using the text cleaning functionality.

2. **Analyze CSV:**
   - Upload a CSV or Excel file containing text data.
   - Select the column containing the text data.
   - View the sentiment analysis results and visualize the sentiment distribution.
   - Download the analyzed data as a CSV file.

## Project Structure

```plaintext
sentiment-analysis-dashboard/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Technical Details
![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/a1d2ba2a-d2b9-4136-8901-f7f3768fb297)

### Sentiment Analysis

The sentiment analysis is performed using the TextBlob library. TextBlob provides a simple API for diving into common natural language processing (NLP) tasks, including part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/ac44903d-fc37-412c-b3e2-b0ac4058cbee)

![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/e0cf53f5-3903-4cfa-bccd-fa106ee47d64)

![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/50194cfe-4353-49e7-8c66-8550e0d08141)

### Text Cleaning

Text cleaning is handled using the cleantext library. This library helps preprocess text by removing unnecessary characters, extra spaces, stopwords, and performing other text normalization tasks.
![image](https://github.com/nguyenngocquynhgiang/Sentiment-Analysis-Web-App-using-Python-Streamlit/assets/135851627/6e3feef8-fc6c-492b-a887-15fd8fd9254e)

### Visualization

Visualization of sentiment distribution is done using matplotlib. A pie chart is generated to show the proportion of positive, negative, and neutral sentiments within the analyzed dataset.

## Future Considerations

- **Advanced Sentiment Analysis:** Incorporate more advanced sentiment analysis techniques, such as aspect-based sentiment analysis or emotion detection.
- **Customization Options:** Allow users to customize sentiment analysis parameters, such as sentiment thresholds or sentiment lexicons.
- **Integration with External Data Sources:** Integrate with external data sources like social media APIs for real-time sentiment analysis.
- **Deployment and Scalability:** Optimize the application for deployment on cloud platforms and ensure it can handle large volumes of text data efficiently.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for your interest in the Sentiment Analysis Dashboard! If you have any questions or need further assistance, feel free to open an issue in the repository.
