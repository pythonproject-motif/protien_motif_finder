# Protein Motif Finder

A simple Flask web app for finding motifs in protein sequences using regular expressions.

## Run locally

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## GitHub

Create a new GitHub repository and upload all project files.

```bash
git init
git add .
git commit -m "Add protein motif finder"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## Deployment

The project includes a `Procfile` and `runtime.txt` for deployment services that support Python web apps, such as Render.

For Render, create a new Web Service from the GitHub repository.

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```

## Included motifs

- N-glycosylation: `N[^P][ST][^P]`
- Cys pair: `C.{2,20}C`
- Histidine pair: `H.{2,20}H`
- RGD motif: `RGD`

You can also enter a custom motif using Python regular expression syntax.
