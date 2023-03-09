FROM python:3.9 as selenium-base
WORKDIR /app

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get -y update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install chromedriver
RUN apt-get install -yqq unzip \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && apt-get clean \
    && apt-get remove -y unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip and install selenium, pytest, and webdriver-manager
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

FROM selenium-base as selenium-pytest-mip
WORKDIR /app

# copy pytest tests to /app
COPY tests/pytest.ini pytest.ini
COPY tests/project_parameters.py project_parameters.py
COPY tests/test_*.py ./
COPY tests/conftest.py conftest.py
COPY tests/pytest_report.css pytest_report.css

# define the container entrypoint script
COPY entrypoint.sh entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
