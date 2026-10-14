# Pull base image
FROM python:3.14-slim

# Install Streamlit
RUN pip install streamlit

# Set working directory
WORKDIR /var

# Copy app.py into the working directory
COPY app.py .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
