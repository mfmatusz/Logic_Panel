import json
from datetime import datetime
from sqlalchemy.orm import Session
from db.database import SessionLocal  # upewnij się, że masz to w swoim projekcie
from models.phone import Phone       # dostosuj ścieżkę, jeśli inaczej nazywasz folder

# === Wczytanie JSON z pliku ===
with open('test/phoneTest.json', 'r') as f:
    phones_data = json.load(f)

# === Start sesji z bazą danych ===
db: Session = SessionLocal()

for item in phones_data:
    phone_id = item["Id_Phone"]
    x_coord = str(item["location"][0])
    y_coord = str(item["location"][1])
    time_full = datetime.strptime(item["TimeStatus"], "%Y-%m-%dT%H:%M:%SZ")
    status = item["Status"] == "active"  # True jeśli "active"
    battery = item["batteryLevel"]

    # Szukaj istniejącego telefonu
    phone = db.query(Phone).filter(Phone.id_phone == phone_id).first()
    if phone:
        # Aktualizacja
        phone.X_coordinate = x_coord
        phone.Y_coordinate = y_coord
        phone.timestatus = time_full
        print(phone.timestatus)
        phone.is_active = status
        phone.battery = battery
    else:
        # Dodanie nowego wpisu
        new_phone = Phone(
            id_phone=phone_id,
            X_coordinate=x_coord,
            Y_coordinate=y_coord,
            timestatus=time_full,
            is_active=status,
            battery=battery
        )
        db.add(new_phone)

# === Zatwierdź i zamknij połączenie ===
db.commit()
db.close()
print(type(time_full))