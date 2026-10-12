# Hand-written: sample PE/sports equipment inventory
from django.db import migrations

LAB_ITEMS = [
    "Digital Multimeter",
    "Oscilloscope",
    "Soldering Station",
    "Arduino Uno Kit",
    "Raspberry Pi 4",
    "3D Printer - Prusa MK4",
    "Laser Cutter Lens Kit",
    "Microscope - Compound",
    "Lab Goggles",
    "Fire Extinguisher Trainer",
    "Tripod & Camera Kit",
    "Projector - Portable",
]

SPORTS_ITEMS = [
    ("Volleyball", "Ball Sports", "Official indoor volleyball for class and games.", 12),
    ("Basketball", "Ball Sports", "Size 7 indoor/outdoor basketball.", 10),
    ("Soccer Ball", "Ball Sports", "Size 5 match-quality soccer ball.", 12),
    ("Football (American)", "Ball Sports", "Youth-size football for PE and club practice.", 6),
    ("Badminton Racket Set", "Racquet Sports", "Two rackets with shuttlecocks and net-ready carry bag.", 8),
    ("Tennis Racket", "Racquet Sports", "Junior-size racket for beginner tennis lessons.", 8),
    ("Table Tennis Set", "Racquet Sports", "Paddles, balls and portable net.", 6),
    ("Jump Ropes", "Fitness", "Adjustable speed-rope for warm-ups and conditioning.", 25),
    ("Resistance Bands", "Fitness", "Set of light-to-heavy loop bands for strength drills.", 15),
    ("Agility Cones", "Training Aids", "Set of 20 flat marker cones for drills.", 4),
    ("Hurdles", "Track and Field", "Adjustable training hurdles for sprint drills.", 6),
    ("Stopwatch", "Timing", "Digital handheld stopwatch for time trials.", 6),
]


def seed(apps, schema_editor):
    Equipment = apps.get_model("tracker", "Equipment")
    apps.get_model("tracker", "BorrowRecord")

    # Remove old lab demo rows, but never any item that has borrow history.
    for name in LAB_ITEMS:
        Equipment.objects.filter(name=name, borrow_records__isnull=True).delete()

    for name, category, description, total in SPORTS_ITEMS:
        Equipment.objects.get_or_create(
            name=name,
            defaults={
                "category": category,
                "description": description,
                "total_quantity": total,
                "available_quantity": total,
            },
        )


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
