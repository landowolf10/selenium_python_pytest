# Use an official Python runtime as a parent image
FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y wget gnupg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Download and install Firefox
RUN mkdir -p /opt && \
    wget -O /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" && \
    echo "Downloaded Firefox" && \
    ls -l /tmp/firefox.tar.bz2 && \
    tar -xjf /tmp/firefox.tar.bz2 -C /opt/ && \
    echo "Extracted Firefox" && \
    ls -l /opt/firefox && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    echo "Created symlink" && \
    rm /tmp/firefox.tar.bz2 && \
    echo "Removed tar file"

# Set up the working directory
WORKDIR /usr/src/app

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV BROWSER="chrome,firefox"
ENV SELENIUM_GRID_ENABLED="False"

# Run the test runner
CMD ["sh", "-c", "pytest --browser $BROWSER --selenium_grid_enabled $SELENIUM_GRID_ENABLED"]