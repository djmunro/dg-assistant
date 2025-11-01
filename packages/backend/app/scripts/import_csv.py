import csv
from pathlib import Path

from app.db.schema import Base, SessionLocal, engine
from app.models.disc import DiscCreate
from app.services.disc_service import DiscService

# Ensure tables exist
Base.metadata.create_all(bind=engine)


def import_csv(csv_path: Path):
    """Import CSV file into database - combines Manufacturer/Distributor and Disc Model into name."""
    session = SessionLocal()
    service = DiscService(session=session)

    imported_count = 0
    skipped_count = 0

    try:
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row_num, row in enumerate(reader, start=2):  # start=2 for header row
                # Extract the columns we care about
                manufacturer = row.get("Manufacturer / Distributor", "").strip()
                disc_model = row.get("Disc Model", "").strip()

                # Skip rows with missing data
                if not manufacturer or not disc_model:
                    print(f"⚠️  Row {row_num}: Skipping - missing data")
                    skipped_count += 1
                    continue

                # Combine manufacturer and model into single name field
                name = f"{manufacturer} {disc_model}"

                # Create disc using service
                disc_create = DiscCreate(name=name)
                service.create_disc(disc_create)
                imported_count += 1

        print(f"✅ Imported {imported_count} discs")
        if skipped_count > 0:
            print(f"⚠️  Skipped {skipped_count} rows with missing data")
    finally:
        session.close()


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m app.scripts.import_csv <file.csv>")
        sys.exit(1)

    csv_path = Path(sys.argv[1])

    if not csv_path.exists():
        print(f"❌ Error: File not found: {csv_path}")
        sys.exit(1)

    print(f"📁 Importing from: {csv_path}")
    import_csv(csv_path)


if __name__ == "__main__":
    main()
