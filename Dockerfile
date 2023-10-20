# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages

#RUN pip install "uvicorn[standard]"
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/nathanrchn/perplexityai.git 

# Expose port 8000 for the container
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "mobile_app_api:app", "--host", "0.0.0.0", "--port", "8000"]