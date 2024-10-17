FROM python:latest

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y chromium

RUN apt-get update && apt-get install -y curl build-essential file git
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /root/.bashrc

RUN /bin/bash -c "source /root/.bashrc && eval \"\$($(/home/linuxbrew/.linuxbrew/bin/brew shellenv))\""
RUN /bin/bash -c "source /root/.bashrc && brew install allure"
RUN ln -s /home/linuxbrew/.linuxbrew/bin/allure /usr/local/bin/allure
RUN /bin/bash -c "source /root/.bashrc && allure --version"


RUN python -m pytest -v tests/ --alluredir=allure-results
EXPOSE 8080:8080

CMD ["allure", "serve", "allure-results", "--port", "8080"]
