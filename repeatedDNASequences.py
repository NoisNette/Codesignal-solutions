return sorted({*re.findall(r"(?=(.{10}))(?=.+\1)", str(vars()))})
