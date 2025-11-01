## Starting the server:

```bash
uv run uvicorn app.main:app --reload
```

## Import Disc Data

### 1. Download the CSV

Go to: https://www.pdga.com/technical-standards/equipment-certification/discs

Click the "CSV" download button to get the latest approved discs CSV file.

### 2. Save it to the assets folder

```bash
# Create assets folder if it doesn't exist
mkdir -p assets

# Move your downloaded CSV to assets/
mv ~/Downloads/pdga-approved-disc-golf-discs_*.csv assets/
```

### 3. Import into database

```bash
uv run --package backend python -m app.scripts.import_csv assets/pdga-approved-disc-golf-discs_2025-10-31T17-36-46.csv
```

## Example requests:

Here's a set of simple curl examples you can use to interact with your FastAPI app once it’s running (default at http://localhost:8000):

1. Create a User

```bash
curl -X POST "http://localhost:8000/api/v1/users" \
 -H "Content-Type: application/json" \
 -d '{"name": "Ada Lovelace"}'
```

2. Get All Users

```bash
curl -X GET "http://localhost:8000/api/v1/users"
```

3. Get a User by ID

(Replace 1 with the actual ID from the create response)

```bash
curl -X GET "http://localhost:8000/api/v1/users/1"
```

4. Update a User

```bash
curl -X PUT "http://localhost:8000/api/v1/users/1" \
 -H "Content-Type: application/json" \
 -d '{"name": "Grace Hopper"}'
```

5. Delete a User

```bash
curl -X DELETE "http://localhost:8000/api/v1/users/1"
```
