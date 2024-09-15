from datetime import datetime
import holidays

def get_toll_fee_for_entry(vehicle: str, date: datetime):
    toll_fee_for_entry = 0
    if vehicle in ["motorbike", "tractor", "emergency", "diplomat", "foreign", "military"]:
        print(f"[DEBUG] vehicle is toll free: {vehicle}")
        return 0

    holidays_swe = holidays.country_holidays('SE')

    if date in holidays_swe:
        print(f"[DEBUG] date is a holiday: {date}")
        return 0
    if date.weekday() == 5 or date.weekday() == 6:
        print(f"[DEBUG] date is a weekend: {date}")
        return 0
    toll_fee_for_entry = get_period_toll_fee(date)
    return toll_fee_for_entry

def get_period_toll_fee(date: datetime):
    period_toll_fee = 0
    if date.hour == 6 and date.minute >= 0 and date.minute <= 29:
        print(f"[DEBUG] 06:00 => 06:29 tollfee: 8")
        period_toll_fee += 8
    elif date.hour == 6 and date.minute >= 30 and date.minute <= 59:
        print(f"[DEBUG] 06:30 => 06:59 tollfee: 13")
        period_toll_fee += 13
    elif date.hour == 7 and date.minute >= 0 and date.minute <= 59:
        print(f"[DEBUG] 07:00 => 07:59 tollfee: 18")
        period_toll_fee += 18
    elif date.hour == 8 and date.minute >= 0 and date.minute <= 29:
        print(f"[DEBUG] 08:00 => 08:29 tollfee: 13")
        period_toll_fee += 13
    elif date.hour == 8 and date.minute >= 30 and date.minute <= 59:
        print(f"[DEBUG] 08:30 => 08:59 tollfee: 8")
        period_toll_fee += 8
    elif date.hour >=9 and date.hour <= 14:
        print(f"[DEBUG] 09:00 => 14:59 tollfee: 8")
        period_toll_fee += 8
    elif date.hour == 15 and date.minute >= 0 and date.minute <= 29:
        print(f"[DEBUG] 15:00 => 15:29 tollfee: 13")
        period_toll_fee += 13
    elif date.hour == 15 and date.minute >= 30 and date.minute <= 59:
        print(f"[DEBUG] 15:30 => 15:59 tollfee: 18")
        period_toll_fee += 18
    elif date.hour == 16:
        print(f"[DEBUG] 16:00 => 16:59 tollfee: 18")
        period_toll_fee += 18
    elif date.hour == 17:
        print(f"[DEBUG] 17:00 => 17:59 tollfee: 13")
        period_toll_fee += 13
    elif date.hour == 18 and date.minute >= 0 and date.minute <= 29:
        print(f"[DEBUG] 18:00 => 18:29 tollfee: 8")
        period_toll_fee += 8
    return period_toll_fee

if __name__ == "__main__":
    total_fee = 0
    with open("dataset_car") as file:
         vehicle_entries = file.readlines()

    last_toll_fee = 0
    for vehicle_entry in vehicle_entries:
        vehicle_entry = vehicle_entry.strip()
        entry_vehicle = vehicle_entry.split(',')[0]
        entry_date = datetime.strptime(vehicle_entry.split(',')[1], '%Y-%m-%dT%H:%M:%S')
        print(f"vehicle: {entry_vehicle}, time: {entry_date}")
        toll_fee = get_toll_fee_for_entry(entry_vehicle, entry_date)
        print(f"tollfee for entry: {toll_fee}")
        total_fee += toll_fee
        print("---------------")

    if total_fee > 60:
        print(f"[DEBUG] Total toll fee is higher than 60 sek: {total_fee}")
        total_fee = 60
    print(f"Total toll fee: {total_fee}")

