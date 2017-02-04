FROM python

RUN git clone https://github.com/gsmafra/docker-ci-test.git

WORKDIR /docker-ci-test

CMD python main.py