# Wybierz obraz bazowy Pythona
FROM python:3.11-slim

# Ustaw zmienną środowiskową, która wyłącza buforowanie wyjścia Pythona
ENV PYTHONUNBUFFERED 1

# Utwórz katalog w kontenerze na aplikację
WORKDIR /app

# Zainstaluj zależności (Django)
RUN pip install --upgrade pip && pip install Django==5.1.1

# Skopiuj cały projekt do katalogu /app w kontenerze
COPY . /app/

# Otwarcie portu 8000 w kontenerze
EXPOSE 8000

# Uruchom serwer deweloperski Django na porcie 0.0.0.0:8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
