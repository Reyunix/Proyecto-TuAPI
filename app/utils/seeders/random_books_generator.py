from sqlmodel import Session
from app.db.database import engine
from faker import Faker
from app.routers.books import fetch_create_book
import random
import json
from app.models.books import Book
# Configuración de la semilla de datos aleatorios
common_western_language_codes = [
    "en",  # English
    "es",  # Spanish
    "fr",  # French
    "de",  # German
    "it",  # Italian
    "pt",  # Portuguese
]
book_categories = [
    "literary-fiction",
    "historical-fiction",
    "science-fiction",
    "fantasy",
    "mystery",
    "thriller",
    "suspense",
    "horror",
    "romance",
    "adventure",
    "magical-realism",
    "dystopian",
    "utopian",
    "crime-fiction",
    "satire",
    "coming-of-age",
    "contemporary-fiction",
    "paranormal-fiction",
    "urban-fantasy",
    "fairy-tales",
    "biography",
    "memoir",
    "autobiography",
    "self-help",
    "personal-development",
    "psychology",
    "philosophy",
    "science",
    "history",
    "politics",
    "economics",
    "true-crime",
    "religion-spirituality",
    "travel",
    "health-wellness",
    "parenting",
    "education",
    "business-finance",
    "technology",
    "essays",
    "young-adult-fiction",
    "ya-romance",
    "ya-fantasy",
    "ya-dystopian",
    "middle-grade",
    "childrens-picture-books",
    "early-readers",
    "chapter-books",
    "cozy-mystery",
    "sci-fi-romance",
    "romantic-suspense",
    "historical-romance",
    "post-apocalyptic",
    "cyberpunk",
    "steampunk",
    "dark-fantasy",
    "high-fantasy",
    "low-fantasy",
    "space-opera",
    "gothic-fiction",
    "lgbtq-fiction",
    "new-adult",
    "chick-lit",
    "christian-fiction",
    "climate-fiction"
]
subtitle_templates = [
    "A Journey Through Time and Shadows",
    "The Beginning of a Dark Legacy",
    "Chronicles of Forgotten Realms",
    "Memoirs from a Lost World",
    "The Untold Story Behind the Mask",
    "When Prophecies Become Reality",
    "From Ashes to Eternity",
    "The Battle Between Light and Darkness",
    "Where Magic and Madness Collide",
    "The Truth Buried in Silence",
    "A Tale of Power, Betrayal and Redemption",
    "In the Heart of the Forbidden Lands",
    "An Ancient Evil Awakens",
    "Guardians of a Shattered Realm",
    "A Love Doomed by Fate",
    "Secrets Hidden Beneath the Surface",
    "Legends Carved in Stone",
    "Dreams Lost in the Mist",
    "A Whisper from Beyond the Grave",
    "Voices That Should Not Be Heard",
    "Echoes of a Forgotten Prophecy",
    "The Price of Immortality",
    "In Search of the Last Light",
    "The Curse That Bound Them",
    "Footsteps in the Realm of Nightmares",
    "The Final Chapter of Hope",
    "A Kingdom Drowning in Secrets",
    "Unveiling the Eyes of Destiny",
    "The Song That Broke the Silence",
    "Rituals Written in Blood",
    "Tides of Time and Treachery",
    "The Last Heir of the Fallen Throne",
    "The Portal Between Dreams and Death",
    "A Pact Sealed in Shadows",
    "The Mirror That Lied",
    "Through the Flames of Vengeance",
    "Stories Etched in the Void",
    "A Beacon in the Realm of Dusk",
    "Hearts Torn by War and Wonder",
    "The Path Between Stars and Sorrow"
]
adjectives = [
    "Silent", "Hidden", "Dark", "Eternal", "Forgotten", "Whispering", "Broken", "Sacred", "Fallen", "Crimson",
    "Twisted", "Secret", "Burning", "Frozen", "Ancient", "Lonely", "Golden", "Savage", "Deadly", "Hollow",
    "Radiant", "Cursed", "Misty", "Distant", "Shattered", "Obsidian", "Gilded", "Echoing", "Vanishing", "Lurking",
    "Haunted", "Enchanted", "Mysterious", "Wicked", "Shadowy", "Luminous", "Stormy", "Majestic", "Infernal", "Celestial",
    "Tainted", "Rusty", "Grim", "Ghostly", "Feral", "Nocturnal", "Frosted", "Gloomy", "Timeless", "Vengeful",
    "Delirious", "Desolate", "Vast", "Sinister", "Mythic", "Chilling", "Ghastly", "Arcane", "Velvet", "Bleeding",
    "Savory", "Wounded", "Infinite", "Doomed", "Fiery", "Icy", "Morbid", "Serene", "Fabled", "Unholy",
    "Cracked", "Bleak", "Roaring", "Divine", "Sorrowful", "Tempestuous", "Burnished", "Nameless", "Fractured", "Drifting",
    "Verdant", "Harmonic", "Merciless", "Spectral", "Emerald", "Ruthless", "Astral", "Lurking", "Nameless", "Whimsical",
    "Obscure", "Bleached", "Flickering", "Radiated", "Ominous", "Thorned", "Wretched", "Howling", "Starless", "Weeping",
    "Molten", "Veiled", "Shifting", "Blazing", "Pale", "Desperate", "Tragic", "Boundless", "Ashen", "Bleeding",
    "Runed", "Silvered", "Blighted", "Eclipsed", "Sacrificial", "Trembling", "Restless", "Tormented", "Transcendent", "Shimmering"
]
nouns = [
    "Forest", "Kingdom", "Dreams", "Echoes", "Temple", "Empire", "Souls", "Voices", "Night", "Maze",
    "Ocean", "Shadows", "Fire", "Throne", "Dagger", "Chronicles", "Curse", "Prophecy", "Storm", "Ashes",
    "Guardian", "Path", "Horizon", "Depths", "Tomb", "Covenant", "Mist", "Fate", "Oath", "Abyss",
    "Moon", "Crown", "Mirror", "Grave", "Rose", "Hunt", "Whispers", "Beast", "Altar", "Sanctuary",
    "Serpent", "Blade", "Mask", "Star", "Book", "Cage", "Eye", "Ritual", "Key", "Feather",
    "Flood", "Web", "Spire", "Silence", "Burden", "Vault", "Lantern", "Scroll", "Descent", "Reckoning",
    "Witch", "Watcher", "Raven", "Oracle", "Clock", "Furnace", "Labyrinth", "Obelisk", "Hollow", "Flame",
    "Veil", "Spell", "Cavern", "Phoenix", "Drifter", "Wound", "Bastion", "Sanctum", "Howl", "Shard",
    "Tide", "Catacomb", "Banner", "Crescent", "Ember", "Gale", "Tear", "Bloom", "Plague", "Nest",
    "Grimoire", "Horn", "Fang", "Cloak", "Revenant", "Idol", "Crown", "Blood", "Trial", "Warden",
    "Mark", "Bargain", "Grasp", "Specter", "Reign", "Torch", "Dawn", "Drum", "Chain", "Charm",
    "Riddle", "Mirror", "Chasm", "Pact", "Scripture", "Fang", "Trance", "Echo", "Burial", "Flesh"
]
# Lista de funciones lambda para aletoreizar más aún los títulos de los libros
structures = [
    lambda adj, noun: f"The {adj} {noun}",
    lambda adj, noun: f"An {adj} {noun}" if adj[0].lower() in 'aeiou' else f"A {adj} {noun}",
    lambda adj, noun: f"{adj} {noun}",
    lambda adj, noun: f"{noun} of the {adj}",
    lambda adj, noun: f"The {noun} of {adj}ness",
    lambda adj, noun: f"The {noun} Beneath the {adj} Sky",
    lambda adj, noun: f"The {adj} Tale of the {noun}",
    lambda adj, noun: f"In the {adj} {noun}",
    lambda adj, noun: f"Whispers of the {adj} {noun}",
    lambda adj, noun: f"Under the {adj} {noun}",
    lambda adj, noun: f"Between {adj} and {noun}",
    lambda adj, noun: f"Echoes of a {adj} {noun}",
    lambda adj, noun: f"Among the {adj} {noun}s",
    lambda adj, noun: f"Songs of the {adj} {noun}",
    lambda adj, noun: f"The {adj} {noun}'s Legacy",
    lambda adj, noun: f"The {adj} {noun} Chronicles",
    lambda adj, noun: f"The {noun} of Lost {adj}ness",
    lambda adj, noun: f"The Rise of the {adj} {noun}",
    lambda adj, noun: f"The Fall of the {adj} {noun}",
    lambda adj, noun: f"Return to the {adj} {noun}",
    lambda adj, noun: f"Journey through the {adj} {noun}",
    lambda adj, noun: f"Beneath the {adj} {noun}",
    lambda adj, noun: f"The {adj} {noun} Prophecy",
    lambda adj, noun: f"The {adj} {noun} Files",
    lambda adj, noun: f"The Curse of the {adj} {noun}",
    lambda adj, noun: f"Legends of the {adj} {noun}",
    lambda adj, noun: f"Tales from the {adj} {noun}",
    lambda adj, noun: f"The {adj} {noun} and Other Stories",
    lambda adj, noun: f"The {adj} {noun} of Tomorrow",
    lambda adj, noun: f"The {adj} {noun} of Time",
    lambda adj, noun: f"The {adj} {noun} Within",
    lambda adj, noun: f"Memories of a {adj} {noun}",
    lambda adj, noun: f"Voices from the {adj} {noun}",
    lambda adj, noun: f"Letters to a {adj} {noun}",
    lambda adj, noun: f"The {adj} {noun} We Forgot",
    lambda adj, noun: f"The {adj} {noun} That Wasn't",
    lambda adj, noun: f"The {adj} {noun} of Dreams",
    lambda adj, noun: f"The {adj} {noun} Manifesto",
    lambda adj, noun: f"Blood of the {adj} {noun}",
    lambda adj, noun: f"The {adj} {noun}'s Game"
]


def generate_book_title():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    structure = random.choice(structures)
    return structure(adj, noun)
# Función para generar libros aleatorios fácilmente
def create_random_books(quantity: int, session: Session):
    fk = Faker()
    print("-- Generador de libros aleatorios --")
 
    for _ in range(quantity):        
        book_data = {
            "title": generate_book_title(),
            "subtitle": random.choice(subtitle_templates),
            "authors": json.dumps([fk.name() for _ in range(random.randint(1,3))]),
            "categories": json.dumps([random.choice(book_categories) for _ in range(random.randint(1,2))]),
            "publisher": fk.company(),
            "publishedDate": fk.date(),
            "pageCount": random.randint(50, 2000),
            "imageLinks": fk.image_url(),
            "language": random.choice(common_western_language_codes),
            "isbn_13": fk.isbn13(),
            "isbn_10": fk.isbn10()            
            }
        book_data = Book(**book_data)
        fetch_create_book(session, book_data)        
    print(f"\n{quantity} libros creados correctamente")



if __name__ == "__main__":    
    try:
        quantity = int(input("Cantidad de libros: "))
        with Session(engine) as session:         
            create_random_books(quantity, session)
    except ValueError as error:
        print("\nIngresa un número válido\n", error)