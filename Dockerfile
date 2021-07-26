FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip curl xvfb unzip
RUN apt-get install -y libxss1 libappindicator1 libindicator7
RUN apt-get install -y libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev libgconf-2-4
COPY . /app
WORKDIR /app
RUN curl -s "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" -o /tmp/chrome.deb  && apt-get install -y /tmp/chrome.deb
RUN curl -s "http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$(echo $(google-chrome --version) | tr -d 'Google Chrome ' | cut -c1-9))/chromedriver_linux64.zip" -o /tmp/chromedriver.zip && unzip -o /tmp/chromedriver.zip -d /app/
RUN pip3 install -r requirements.txt
ENV DISPLAY=:99
CMD ./run_tests.sh