FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN pip install wldhx.yadisk-direct

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip chromedriver -d ./
RUN wget `yadisk-direct https://disk.yandex.ru/d/Y_fPCLNuh9Px_Q` -O ./google-chrome-stable_114.0.5735.90-1_amd64.deb
RUN wget `yadisk-direct https://disk.yandex.ru/d/WcLcAcaQaYqe2g` -O ./chromedriver

# set display port to avoid crash
ENV DISPLAY=:99

# COPY ./hh_parser_nn ./hh_parser_nn
# COPY ./chromedriver .
# COPY ./google-chrome-stable_114.0.5735.90-1_amd64.deb .
# COPY ./req.txt .
RUN chmod 755 chromedriver
COPY . .
# RUN rm -r json_data
RUN mkdir images
RUN dpkg -i ./google-chrome-stable_114.0.5735.90-1_amd64.deb
RUN pip install -r req.txt
WORKDIR /img_parser
# VOLUME ["hh_parser_data"]
CMD python3 main.py
