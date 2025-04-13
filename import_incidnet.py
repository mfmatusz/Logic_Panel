import json
from datetime import datetime
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.incident import Incident

# === Wczytanie JSON z pliku ===
with open('test/incydentTest.json', 'r') as f:
    incidents_data = json.load(f)

# === Start sesji z bazą danych ===
db: Session = SessionLocal()

for item in incidents_data:
    incident_id = item["incidentId"]
    
    # Wyciągnięcie numeru z "dev-XXX"
    trigger_phone_str = item["triggerPhoneId"]  # np. "dev-026"
    trigger_phone_id = int(trigger_phone_str.replace("dev-", ""))  # → 26

    photo = item["photo"]
    time_full = datetime.strptime(item["time"], "%Y-%m-%dT%H:%M:%SZ")

    # Sprawdź, czy incydent już istnieje
    incident = db.query(Incident).filter(Incident.id_incident == incident_id).first()
    if incident:
        incident.trigger_phone_id = trigger_phone_id
        incident.photo = photo
        incident.time = time_full
    else:
        new_incident = Incident(
            id_incident=incident_id,
            trigger_phone_id=trigger_phone_id,
            photo=photo,
            time=time_full
        )
        db.add(new_incident)

# === Zatwierdzenie zmian i zamknięcie sesji ===
db.commit()
db.close()
