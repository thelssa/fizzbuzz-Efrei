FROM python:3.9-slim
 
WORKDIR /app
 
COPY main.py test_unitaire.py /app/
 
RUN pip install pytest
 
CMD ["pytest", "test_unitaire.py"]
 