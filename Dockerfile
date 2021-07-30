FROM ubuntu:21.10
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip curl xvfb unzip firefox default-jre
RUN apt-get install -y libxss1 libappindicator1 libindicator7
RUN apt-get install -y libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev libgconf-2-4
RUN curl -s "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" -o /tmp/chrome.deb  && apt-get install -y /tmp/chrome.deb
RUN curl -s "http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$(echo $(google-chrome --version) | tr -d 'Google Chrome ' | cut -c1-9))/chromedriver_linux64.zip" -o /tmp/chromedriver.zip && unzip -o /tmp/chromedriver.zip
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz" -P /tmp/ && tar xzf /tmp/geckodriver-v0.24.0-linux64.tar.gz -C /tmp/
RUN wget "https://github.com/allure-framework/allure2/releases/download/2.7.0/allure-2.7.0.zip" -P /tmp/ && unzip /tmp/allure-2.7.0.zip -d /tmp/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV DISPLAY=:99
ENV DOCKER_RUN=true
CMD ./run_tests.sh -po "$PORTAL" -b "$BROWSER" -pa "$PARALLEL"