import random
import time

class UserInvolvedVacuum:
    def __init__(self):
        self.battery = 100.0
        self.rooms = {
            "A": {"name": "Room A", "dirt": random.randint(60, 100), "cleaned_percentage": 0.0},
            "B": {"name": "Room B", "dirt": random.randint(60, 100), "cleaned_percentage": 0.0}
        }
        self.total_energy_consumed = 0.0
        self.recharge_count = 0
        self.user_choices_count = 0
        self.start_time = time.time()
        self.cleaning_log = []

    def display_status(self):
        print(f"\n------------------------------------------")
        print(f"🔋 Battery Level: {self.battery:.1f}%")
        print(f"🧹 Room Status Dashboard:")
        for key, data in self.rooms.items():
            print(f"   [{key}] {data['name']}: Remaining Dirt = {data['dirt']}% | Cleaned = {data['cleaned_percentage']}%")
        print(f"------------------------------------------")

    def recharge_battery(self):
        print("\n⚡ Battery is critically low! Forcing return to dock for recharge...")
        time.sleep(1)
        energy_added = 100.0 - self.battery
        self.battery = 100.0
        self.recharge_count += 1
        self.total_energy_consumed += energy_added
        print("🔋 Battery fully recharged to 100%. Ready for next command.\n")

    def run_simulation(self):
        print("==================================================")
        print("   🤖 USER-INVOLVED SMART VACUUM SIMULATION      ")
        print("==================================================")
        print("Initial Setup: Rooms loaded with randomized initial dirt levels.\n")

        while any(data["cleaned_percentage"] < 100 for data in self.rooms.values()):
            self.display_status()

            if self.battery < 15.0:
                self.recharge_battery()
                continue

            print("Select which room the vacuum should target next:")
            for key, data in self.rooms.items():
                if data["cleaned_percentage"] < 100:
                    print(f"  Enter '{key}' to clean {data['name']}")
                else:
                    print(f"  [{key}] {data['name']} is already 100% clean.")
            
            choice = input("Your choice (A or B): ").strip().upper()
            print()

            if choice not in self.rooms:
                print("❌ Invalid selection! Please enter 'A' or 'B'.\n")
                continue

            target_room = self.rooms[choice]

            if target_room["cleaned_percentage"] >= 100:
                print(f"⚠️ {target_room['name']} is already fully cleaned! Choose another room.\n")
                continue

            self.user_choices_count += 1
            print(f"-> Vacuum dispatched to {target_room['name']}...")

            battery_drain = random.randint(20, 40)
            cleaning_progress = random.randint(25, 50)

            if self.battery - battery_drain < 0:
                battery_drain = self.battery
                cleaning_progress = int(cleaning_progress * (battery_drain / 40))

            self.battery -= battery_drain
            self.total_energy_consumed += battery_drain
            
            prev_cleaned = target_room["cleaned_percentage"]
            target_room["cleaned_percentage"] = min(100.0, prev_cleaned + cleaning_progress)
            actual_gain = target_room["cleaned_percentage"] - prev_cleaned

            target_room["dirt"] = max(0, target_room["dirt"] - actual_gain)

            log_msg = f"User selected {target_room['name']}: +{actual_gain}% cleaned, -{battery_drain}% battery used. Dirt remaining: {target_room['dirt']}%"
            self.cleaning_log.append(log_msg)
            print(f"   [{log_msg}]\n")
            
            time.sleep(1)

        self.generate_analytics()

    def generate_analytics(self):
        end_time = time.time()
        total_time_elapsed = round(end_time - self.start_time, 2)
        
        total_cleaned_sum = sum(d["cleaned_percentage"] for d in self.rooms.values())
        efficiency_score = round(total_cleaned_sum / max(1, self.total_energy_consumed), 2)

        print("\n==================================================")
        print("📊 SESSION DATA ANALYTICS & PERFORMANCE REPORT")
        print("==================================================")
        print(f"⏱️ Total Simulation Time  : {total_time_elapsed} seconds")
        print(f"⚡ Total Energy Consumed  : {self.total_energy_consumed:.1f}% battery units")
        print(f"🔌 Total Dock Recharges   : {self.recharge_count} times")
        print(f"👤 Total User Directives  : {self.user_choices_count} choices made")
        print(f"🧹 Final Room Status      :")
        for key, data in self.rooms.items():
            print(f"   - {data['name']}: {data['cleaned_percentage']}% Cleaned | Final Dirt: {data['dirt']}%")
        print(f"📈 Efficiency Score       : {efficiency_score} (Output/Energy Ratio)")
        print("--------------------------------------------------")
        print("📜 User & Operation Log Summary:")
        for idx, log in enumerate(self.cleaning_log, 1):
            print(f"   {idx}. {log}")
        print("==================================================")
        print("🏁 Target Reached! Both rooms clean. Vacuum docked.")

if __name__ == "__main__":
    sim = UserInvolvedVacuum()
    sim.run_simulation()
