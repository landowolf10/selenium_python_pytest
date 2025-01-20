# Use an official Python runtime as a parent image
FROM python:3.9

# Install dependencies and Rust
RUN apt-get update && apt-get install -y wget gnupg rustc cargo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Download and install Firefox
RUN mkdir -p /opt && \
    wget -O /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    tar -xjf /tmp/firefox.tar.bz2 -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm /tmp/firefox.tar.bz2

# Set up the working directory
WORKDIR /usr/src/app

# Copy your project files
COPY . .

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create and activate virtual environment
RUN virtualenv venv
RUN . venv/bin/activate

# Clear pip cache and install cryptography separately
RUN . venv/bin/activate && pip cache purge
RUN . venv/bin/activate && pip install --no-cache-dir cryptography==42.0.0

# Install remaining Python dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV BROWSER="chrome,firefox"
ENV SELENIUM_GRID_ENABLED="False"

# Run the test runner
CMD ["sh", "-c", ". venv/bin/activate && pytest --browser $BROWSER --selenium_grid_enabled $SELENIUM_GRID_ENABLED"]
