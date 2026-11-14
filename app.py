import re
from flask import Flask, render_template, request

app = Flask(__name__)

DEFAULT_PATTERNS = {
    "N-glycosylation": r"N[^P][ST][^P]",
    "Cys pair": r"C.{2,20}C",
    "Histidine pair": r"H.{2,20}H",
    "RGD motif": r"RGD"
}

def clean_sequence(sequence):
    sequence = re.sub(r"[^A-Za-z]", "", sequence).upper()
    return sequence

def find_motifs(sequence, patterns):
    results = []

    for name, pattern in patterns.items():
        try:
            matches = list(re.finditer(pattern, sequence))
        except re.error as error:
            results.append({
                "name": name,
                "pattern": pattern,
                "error": str(error),
                "matches": []
            })
            continue

        found = []
        for match in matches:
            found.append({
                "start": match.start() + 1,
                "end": match.end(),
                "sequence": match.group()
            })

        results.append({
            "name": name,
            "pattern": pattern,
            "error": None,
            "matches": found
        })

    return results

@app.route("/", methods=["GET", "POST"])
def index():
    sequence = ""
    results = []
    custom_name = ""
    custom_pattern = ""

    if request.method == "POST":
        sequence = clean_sequence(request.form.get("sequence", ""))
        custom_name = request.form.get("custom_name", "").strip()
        custom_pattern = request.form.get("custom_pattern", "").strip()

        patterns = dict(DEFAULT_PATTERNS)

        if custom_name and custom_pattern:
            patterns[custom_name] = custom_pattern

        if sequence:
            results = find_motifs(sequence, patterns)

    total_matches = sum(len(item["matches"]) for item in results)

    return render_template(
        "index.html",
        sequence=sequence,
        results=results,
        total_matches=total_matches,
        custom_name=custom_name,
        custom_pattern=custom_pattern
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
