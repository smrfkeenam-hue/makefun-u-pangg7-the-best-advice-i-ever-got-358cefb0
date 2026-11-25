import os

# One sentence, 179 characters: the best advice the writer ever got,
# from a named giver (Grandma) in a real moment (shelling peas on the
# porch the night Dad left). Concrete, earned, and true beyond its moment.
ENTRY = "Grandma, shelling peas on the porch the night Dad left, told me to marry the one who washes the dishes without being asked, because love is what people do when no one is watching."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Write exactly the sentence, no trailing newline: the gate counts 1-200 chars.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
