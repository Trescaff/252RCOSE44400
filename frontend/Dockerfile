FROM python:3.10
WORKDIR /app
COPY app_front.py .
COPY templates ./templates
RUN pip install flask requests
CMD ["python", "app_front.py"]