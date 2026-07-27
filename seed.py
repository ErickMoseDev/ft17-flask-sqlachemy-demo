from datetime import date
from app import app, bcrypt
from models import db, User, Profile, Book


with app.app_context():
    User.query.delete()
    Profile.query.delete()
    Book.query.delete()

    users = [
        User(
            first_name="Alice",
            last_name="Johnson",
            email_address="alice.johnson@gmail.com",
            phone="0700000001",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Bob",
            last_name="Smith",
            email_address="bob.smith@gmail.com",
            phone="0700000002",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Carol",
            last_name="Williams",
            email_address="carol.williams@gmail.com",
            phone="0700000003",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="David",
            last_name="Brown",
            email_address="david.brown@gmail.com",
            phone="0700000004",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Eva",
            last_name="Jones",
            email_address="eva.jones@gmail.com",
            phone="0700000005",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Frank",
            last_name="Garcia",
            email_address="frank.garcia@gmail.com",
            phone="0700000006",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Grace",
            last_name="Martinez",
            email_address="grace.martinez@gmail.com",
            phone="0700000007",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Henry",
            last_name="Davis",
            email_address="henry.davis@gmail.com",
            phone="0700000008",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Irene",
            last_name="Wilson",
            email_address="irene.wilson@gmail.com",
            phone="0700000009",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="James",
            last_name="Taylor",
            email_address="james.taylor@gmail.com",
            phone="0700000010",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Karen",
            last_name="Anderson",
            email_address="karen.anderson@gmail.com",
            phone="0700000011",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Leo",
            last_name="Thomas",
            email_address="leo.thomas@gmail.com",
            phone="0700000012",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Mia",
            last_name="Jackson",
            email_address="mia.jackson@gmail.com",
            phone="0700000013",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Nathan",
            last_name="White",
            email_address="nathan.white@gmail.com",
            phone="0700000014",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Olivia",
            last_name="Harris",
            email_address="olivia.harris@gmail.com",
            phone="0700000015",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Paul",
            last_name="Martin",
            email_address="paul.martin@gmail.com",
            phone="0700000016",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Quinn",
            last_name="Thompson",
            email_address="quinn.thompson@gmail.com",
            phone="0700000017",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Rachel",
            last_name="Clark",
            email_address="rachel.clark@gmail.com",
            phone="0700000018",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Samuel",
            last_name="Lewis",
            email_address="samuel.lewis@gmail.com",
            phone="0700000019",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
        User(
            first_name="Tina",
            last_name="Walker",
            email_address="tina.walker@gmail.com",
            phone="0700000020",
            password=bcrypt.generate_password_hash("12345").decode("utf-8"),
        ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print(f"Seeded {len(users)} users.")

    # --- Profiles (one per user, linked via user_id FK) ---
    (
        alice,
        bob,
        carol,
        david,
        eva,
        frank,
        grace,
        henry,
        irene,
        james,
        karen,
        leo,
        mia,
        nathan,
        olivia,
        paul,
        quinn,
        rachel,
        samuel,
        tina,
    ) = users

    profiles = [
        Profile(
            user_id=alice.id,
            dob=date(1990, 3, 15),
            gender="female",
            role="admin",
            bio="Tech enthusiast and lifelong learner.",
        ),
        Profile(
            user_id=bob.id,
            dob=date(1985, 7, 22),
            gender="male",
            role="staff",
            bio="Avid reader and coffee lover.",
        ),
        Profile(
            user_id=carol.id,
            dob=date(1993, 11, 5),
            gender="female",
            role="user",
            bio="Passionate about literature and travel.",
        ),
        Profile(
            user_id=david.id,
            dob=date(1988, 1, 30),
            gender="male",
            role="staff",
            bio="Software developer by day, writer by night.",
        ),
        Profile(
            user_id=eva.id,
            dob=date(1995, 6, 18),
            gender="female",
            role="user",
            bio="Loves sci-fi novels and hiking.",
        ),
        Profile(
            user_id=frank.id,
            dob=date(1980, 9, 11),
            gender="male",
            role="admin",
            bio="Veteran programmer and open-source advocate.",
        ),
        Profile(
            user_id=grace.id,
            dob=date(1992, 4, 25),
            gender="female",
            role="user",
            bio="Bookworm with a passion for history.",
        ),
        Profile(
            user_id=henry.id,
            dob=date(1987, 12, 3),
            gender="male",
            role="staff",
            bio="Sports fan and amateur novelist.",
        ),
        Profile(
            user_id=irene.id,
            dob=date(1994, 8, 14),
            gender="female",
            role="user",
            bio="Graphic designer and fantasy fiction fan.",
        ),
        Profile(
            user_id=james.id,
            dob=date(1983, 2, 19),
            gender="male",
            role="staff",
            bio="Data scientist with a love for thrillers.",
        ),
        Profile(
            user_id=karen.id,
            dob=date(1991, 5, 7),
            gender="female",
            role="user",
            bio="Teacher and children's book enthusiast.",
        ),
        Profile(
            user_id=leo.id,
            dob=date(1989, 10, 23),
            gender="male",
            role="user",
            bio="Philosopher and mystery genre devotee.",
        ),
        Profile(
            user_id=mia.id,
            dob=date(1997, 1, 12),
            gender="female",
            role="user",
            bio="Young entrepreneur and self-help book fan.",
        ),
        Profile(
            user_id=nathan.id,
            dob=date(1986, 7, 9),
            gender="male",
            role="staff",
            bio="Marketing manager and biography reader.",
        ),
        Profile(
            user_id=olivia.id,
            dob=date(1990, 3, 28),
            gender="female",
            role="user",
            bio="Nurse who unwinds with romance novels.",
        ),
        Profile(
            user_id=paul.id,
            dob=date(1984, 11, 17),
            gender="male",
            role="admin",
            bio="Architect with a keen interest in design books.",
        ),
        Profile(
            user_id=quinn.id,
            dob=date(1996, 6, 30),
            gender="male",
            role="user",
            bio="Music producer and poetry lover.",
        ),
        Profile(
            user_id=rachel.id,
            dob=date(1993, 9, 4),
            gender="female",
            role="user",
            bio="Environmental scientist and nature writer.",
        ),
        Profile(
            user_id=samuel.id,
            dob=date(1981, 4, 16),
            gender="male",
            role="staff",
            bio="Chef who enjoys culinary and travel memoirs.",
        ),
        Profile(
            user_id=tina.id,
            dob=date(1998, 12, 21),
            gender="female",
            role="user",
            bio="Film student fascinated by screenwriting.",
        ),
    ]

    db.session.add_all(profiles)
    db.session.commit()
    print(f"Seeded {len(profiles)} profiles.")

    # --- Books (linked to users via user_id FK) ---
    books = [
        # Alice's books
        Book(title="The Code Whisperer", genre="Technology", user_id=alice.id),
        Book(title="Algorithms of the Heart", genre="Romance", user_id=alice.id),
        # Bob's books
        Book(title="Brewed Awakening", genre="Fiction", user_id=bob.id),
        Book(title="Chapters of Silence", genre="Drama", user_id=bob.id),
        # Carol's books
        Book(title="Wanderlust Chronicles", genre="Travel", user_id=carol.id),
        # David's books
        Book(title="Midnight Pull Requests", genre="Technology", user_id=david.id),
        Book(title="The Debugger's Diary", genre="Comedy", user_id=david.id),
        Book(title="Refactoring Life", genre="Self-Help", user_id=david.id),
        # Eva's books
        Book(title="Stars Beyond the Firewall", genre="Sci-Fi", user_id=eva.id),
        Book(title="Trail Blazers", genre="Adventure", user_id=eva.id),
        # Frank's books
        Book(title="Open Source Odyssey", genre="Technology", user_id=frank.id),
        # Grace's books
        Book(title="Pages of the Past", genre="History", user_id=grace.id),
        Book(title="The Archivist", genre="Mystery", user_id=grace.id),
        # Henry's books
        Book(title="Overtime", genre="Sports", user_id=henry.id),
        Book(title="The Last Draft", genre="Fiction", user_id=henry.id),
        # Irene's books
        Book(title="Pixels and Dragons", genre="Fantasy", user_id=irene.id),
        # James's books
        Book(title="Data Don't Lie", genre="Technology", user_id=james.id),
        Book(title="The Stockholm Variable", genre="Thriller", user_id=james.id),
        # Karen's books
        Book(title="Little Readers", genre="Children", user_id=karen.id),
        Book(title="The Classroom Garden", genre="Children", user_id=karen.id),
        # Leo's books
        Book(title="Socrates in Suburbia", genre="Philosophy", user_id=leo.id),
        Book(title="The Butler Did It", genre="Mystery", user_id=leo.id),
        # Mia's books
        Book(title="Zero to One Hundred", genre="Self-Help", user_id=mia.id),
        # Nathan's books
        Book(title="The Brand Inside", genre="Business", user_id=nathan.id),
        Book(title="Life in Headlines", genre="Biography", user_id=nathan.id),
        # Olivia's books
        Book(title="When Hearts Heal", genre="Romance", user_id=olivia.id),
        # Paul's books
        Book(title="Blueprint of Dreams", genre="Architecture", user_id=paul.id),
        Book(title="Spaces and Stories", genre="Design", user_id=paul.id),
        # Quinn's books
        Book(title="Verse and Verse Again", genre="Poetry", user_id=quinn.id),
        # Rachel's books
        Book(title="Green Chapters", genre="Environment", user_id=rachel.id),
        Book(title="The River Speaks", genre="Nature", user_id=rachel.id),
        # Samuel's books
        Book(title="Flavors I've Known", genre="Memoir", user_id=samuel.id),
        Book(title="The Wandering Plate", genre="Travel", user_id=samuel.id),
        # Tina's books
        Book(title="Cut to Scene", genre="Screenplay", user_id=tina.id),
        Book(title="Frames of Reference", genre="Film", user_id=tina.id),
    ]

    db.session.add_all(books)
    db.session.commit()
    print(f"Seeded {len(books)} books.")
