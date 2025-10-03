# Use base Python image
FROM python:3.13.3

# Copy repo into container
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Run Python Program
CMD [ "python3", "./saintly_bot.py" ]
