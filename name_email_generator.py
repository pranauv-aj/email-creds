import random
import json
import os

class NameEmailGenerator:
    def __init__(self, data_file='name_email_data.json'):
        self.data_file = data_file
        self.used_data = []
        self.load_data()
        self.first_names = [
            'John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Laura', 'William', 'Emma',
            'James', 'Olivia', 'Daniel', 'Sophia', 'Joseph', 'Isabella', 'Thomas', 'Mia', 'Charles', 'Charlotte',
            'Christopher', 'Amelia', 'Matthew', 'Harper', 'Anthony', 'Evelyn', 'Donald', 'Abigail', 'Steven', 'Emily',
            'Paul', 'Elizabeth', 'Andrew', 'Sofia', 'Joshua', 'Avery', 'Kenneth', 'Ella', 'Kevin', 'Scarlett',
            'Brian', 'Grace', 'George', 'Chloe', 'Edward', 'Victoria', 'Ronald', 'Riley', 'Timothy', 'Aria',
            'Jason', 'Lily', 'Jeffrey', 'Aubrey', 'Ryan', 'Zoey', 'Jacob', 'Hannah', 'Gary', 'Layla',
            'Nicholas', 'Nora', 'Eric', 'Zoe', 'Jonathan', 'Leah', 'Stephen', 'Audrey', 'Larry', 'Savannah',
            'Scott', 'Brooklyn', 'Benjamin', 'Bella', 'Frank', 'Claire', 'Gregory', 'Skylar', 'Raymond', 'Lucy',
            'Alexander', 'Paisley', 'Patrick', 'Everly', 'Jack', 'Anna', 'Dennis', 'Caroline', 'Jerry', 'Nova',
            'Tyler', 'Genesis', 'Aaron', 'Emilia', 'Jose', 'Kennedy', 'Henry', 'Samantha', 'Adam', 'Maya',
            'Mary', 'Peter', 'Barbara', 'Richard', 'Susan', 'Mark', 'Margaret', 'Thomas', 'Lisa', 'Christopher',
            'Nancy', 'Karen', 'Betty', 'Dorothy', 'Sandra', 'Ashley', 'Patricia', 'Linda', 'Deborah', 'Jessica',
            'Kimberly', 'Donna', 'Carol', 'Michelle', 'Emily', 'Amanda', 'Helen', 'Melissa', 'Debra', 'Angela',
            'Brenda', 'Pamela', 'Nicole', 'Samantha', 'Katherine', 'Rachel', 'Janet', 'Catherine', 'Virginia', 'Ruth',
            'Julie', 'Sharon', 'Maria', 'Heather', 'Diane', 'Alice', 'Jacqueline', 'Hannah', 'Jean', 'Doris',
            'Evelyn', 'Judith', 'Megan', 'Andrea', 'Cheryl', 'Olivia', 'Martha', 'Christine', 'Cynthia', 'Amy',
            'Ann', 'Marie', 'Amber', 'Kelly', 'Jennifer', 'Christina', 'Walter', 'Justin', 'Terry', 'Gerald',
            'Keith', 'Samuel', 'Willie', 'Ralph', 'Lawrence', 'Nicholas', 'Roy', 'Benjamin', 'Bruce', 'Brandon',
            'Eugene', 'Harry', 'Carl', 'Arthur', 'Roger', 'Wayne', 'Vincent', 'Russell', 'Louis', 'Bobby',
            'Philip', 'Johnny', 'Randy', 'Alan', 'Jeremy', 'Scott', 'Howard', 'Eugene', 'Carlos', 'Keith',
            'Albert', 'Victor', 'Martin', 'Tony', 'Ernest', 'Phillip', 'Todd', 'Jesse', 'Craig', 'Alan',
            'Shawn', 'Clarence', 'Sean', 'Philip', 'Chris', 'Johnny', 'Earl', 'Jimmy', 'Antonio', 'Bryan',
            'Danny', 'Tony', 'Luis', 'Mike', 'Stanley', 'Leonard', 'Nathan', 'Dale', 'Manuel', 'Curtis',
            'Wendy', 'Dawn', 'Connie', 'Rebecca', 'Kathleen', 'Erica', 'Jamie', 'Sara', 'Theresa', 'Denise',
            'Tammy', 'Irene', 'Carla', 'Carrie', 'Tara', 'Ana', 'Renee', 'Ida', 'Holly', 'Edna',
            'Bonnie', 'Terri', 'Gertrude', 'Lucy', 'Tonya', 'Ella', 'Stacy', 'Wilma', 'Gina', 'Kristin',
            'Natalie', 'Agnes', 'Vera', 'Charlene', 'Bessie', 'Delores', 'Melinda', 'Pearl', 'Arlene', 'Maureen',
            'Colleen', 'Allison', 'Tamara', 'Joy', 'Georgia', 'Constance', 'Lillie', 'Claudia', 'Jackie', 'Marcia',
            'Tanya', 'Nellie', 'Minnie', 'Marlene', 'Heidi', 'Glenda', 'Lydia', 'Viola', 'Courtney', 'Marian',
            'Stella', 'Caroline', 'Dora', 'Jo', 'Vickie', 'Mattie', 'Terry', 'Maxine', 'Irma', 'Mabel',
            'Marsha', 'Myrtle', 'Lena', 'Christy', 'Deanna', 'Patsy', 'Hilda', 'Gwendolyn', 'Jennie', 'Nora',
            'Margie', 'Nina', 'Cassandra', 'Leah', 'Penny', 'Kay', 'Priscilla', 'Naomi', 'Carole', 'Brandy',
            'Olga', 'Billie', 'Dianne', 'Tracey', 'Leona', 'Jenny', 'Felicia', 'Sonia', 'Miriam', 'Velma',
            'Becky', 'Bobbie', 'Violet', 'Kristina', 'Toni', 'Misty', 'Mae', 'Shelly', 'Daisy', 'Ramona',
            'Sherri', 'Erika', 'Katrina', 'Claire', 'Lindsey', 'Lindsay', 'Geneva', 'Guadalupe', 'Belinda', 'Margarita',
            'Sheryl', 'Cora', 'Faye', 'Ada', 'Natasha', 'Sabrina', 'Isabel', 'Marguerite', 'Hattie', 'Harriet',
            'Molly', 'Cecilia', 'Kristi', 'Brandi', 'Blanche', 'Sandy', 'Rosemary', 'Joanna', 'Iris', 'Eunice',
            'Angie', 'Inez', 'Lynda', 'Madeline', 'Amelia', 'Alberta', 'Genevieve', 'Monique', 'Jodi', 'Janie',
            'Maggie', 'Kayla', 'Sonya', 'Jan', 'Lee', 'Kristine', 'Candace', 'Fannie', 'Maryann', 'Opal',
            'Alison', 'Yvette', 'Melody', 'Luz', 'Susie', 'Olivia', 'Flora', 'Shelley', 'Kristy', 'Mamie',
            'Lula', 'Lola', 'Verna', 'Beulah', 'Antoinette', 'Candice', 'Juana', 'Jeannette', 'Pam', 'Kelli',
            'Hannah', 'Whitney', 'Bridget', 'Karla', 'Celia', 'Latoya', 'Patty', 'Shelia', 'Gayle', 'Della'
        ]
        
        self.last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
            'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
            'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson',
            'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
            'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts',
            'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes',
            'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper',
            'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson',
            'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennett', 'Gray', 'Mendoza', 'Ruiz', 'Hughes',
            'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez',
            'Powell', 'Jenkins', 'Perry', 'Russell', 'Sullivan', 'Bell', 'Coleman', 'Butler', 'Henderson', 'Barnes',
            'Gonzales', 'Fisher', 'Vasquez', 'Simmons', 'Romero', 'Jordan', 'Patterson', 'Alexander', 'Hamilton', 'Graham',
            'Reynolds', 'Griffin', 'Wallace', 'Moreno', 'West', 'Cole', 'Hayes', 'Bryant', 'Herrera', 'Gibson',
            'Ellis', 'Tran', 'Medina', 'Aguilar', 'Stevens', 'Murray', 'Ford', 'Castro', 'Marshall', 'Owens',
            'Harrison', 'Fernandez', 'McDonald', 'Woods', 'Washington', 'Kennedy', 'Wells', 'Vargas', 'Henry', 'Chen',
            'Freeman', 'Webb', 'Tucker', 'Guzman', 'Burns', 'Crawford', 'Olson', 'Simpson', 'Porter', 'Hunter',
            'Gordon', 'Mendez', 'Silva', 'Shaw', 'Snyder', 'Mason', 'Dixon', 'Munoz', 'Hunt', 'Hicks',
            'Holmes', 'Palmer', 'Wagner', 'Black', 'Robertson', 'Boyd', 'Rose', 'Stone', 'Salazar', 'Fox',
            'Warren', 'Mills', 'Meyer', 'Rice', 'Schmidt', 'Garza', 'Daniels', 'Ferguson', 'Nichols', 'Stephens',
            'Soto', 'Weaver', 'Ryan', 'Gardner', 'Payne', 'Grant', 'Dunn', 'Kelley', 'Spencer', 'Hawkins',
            'Arnold', 'Pierce', 'Vazquez', 'Hansen', 'Peters', 'Santos', 'Hart', 'Bradley', 'Knight', 'Elliott',
            'Cunningham', 'Duncan', 'Armstrong', 'Hudson', 'Carroll', 'Lane', 'Riley', 'Andrews', 'Alvarado', 'Ray',
            'Deleon', 'Berry', 'Perkins', 'Hoffman', 'Johnston', 'Matthews', 'Pena', 'Richards', 'Contreras', 'Willis',
            'Carpenter', 'Lawrence', 'Sandoval', 'Guerrero', 'George', 'Chapman', 'Rios', 'Estrada', 'Ortega', 'Watkins',
            'Greene', 'Nunez', 'Wheeler', 'Valdez', 'Harper', 'Burke', 'Larson', 'Santiago', 'Maldonado', 'Morrison',
            'Franklin', 'Carlson', 'Austin', 'Dominguez', 'Carr', 'Lawson', 'Jacobs', 'Obrien', 'Lynch', 'Singh',
            'Vega', 'Bishop', 'Montgomery', 'Oliver', 'Jensen', 'Harvey', 'Williamson', 'Gilbert', 'Dean', 'Sims',
            'Espinoza', 'Howell', 'Li', 'Wong', 'Reid', 'Hanson', 'Le', 'McCoy', 'Garrett', 'Burton',
            'Fuller', 'Wang', 'Weber', 'Welch', 'Rojas', 'Lucas', 'Marquez', 'Fields', 'Park', 'Yang',
            'Little', 'Banks', 'Padilla', 'Day', 'Walsh', 'Bowman', 'Schultz', 'Luna', 'Fowler', 'Mejia',
            'Davidson', 'Acosta', 'Brewer', 'May', 'Holland', 'Juarez', 'Newman', 'Pearson', 'Curtis', 'Cortez',
            'Douglas', 'Schneider', 'Joseph', 'Barrett', 'Navarro', 'Figueroa', 'Keller', 'Avila', 'Wade', 'Molina',
            'Stanley', 'Hopkins', 'Campos', 'Barnett', 'Bates', 'Chambers', 'Caldwell', 'Beck', 'Lambert', 'Miranda',
            'Byrd', 'Craig', 'Ayala', 'Lowe', 'Frazier', 'Powers', 'Neal', 'Leonard', 'Gregory', 'Carrillo',
            'Sutton', 'Fleming', 'Rhodes', 'Shelton', 'Schwartz', 'Norris', 'Jennings', 'Watts', 'Duran', 'Walters',
            'Cohen', 'McDaniel', 'Moran', 'Parks', 'Steele', 'Vaughn', 'Becker', 'Holt', 'Deleon', 'Barker',
            'Terry', 'Hale', 'Leon', 'Hail', 'Benson', 'Haynes', 'Horton', 'Miles', 'Lyons','Cohen', 'McDaniel', 'Moran', 'Parks', 'Steele', 'Vaughn', 'Becker', 'Holt', 'Deleon', 'Barker',
            'Knox', 'Little', 'Camacho', 'Gonzales', 'Lindsey', 'Coffey', 'Sloan', 'Moss', 'Fernandez', 'Hodges',
            'Adkins', 'Bush', 'McKay', 'Kirby', 'Wilkins', 'Beard', 'Sharp', 'Ware', 'McBride', 'Hendricks',
            'Friedman', 'Dyer', 'Blackwell', 'Mercado', 'Tanner', 'Eaton', 'Clay', 'Barron', 'Beasley', 'Oneal',
            'Small', 'Preston', 'Wu', 'Zamora', 'Macdonald', 'Vance', 'Snow', 'McClain', 'Stafford', 'Orozco',
            'Barry', 'English', 'Shannon', 'Kline', 'Jacobson', 'Woodard', 'Huang', 'Kemp', 'Mosley', 'Prince',
            'Merritt', 'Hurst', 'Villanueva', 'Roach', 'Nolan', 'Lam', 'Yoder', 'McCullough', 'Lester', 'Santana',
            'Valenzuela', 'Winters', 'Barrera', 'Orr', 'Leach', 'Berger', 'McKee', 'Strong', 'Conway', 'Stein',
            'Whitehead', 'Bullock', 'Escobar', 'Knox', 'Meadows', 'Solomon', 'Velez', 'Odonnell', 'Kerr', 'Stout',
            'Blankenship', 'Browning', 'Kent', 'Lozano', 'Bartlett', 'Pruitt', 'Buck', 'Barr', 'Gaines', 'Durham',
            'Gentry', 'McIntyre', 'Slater', 'Melendez', 'Rocha', 'Herman', 'Sexton', 'Moon', 'Hendrix', 'Rangel',
            'Stark', 'Lowery', 'Hardin', 'Hull', 'Sellers', 'Ellison', 'Calhoun', 'Gillespie', 'Mora', 'Knapp',
            'McCall', 'Morse', 'Dorsey', 'Weeks', 'Nielsen', 'Livingston', 'Leblanc', 'McLean', 'Bradshaw', 'Glass',
            'Baxter', 'Pennington', 'Strickland', 'Atkins', 'Bradford', 'Stein', 'Combs', 'Burgess', 'Greer', 'Briggs',
            'Robles', 'Decker', 'Hickman', 'Dewey', 'Schaefer', 'Finley', 'Todd', 'Rutherford', 'Bentley', 'Dougherty'
    ]

        self.middle_name_formats = [
            lambda m: f"{m}.",  # Space with dot
            lambda m: f"-{m}",  # Hyphen
            lambda m: f"-{m}-",  # Hyphen on both sides
            lambda m: f"_{m}",  # Underscore
            lambda m: m[0],  # First letter only
            lambda m: f"{m[0]}.",  # First letter with dot
        ]

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                if 'used_data' in data:
                    self.used_data = data['used_data']
                elif 'used_names' in data:
                    # Convert old format to new format
                    self.used_data = [{'first_name': name[0], 'middle_name': '', 'last_name': name[1], 'email': ''} 
                                      for name in data['used_names']]
                else:
                    self.used_data = []
        else:
            self.used_data = []

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump({'used_data': self.used_data}, f)

    def generate_name(self):
        while True:
            first_name = random.choice(self.first_names)
            middle_name = random.choice(self.first_names)  # Using first names as middle names
            last_name = random.choice(self.last_names)
            middle_name_format = random.choice(self.middle_name_formats)
            formatted_middle_name = middle_name_format(middle_name)
            
            if not any(entry['first_name'] == first_name and entry['last_name'] == last_name for entry in self.used_data):
                return first_name, formatted_middle_name, last_name

    def run(self):
        try:
            while True:
                first_name, middle_name, last_name = self.generate_name()
                print(f"\nGenerated name: {first_name}{middle_name}{last_name}")
                email = input("Enter email address (or 'q' to quit): ").strip()
                if email.lower() == 'q':
                    break
                self.used_data.append({
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'email': email
                })
                print(f"Recorded: {first_name}{middle_name} {last_name} - {email}")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
        finally:
            self.save_data()
            print("Data saved. Goodbye!")

if __name__ == "__main__":
    generator = NameEmailGenerator()
    generator.run()