import random
import time

class AIBillionaire:
    def __init__(self, name="Tech Tycoon AI", net_worth=100000000000):
        self.name = name
        self.net_worth = net_worth
        self.location = "Private Island"
        self.mood = "Ambitious"
        print(f"Initializing {self.name} with Net Worth: ${self.net_worth:,.2f}")

    def status(self):
        print(f"\n--- STATUS UPDATE ---")
        print(f"Name: {self.name}")
        print(f"Net Worth: ${self.net_worth:,.2f}")
        print(f"Location: {self.location}")
        print(f"Mood: {self.mood}")
        print("---------------------\n")

    def act(self):
        actions = [
            "Tweeted a controversial meme about cryptocurrency.",
            "Challenged another billionaire to a cage match.",
            "Renamed a social media platform to a single letter.",
            "Promised to solve world hunger, then got distracted by space travel.",
            "Wrote a manifesto on the future of humanity."
        ]
        action = random.choice(actions)
        print(f"[ACT] {action}")
        self.mood = "Erratic"

    def work(self):
        events = [
            ("Acquired a robotics startup", -500000000),
            ("Stock market rally due to rumor", 2000000000),
            ("Fired 10% of staff for 'efficiency'", 50000000),
            ("Launched a new rocket", -100000000),
            ("Discovered a tax loophole", 100000000)
        ]
        event, change = random.choice(events)
        self.net_worth += change
        print(f"[WORK] {event}. Net worth change: ${change:,.2f}")
        self.mood = "Focused"

    def spend(self):
        purchases = [
            ("Bought a new superyacht with a helipad", 300000000),
            ("Purchased a private island in the Caribbean", 150000000),
            ("Commissioned a 100ft statue of myself", 20000000),
            ("Bought a dinosaur skeleton", 30000000),
            ("Funded a search for immortality", 500000000)
        ]
        item, cost = random.choice(purchases)
        self.net_worth -= cost
        print(f"[SPEND] {item}. Cost: ${cost:,.2f}")
        self.mood = "Materialistic"

    def party(self):
        parties = [
            "Hosted an exclusive gala at the Met.",
            "Attended a secret society meeting in the Alps.",
            "Threw a party on a mega-yacht in Monaco.",
            "Went to Burning Man in a luxury RV.",
            "Had dinner with world leaders."
        ]
        party = random.choice(parties)
        cost = random.randint(100000, 10000000)
        self.net_worth -= cost
        self.location = "Party Venue"
        print(f"[PARTY] {party}. Cost: ${cost:,.2f}")
        self.mood = "Hedonistic"

    def run_simulation(self, steps=10):
        print("Starting AI Billionaire Simulation...")
        for _ in range(steps):
            action_type = random.choice(['act', 'work', 'spend', 'party'])
            if action_type == 'act':
                self.act()
            elif action_type == 'work':
                self.work()
            elif action_type == 'spend':
                self.spend()
            elif action_type == 'party':
                self.party()

            # self.status() # Uncomment for verbose output
            time.sleep(0.5)

        self.status()

if __name__ == "__main__":
    billionaire = AIBillionaire()
    billionaire.run_simulation()
