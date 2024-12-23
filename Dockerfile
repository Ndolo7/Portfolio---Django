# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /mypage

# Copy dependencies file
COPY requirements.txt /mypage/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /mypage/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Command to run the application
#CMD ["gunicorn", "mypage.wsgi:application", "--bind", "0.0.0.0:8000"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
