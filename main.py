from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import matplotlib.pyplot as plt

st.set_page_config(page_title='Sentiment Analysis', layout='wide')
st.title('🌿Sentiment Analysis Dashboard🌿')

# Function to get sentiment icon
def sentiment_icon(polarity):
    if polarity > 0:
        return "😊 Positive", "✅"
    elif polarity < 0:
        return "😢 Negative", "❌"
    else:
        return "😐 Neutral", "➖"

with st.expander('Analyze Text'):
    col1, col2 = st.columns(2)
    
    with col1:
        text = st.text_area('Enter text to analyze:', height=150)
        if text:
            blob = TextBlob(text)
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)
            sentiment, icon = sentiment_icon(polarity)
            
            st.metric('Polarity', f"{polarity} {icon}", delta_color='off')
            st.metric('Subjectivity', subjectivity, delta_color='off')

            # Display sentiment as text with icon
            st.markdown(f"**Sentiment:** {sentiment}")

    with col2:
        pre = st.text_area('Enter text to clean:', height=150)
        if pre:
            cleaned_text = cleantext.clean(pre, clean_all=False, extra_spaces=True, stopwords=True, lowercase=True, numbers=True, punct=True)
            st.write('Cleaned Text:', cleaned_text)

with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload a CSV or Excel file', type=['csv', 'xlsx'])

    def score(x):
        blob1 = TextBlob(str(x))  # Convert to string to avoid TypeError
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0:
            return 'Positive'
        elif x <= 0:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        if upl.name.endswith('csv'):
            df = pd.read_csv(upl)
        else:
            df = pd.read_excel(upl)
        
        st.write(df.head())  # Display the dataframe for user reference

        # Allow user to select the text column
        text_column = st.selectbox('Select the column containing text data', df.columns)
        
        df['score'] = df[text_column].astype(str).apply(score)  # Ensure all data is string
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        # Visualization
        st.subheader('Sentiment Analysis Results')
        sentiment_counts = df['analysis'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'red', 'gray'])
        ax.axis('equal')
        st.pyplot(fig)

        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment_analysis.csv',
            mime='text/csv',
        )
