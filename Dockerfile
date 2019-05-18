FROM debian
MAINTAINER w8ay@qq.com
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -x \
    && apt update \
    && apt install libpcap-dev python3 nmap masscan python3-pip -y
RUN mkdir -p /opt/Sclient
COPY . /opt/Sclient

RUN set -x \
    && pip3 install -r /opt/Sclient/requirements.txt

WORKDIR /opt/Sclient
ENTRYPOINT ["python3","main.py"]
