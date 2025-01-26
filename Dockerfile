
FROM python:latest

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y chromium
RUN apt-get update && apt-get install -y openjdk-17-jdk-headless
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.17.3/allure-2.17.3.zip \
    && unzip allure-2.17.3.zip -d /opt/ \
    && ln -s /opt/allure-2.17.3/bin/allure /usr/bin/allure
RUN apt-get update && apt-get install -y curl build-essential file git

EXPOSE 4040

# Run the tests and generate Allure report
CMD ["sh", "-c", "pytest --alluredir=/app/allure-results && allure serve /app/allure-results"]
