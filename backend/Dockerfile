FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Copy everything into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]