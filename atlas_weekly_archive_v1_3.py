"""V1.3: lossless, atomic weekly history storage. ATLAS never rescales scores."""
import json, os, tempfile, threading
from pathlib import Path
PATH = Path(__file__).with_name("atlas_weekly_history_v1_3.json")
LOCK = threading.RLock()
REQUIRED = ("strategic_scorecard","weekly_execution_scorecard","atlas_weekly_brief")

def key_for(record):
    if not isinstance(record,dict) or any(k not in record for k in REQUIRED):
        raise ValueError("Invalid weekly check-in")
    week = record.get("week",{})
    key = week.get("date_range") if isinstance(week,dict) else None
    if not isinstance(key,str) or not key.strip() or len(key)>160:
        raise ValueError("Weekly check-in missing week.date_range")
    return key.strip()

def read():
    if not PATH.exists():
        return {"schema_version":"1.3","weekly_checkins":{}}
    data=json.loads(PATH.read_text(encoding="utf-8"))
    if not isinstance(data,dict) or not isinstance(data.get("weekly_checkins"),dict):
        raise ValueError("Existing weekly archive is invalid; refusing overwrite")
    return data

def store(records):
    updates={key_for(record):record for record in records}
    with LOCK:
        data=read()
        data["weekly_checkins"].update(updates)
        fd,tmp=tempfile.mkstemp(dir=str(PATH.parent),prefix=".atlas_weekly_",suffix=".json")
        try:
            with os.fdopen(fd,"w",encoding="utf-8") as f:
                json.dump(data,f,indent=2,ensure_ascii=False)
                f.write("\n");f.flush();os.fsync(f.fileno())
            os.replace(tmp,PATH)
        finally:
            if os.path.exists(tmp):os.unlink(tmp)
    return len(updates)
