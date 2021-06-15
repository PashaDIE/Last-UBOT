# Feri Ganteng
FROM biansepang/weebproject:buster
#
# Feri
#
RUN git clone -b Last-Userbot https://github.com/PashaDIE/Last-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/PashaDIE/Last-UBOT/Last-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
